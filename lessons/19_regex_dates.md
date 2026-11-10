# Lesson 19: Regular expressions and dates / Lección 19: Expresiones regulares y fechas

Goals: find patterns in text with `re`, and work with dates, times, and time
zones using `datetime`, `zoneinfo`, and `timedelta`.

> **ES:** Objetivos: encontrar patrones en texto con `re`, y trabajar con fechas, horas y zonas horarias usando `datetime`, `zoneinfo` y `timedelta`.

## Regular expressions / Expresiones regulares

A regex describes a pattern. Always write it as a raw string (`r"..."`) so
backslashes reach the regex engine untouched.

> **ES:** Una regex describe un patrón. Escríbela siempre como raw string (`r"..."`) para que las barras invertidas lleguen intactas al motor de regex.

```python
import re

text = "Order 66 shipped on 2024-03-05, order 7 pending."

re.findall(r"\d+", text)  # ['66', '2024', '03', '05', '7']
re.search(r"order (\d+)", text, re.IGNORECASE).group(1)  # '66'
re.sub(r"\d", "#", "a1b22")  # 'a#b##'
```

### The pieces / Las piezas

| Pattern | Meaning |
|---|---|
| `\d` `\w` `\s` | digit, word character, whitespace |
| `.` | any character except newline |
| `[a-z0-9]` | one of a set; `[^...]` is "not these" |
| `*` `+` `?` | 0 or more, 1 or more, 0 or 1 |
| `{4}` `{2,3}` | exact or ranged repeat |
| `^` `$` | start / end of string |
| `(...)` | capture group; `(?:...)` groups without capturing |
| `a\|b` | a or b |

> **ES:**
>
> | Patrón | Significado |
> |---|---|
> | `\d` `\w` `\s` | dígito, carácter de palabra, espacio en blanco |
> | `.` | cualquier carácter excepto salto de línea |
> | `[a-z0-9]` | uno de un conjunto; `[^...]` significa "ninguno de estos" |
> | `*` `+` `?` | 0 o más, 1 o más, 0 o 1 |
> | `{4}` `{2,3}` | repetición exacta o con rango |
> | `^` `$` | inicio / fin de la cadena |
> | `(...)` | grupo de captura; `(?:...)` agrupa sin capturar |
> | `a\|b` | a o b |

### match, search, fullmatch, findall / match, search, fullmatch, findall

- `re.search` finds the pattern anywhere; returns a match or `None`.
- `re.match` anchors at the start; `re.fullmatch` must cover the whole string.
- `re.findall` returns all matches (strings, or tuples if there are groups).
- `re.finditer` yields match objects.

> **ES:**
>
> - `re.search` encuentra el patrón en cualquier parte; devuelve un match o `None`.
> - `re.match` ancla al inicio; `re.fullmatch` debe cubrir toda la cadena.
> - `re.findall` devuelve todas las coincidencias (cadenas, o tuplas si hay grupos).
> - `re.finditer` produce objetos match.

Always check for `None` before using a match:

> **ES:** Verifica siempre que no sea `None` antes de usar un match:

```python
if m := re.search(r"(\d+)-(\d+)", "pages 3-9"):
    start, end = m.groups()
```

### Named groups and compiling / Grupos con nombre y compilación

```python
LOG = re.compile(r"(?P<level>[A-Z]+): (?P<msg>.*)")
m = LOG.fullmatch("ERROR: disk full")
m.groupdict()  # {'level': 'ERROR', 'msg': 'disk full'}
```

Compile patterns once at module level when you use them repeatedly.

> **ES:** Compila los patrones una sola vez a nivel de módulo cuando los uses repetidamente.

### Gotchas / Errores comunes

- `.*` is greedy; `.*?` is lazy (stops as early as possible).
- Regexes cannot validate everything (real email rules, HTML). Keep them
  simple and be honest about what they accept.
- `re.match` does not mean "matches the whole string"; use `fullmatch`.
- Do not use regex when `str.split`, `startswith`, or `in` will do.

> **ES:**
>
> - `.*` es codicioso (greedy); `.*?` es perezoso (se detiene lo antes posible).
> - Las regex no pueden validar todo (reglas reales de email, HTML). Mantenlas simples y sé honesto sobre lo que aceptan.
> - `re.match` no significa "coincide con toda la cadena"; usa `fullmatch`.
> - No uses regex cuando `str.split`, `startswith` o `in` bastan.

## Dates and times / Fechas y horas

```python
from datetime import date, datetime, timedelta

d = date(2024, 3, 5)
d.isoformat()  # '2024-03-05'
date.fromisoformat("2024-03-05")  # parse
d + timedelta(days=30)  # date arithmetic
(date(2024, 12, 25) - d).days  # difference is a timedelta

now = datetime.now()
f"{now:%Y-%m-%d %H:%M}"  # formatting codes
datetime.strptime("05/03/2024", "%d/%m/%Y")  # parse custom formats
```

`timedelta` holds a duration: `timedelta(hours=2, minutes=30)`. Use
`.total_seconds()` for a single number; `.days` is only the whole-day part.

> **ES:** `timedelta` guarda una duración: `timedelta(hours=2, minutes=30)`. Usa `.total_seconds()` para obtener un solo número; `.days` es solo la parte de días completos.

### Naive vs aware / Naive vs aware

A *naive* datetime has no time zone; it is ambiguous. An *aware* one knows its
offset. Mixing them raises `TypeError`. Prefer aware datetimes, and store
times in UTC.

> **ES:** Un datetime *naive* (ingenuo) no tiene zona horaria; es ambiguo. Uno *aware* (consciente) conoce su desfase (offset). Mezclarlos lanza `TypeError`. Prefiere datetimes aware y guarda las horas en UTC.

```python
from datetime import UTC
from zoneinfo import ZoneInfo

now_utc = datetime.now(UTC)
meeting = datetime(2024, 7, 15, 9, 0, tzinfo=ZoneInfo("America/New_York"))
meeting.astimezone(ZoneInfo("Europe/Paris"))  # 15:00+02:00
```

Use IANA names (`"America/New_York"`), not fixed offsets, so daylight saving
is handled for you. Do not use `.replace(tzinfo=...)` to *convert*; it only
attaches a zone to a naive value (right for interpreting local time, wrong for
moving between zones; use `astimezone`).

> **ES:** Usa nombres IANA (`"America/New_York"`), no desfases fijos, para que el horario de verano se maneje solo. No uses `.replace(tzinfo=...)` para *convertir*; solo asigna una zona a un valor naive (correcto para interpretar hora local, incorrecto para pasar de una zona a otra; usa `astimezone`).

### Gotchas / Errores comunes

- Month and day order: `%m` is month, `%M` is minutes.
- Age and "months between" are not simple subtraction; compare (month, day).
- Tests that call `datetime.now()` are non-deterministic. Pass the date in as
  an argument instead.
- On Windows, zoneinfo needs the `tzdata` package.

> **ES:**
>
> - Orden de mes y día: `%m` es mes, `%M` es minutos.
> - La edad y los "meses entre" no son una resta simple; compara (mes, día).
> - Las pruebas que llaman a `datetime.now()` no son deterministas. Pasa la fecha como argumento.
> - En Windows, zoneinfo necesita el paquete `tzdata`.

## Exercises / Ejercicios

Files:

> **ES:** Archivos:

- `exercises/19_regex_dates/text_and_time.py` — implement the stubs
- `exercises/19_regex_dates/test_text_and_time.py` — the tests
- Reference: `solutions/19_regex_dates/text_and_time.py`

> **ES:**
>
> - `exercises/19_regex_dates/text_and_time.py` — implementa los stubs
> - `exercises/19_regex_dates/test_text_and_time.py` — las pruebas
> - Referencia: `solutions/19_regex_dates/text_and_time.py`

Run: `uv run pytest exercises/19_regex_dates`

> **ES:** Ejecuta: `uv run pytest exercises/19_regex_dates`
