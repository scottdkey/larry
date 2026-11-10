"""Lesson 21: a small client for a JSON API, built on httpx.

ES: Lección 21: un pequeño cliente para una API JSON, construido con httpx.
"""

import httpx


def make_client(
    base_url: str, token: str, transport: httpx.BaseTransport | None = None
) -> httpx.Client:
    """Build an httpx.Client with the given base_url, an
    'Authorization: Bearer <token>' header, and a 5 second timeout.
    `transport` is passed through (tests inject a MockTransport).

    ES: Construye un httpx.Client con base_url, el header 'Authorization:
    Bearer <token>' y timeout de 5 segundos. `transport` se pasa tal cual (las
    pruebas inyectan un MockTransport).
    """
    raise NotImplementedError


def fetch_json(client: httpx.Client, path: str) -> dict:
    """GET path and return the decoded JSON body.
    Raise httpx.HTTPStatusError for 4xx/5xx responses.

    ES: Hace GET a path y devuelve el cuerpo JSON decodificado. Lanza
    httpx.HTTPStatusError en respuestas 4xx/5xx.
    """
    raise NotImplementedError


def get_user_name(client: httpx.Client, user_id: int) -> str | None:
    """GET /users/<id> and return the 'name' field, or None on 404.
    Other error statuses raise httpx.HTTPStatusError.

    ES: Hace GET a /users/<id> y devuelve el campo 'name', o None si es 404.
    Otros estados de error lanzan httpx.HTTPStatusError.
    """
    raise NotImplementedError


def search(client: httpx.Client, query: str, limit: int = 10) -> list[str]:
    """GET /search with query parameters q=<query> and limit=<limit> (let
    httpx encode them). The body is {"results": [{"name": ...}, ...]};
    return the names.

    ES: GET /search con parámetros q=<query> y limit=<limit> (deja que httpx los
    codifique). El cuerpo es {"results": [{"name": ...}, ...]}; devuelve los
    nombres.
    """
    raise NotImplementedError


def create_item(client: httpx.Client, name: str) -> int:
    """POST /items with JSON body {"name": name}. The server answers 201 with
    {"id": <int>}; return the id. Raise on any other error status.

    ES: POST /items con cuerpo JSON {"name": name}. El servidor responde 201 con
    {"id": <int>}; devuelve el id. Lanza error en cualquier otro estado.
    """
    raise NotImplementedError


def fetch_all_items(client: httpx.Client, path: str) -> list[dict]:
    """Collect items across pages. Each page is
    {"items": [...], "next": "<path or null>"}; follow `next` until null.

    ES: Reúne elementos de varias páginas. Cada página es {"items": [...],
    "next": "<ruta o null>"}; sigue `next` hasta que sea null.
    """
    raise NotImplementedError


def get_with_retry(
    client: httpx.Client, path: str, attempts: int = 3
) -> httpx.Response:
    """GET path, retrying up to `attempts` times total while the status is
    5xx. Return the first non-5xx response; if every attempt is 5xx, raise
    httpx.HTTPStatusError. Do not sleep (keep it simple and fast).

    ES: GET a path, reintentando hasta `attempts` veces en total mientras el
    estado sea 5xx. Devuelve la primera respuesta no 5xx; si todos los intentos
    son 5xx, lanza httpx.HTTPStatusError. No uses sleep (simple y rápido).
    """
    raise NotImplementedError
