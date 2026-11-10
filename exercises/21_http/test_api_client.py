import json
import time

import httpx
import pytest
from api_client import (
    create_item,
    fetch_all_items,
    fetch_json,
    get_user_name,
    get_with_retry,
    make_client,
    search,
)

BASE = "https://api.test"


def client_for(handler) -> httpx.Client:
    return make_client(BASE, "s3cret", transport=httpx.MockTransport(handler))


def test_make_client_config():
    seen = []

    def handler(request):
        seen.append(request)
        return httpx.Response(200, json={})

    client = client_for(handler)
    client.get("/ping")
    assert seen[0].url == f"{BASE}/ping"
    assert seen[0].headers["Authorization"] == "Bearer s3cret"
    assert client.timeout.read == 5.0


def test_fetch_json():
    client = client_for(lambda r: httpx.Response(200, json={"a": 1}))
    assert fetch_json(client, "/x") == {"a": 1}


def test_fetch_json_error_status():
    client = client_for(lambda r: httpx.Response(500))
    with pytest.raises(httpx.HTTPStatusError):
        fetch_json(client, "/x")


def test_get_user_name_found():
    seen = []

    def handler(request):
        seen.append(request)
        return httpx.Response(200, json={"id": 7, "name": "Ada"})

    assert get_user_name(client_for(handler), 7) == "Ada"
    assert [r.url.path for r in seen] == ["/users/7"]


def test_get_user_name_missing():
    client = client_for(lambda r: httpx.Response(404, json={"error": "nope"}))
    assert get_user_name(client, 1) is None


def test_get_user_name_server_error_raises():
    client = client_for(lambda r: httpx.Response(503))
    with pytest.raises(httpx.HTTPStatusError):
        get_user_name(client, 1)


def test_search_sends_params():
    seen = []

    def handler(request):
        seen.append(request)
        return httpx.Response(200, json={"results": [{"name": "x"}, {"name": "y"}]})

    assert search(client_for(handler), "a b&c", limit=3) == ["x", "y"]
    assert len(seen) == 1
    assert seen[0].url.path == "/search"
    assert seen[0].url.params["q"] == "a b&c"
    assert seen[0].url.params["limit"] == "3"


def test_search_default_limit():
    seen = []

    def handler(request):
        seen.append(request)
        return httpx.Response(200, json={"results": []})

    assert search(client_for(handler), "q") == []
    assert [r.url.params["limit"] for r in seen] == ["10"]


def test_create_item_posts_json():
    seen = []

    def handler(request):
        seen.append(request)
        return httpx.Response(201, json={"id": 42})

    assert create_item(client_for(handler), "widget") == 42
    assert len(seen) == 1
    assert seen[0].method == "POST"
    assert seen[0].url.path == "/items"
    assert json.loads(seen[0].content) == {"name": "widget"}


def test_create_item_error():
    client = client_for(lambda r: httpx.Response(422, json={}))
    with pytest.raises(httpx.HTTPStatusError):
        create_item(client, "")


def test_fetch_all_items_follows_pages():
    pages = {
        "/items": {"items": [1, 2], "next": "/items?page=2"},
        "/items?page=2": {"items": [3], "next": "/items?page=3"},
        "/items?page=3": {"items": [4, 5], "next": None},
    }
    requested = []

    def handler(request):
        key = request.url.raw_path.decode()
        requested.append(key)
        return httpx.Response(200, json=pages[key])

    assert fetch_all_items(client_for(handler), "/items") == [1, 2, 3, 4, 5]
    assert requested == ["/items", "/items?page=2", "/items?page=3"]


def test_retry_recovers(monkeypatch):
    monkeypatch.setattr(time, "sleep", lambda _seconds: None)
    statuses = iter([500, 502, 200])
    calls = []

    def handler(request):
        calls.append(1)
        return httpx.Response(next(statuses), json={"ok": True})

    response = get_with_retry(client_for(handler), "/x")
    assert response.status_code == 200
    assert len(calls) == 3


def test_retry_gives_up(monkeypatch):
    monkeypatch.setattr(time, "sleep", lambda _seconds: None)
    calls = []

    def handler(request):
        calls.append(1)
        return httpx.Response(500)

    with pytest.raises(httpx.HTTPStatusError):
        get_with_retry(client_for(handler), "/x", attempts=2)
    assert len(calls) == 2


def test_retry_does_not_retry_client_errors(monkeypatch):
    monkeypatch.setattr(time, "sleep", lambda _seconds: None)
    calls = []

    def handler(request):
        calls.append(1)
        return httpx.Response(404)

    assert get_with_retry(client_for(handler), "/x").status_code == 404
    assert len(calls) == 1
