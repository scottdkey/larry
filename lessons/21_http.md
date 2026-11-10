# Lesson 21: HTTP with httpx / Lección 21: HTTP con httpx

Goals: call web APIs with `httpx`, handle errors, and test HTTP code without
ever touching the network.

> **ES:** Objetivos: llamar APIs web con `httpx`, manejar errores y probar código HTTP sin tocar nunca la red.

## A first request / Una primera petición

```python
import httpx

response = httpx.get("https://api.github.com/zen", timeout=5.0)
response.raise_for_status()
print(response.status_code, response.text)
```

A response has `.status_code`, `.headers`, `.text`, `.content` (bytes), and
`.json()` (decoded body). `raise_for_status()` raises
`httpx.HTTPStatusError` for 4xx and 5xx; without it, an error page is just
another response that you might accidentally treat as data.

> **ES:** Una respuesta tiene `.status_code`, `.headers`, `.text`, `.content` (bytes) y `.json()` (el cuerpo decodificado). `raise_for_status()` lanza `httpx.HTTPStatusError` para 4xx y 5xx; sin él, una página de error es simplemente otra respuesta que podrías tratar por accidente como datos.

Always set a timeout. A server that never answers will otherwise hang your
program (httpx defaults to 5 seconds, but be explicit in real code).

> **ES:** Siempre define un timeout. Un servidor que nunca responde dejará tu programa colgado (httpx usa 5 segundos por defecto, pero sé explícito en código real).

## Use a Client / Usa un Client

For more than one request, create a `Client`. It reuses connections and holds
shared settings:

> **ES:** Para más de una petición, crea un `Client`. Reutiliza conexiones y guarda configuración compartida:

```python
with httpx.Client(
    base_url="https://api.example.com",
    headers={"Authorization": "Bearer TOKEN"},
    timeout=5.0,
) as client:
    me = client.get("/me").json()
    client.post("/items", json={"name": "widget"})
```

With `base_url`, requests use relative paths like `"/me"`.

> **ES:** Con `base_url`, las peticiones usan rutas relativas como `"/me"`.

## Query parameters and bodies / Parámetros de consulta y cuerpos

```python
client.get("/search", params={"q": "a b&c", "limit": 3})
# -> /search?q=a+b%26c&limit=3   (httpx encodes for you)

client.post("/items", json={"name": "x"})  # JSON body + content-type
client.post("/form", data={"user": "ada"})  # form-encoded body
```

Never glue query strings together by hand; special characters will break.

> **ES:** Nunca pegues cadenas de consulta a mano; los caracteres especiales las romperán.

## Errors / Errores

Two kinds of failure:

> **ES:** Dos tipos de fallo:

1. The server answered with an error status: `HTTPStatusError`, only raised
   by `raise_for_status()`.
2. The request never completed (DNS failure, refused connection, timeout):
   `httpx.RequestError` and subclasses such as `httpx.TimeoutException`.

> **ES:**
>
> 1. El servidor respondió con un estado de error: `HTTPStatusError`, que solo lanza `raise_for_status()`.
> 2. La petición nunca se completó (fallo de DNS, conexión rechazada, timeout): `httpx.RequestError` y sus subclases como `httpx.TimeoutException`.

Decide per status what is *normal*. A `404` from "get user" often means "no
such user" and should become `None`, while `500` is a real problem.

> **ES:** Decide por cada estado qué es *normal*. Un `404` de "obtener usuario" suele significar "no existe ese usuario" y debería convertirse en `None`, mientras que un `500` es un problema real.

Retrying is reasonable for 5xx and timeouts, not for 4xx (the request itself
is wrong). Real code adds a delay that grows between attempts (backoff).

> **ES:** Reintentar es razonable para 5xx y timeouts, no para 4xx (la petición misma está mal). El código real agrega una espera que crece entre intentos (backoff).

## Testing without the network / Probar sin la red

Tests that hit real servers are slow, flaky, and can break when you are
offline. `httpx.MockTransport` takes a function that turns a request into a
response, so your code runs normally but the "server" is in your test:

> **ES:** Las pruebas que llaman a servidores reales son lentas, inestables y pueden fallar cuando no tienes conexión. `httpx.MockTransport` recibe una función que convierte una petición en una respuesta, así tu código se ejecuta normalmente pero el "servidor" vive en tu prueba:

```python
import httpx


def handler(request: httpx.Request) -> httpx.Response:
    assert request.url.path == "/users/7"
    return httpx.Response(200, json={"name": "Ada"})


client = httpx.Client(
    base_url="https://api.test", transport=httpx.MockTransport(handler)
)
assert client.get("/users/7").json() == {"name": "Ada"}
```

Make your code testable by *accepting a client as an argument* rather than
creating one inside each function. The handler can also check what your
code sent (headers, query params, JSON body) and count calls:

> **ES:** Haz tu código fácil de probar *aceptando un client como argumento* en lugar de crear uno dentro de cada función. El handler también puede verificar lo que envió tu código (headers, parámetros de consulta, cuerpo JSON) y contar las llamadas:

```python
request.url.params["q"]  # query parameters
request.headers["Authorization"]
json.loads(request.content)  # the body you posted
```

To simulate a flaky server, return different responses on each call (an
iterator of status codes works well).

> **ES:** Para simular un servidor inestable, devuelve respuestas distintas en cada llamada (un iterador de códigos de estado funciona bien).

## Gotchas / Errores comunes

- `response.json()` raises if the body is not JSON; check the status first.
- `client.get("/x")` with a leading slash and a `base_url` that has a path
  component can behave surprisingly; test your URLs.
- Never commit tokens. Read them from environment variables.
- `httpx.Client` should be closed (`with` block or `.close()`).
- Never make real network calls in tests in this course.

> **ES:**
>
> - `response.json()` lanza un error si el cuerpo no es JSON; verifica primero el estado.
> - `client.get("/x")` con una barra inicial y un `base_url` que tiene componente de ruta puede comportarse de forma sorprendente; prueba tus URLs.
> - Nunca subas tokens al repositorio. Léelos de variables de entorno.
> - `httpx.Client` debe cerrarse (bloque `with` o `.close()`).
> - Nunca hagas llamadas reales a la red en las pruebas de este curso.

## Exercises / Ejercicios

Files:

> **ES:** Archivos:

- `exercises/21_http/api_client.py` — implement the stubs
- `exercises/21_http/test_api_client.py` — the tests (read how handlers are used)
- Reference: `solutions/21_http/api_client.py`

> **ES:**
>
> - `exercises/21_http/api_client.py` — implementa los stubs
> - `exercises/21_http/test_api_client.py` — las pruebas (lee cómo se usan los handlers)
> - Referencia: `solutions/21_http/api_client.py`

Run: `uv run pytest exercises/21_http`

> **ES:** Ejecuta: `uv run pytest exercises/21_http`
