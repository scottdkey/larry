"""Lesson 21: a small client for a JSON API, built on httpx."""

import httpx


def make_client(
    base_url: str, token: str, transport: httpx.BaseTransport | None = None
) -> httpx.Client:
    return httpx.Client(
        base_url=base_url,
        headers={"Authorization": f"Bearer {token}"},
        timeout=5.0,
        transport=transport,
    )


def fetch_json(client: httpx.Client, path: str) -> dict:
    response = client.get(path)
    response.raise_for_status()
    return response.json()


def get_user_name(client: httpx.Client, user_id: int) -> str | None:
    response = client.get(f"/users/{user_id}")
    if response.status_code == 404:
        return None
    response.raise_for_status()
    return response.json()["name"]


def search(client: httpx.Client, query: str, limit: int = 10) -> list[str]:
    response = client.get("/search", params={"q": query, "limit": limit})
    response.raise_for_status()
    return [item["name"] for item in response.json()["results"]]


def create_item(client: httpx.Client, name: str) -> int:
    response = client.post("/items", json={"name": name})
    response.raise_for_status()
    return response.json()["id"]


def fetch_all_items(client: httpx.Client, path: str) -> list[dict]:
    items: list[dict] = []
    next_path: str | None = path
    while next_path:
        page = fetch_json(client, next_path)
        items.extend(page["items"])
        next_path = page["next"]
    return items


def get_with_retry(
    client: httpx.Client, path: str, attempts: int = 3
) -> httpx.Response:
    for _ in range(attempts):
        response = client.get(path)
        if response.status_code < 500:
            return response
    response.raise_for_status()
    return response
