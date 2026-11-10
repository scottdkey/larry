# Lesson 18: JSON and CSV / Lección 18: JSON y CSV

Goals: read and write the two most common data file formats, and understand
*round trips* (write data out, read it back, get the same thing).

> **ES:** Objetivos: leer y escribir los dos formatos de archivo de datos más comunes, y entender los *round trips* (viajes de ida y vuelta: escribes datos, los lees de nuevo y obtienes lo mismo).

## JSON in four functions / JSON en cuatro funciones

```python
import json

data = {"name": "Ada", "langs": ["python", "c"], "active": True, "boss": None}

text = json.dumps(data)  # Python -> str
back = json.loads(text)  # str -> Python
assert back == data

json.dumps(data, indent=2, sort_keys=True)  # pretty and stable
```

The "s" means *string*. Without it, the functions work with open files:
`json.dump(data, f)` and `json.load(f)`. With pathlib it is usually simpler to
use strings:

> **ES:** La "s" significa *string* (cadena). Sin ella, las funciones trabajan con archivos abiertos: `json.dump(data, f)` y `json.load(f)`. Con pathlib suele ser más simple usar cadenas:

```python
from pathlib import Path

path = Path("data.json")
path.write_text(json.dumps(data, indent=2))
data = json.loads(path.read_text())
```

### Type mapping / Mapeo de tipos

| Python | JSON |
|---|---|
| dict | object |
| list, tuple | array |
| str | string |
| int, float | number |
| True / False / None | true / false / null |

> **ES:**
>
> | Python | JSON |
> |---|---|
> | dict | objeto |
> | list, tuple | arreglo |
> | str | cadena |
> | int, float | número |
> | True / False / None | true / false / null |

Gotchas:

> **ES:** Trampas comunes:

- Tuples come back as lists. Sets, dates, `Path`, and dataclasses are not
  supported; `dumps` raises `TypeError`.
- Dict keys become strings: `{1: "a"}` returns as `{"1": "a"}`.
- Invalid input raises `json.JSONDecodeError`, a subclass of `ValueError`.

> **ES:**
>
> - Los tuples regresan como lists. Los sets, las fechas, `Path` y las dataclasses no son compatibles; `dumps` lanza `TypeError`.
> - Las claves de un dict se vuelven cadenas: `{1: "a"}` regresa como `{"1": "a"}`.
> - La entrada inválida lanza `json.JSONDecodeError`, una subclase de `ValueError`.

### Handling types JSON does not know / Manejar tipos que JSON no conoce

Convert them yourself on the way out and back in:

> **ES:** Conviértelos tú mismo al salir y al volver a entrar:

```python
from datetime import date

event = {"name": "launch", "when": date(2024, 3, 5)}
text = json.dumps({**event, "when": event["when"].isoformat()})

raw = json.loads(text)
raw["when"] = date.fromisoformat(raw["when"])
```

ISO 8601 strings (`2024-03-05`) are the standard way to store dates. For
dataclasses, `dataclasses.asdict(obj)` gives a plain dict first.

> **ES:** Las cadenas ISO 8601 (`2024-03-05`) son la forma estándar de guardar fechas. Para las dataclasses, `dataclasses.asdict(obj)` te da primero un dict simple.

## CSV with the csv module / CSV con el módulo csv

CSV looks simple until a field contains a comma, a quote, or a newline. Do not
use `line.split(",")`; use the csv module.

> **ES:** CSV parece simple hasta que un campo contiene una coma, una comilla o un salto de línea. No uses `line.split(",")`; usa el módulo csv.

```python
import csv
import io

text = 'name,note\nAda,"likes ""python"", c"\n'
for row in csv.DictReader(io.StringIO(text)):
    print(row["name"], row["note"])
```

`DictReader` uses the header line for keys. **Every value is a string**, so
convert numbers yourself (`int(row["age"])`).

> **ES:** `DictReader` usa la línea de encabezado como claves. **Todos los valores son cadenas**, así que convierte los números tú mismo (`int(row["age"])`).

Writing:

> **ES:** Escritura:

```python
out = io.StringIO()
writer = csv.DictWriter(out, fieldnames=["name", "age"], lineterminator="\n")
writer.writeheader()
writer.writerow({"name": "Smith, J", "age": 5})
print(out.getvalue())
```

The writer adds quotes only where needed. With real files, open with
`newline=""` and an explicit encoding, otherwise Windows may double the line
endings:

> **ES:** El writer agrega comillas solo donde hacen falta. Con archivos reales, ábrelos con `newline=""` y una codificación explícita; de lo contrario Windows puede duplicar los saltos de línea:

```python
with open("people.csv", "w", newline="", encoding="utf-8") as f:
    ...
```

`io.StringIO` is a file-like object in memory. It makes CSV code easy to test
without touching disk.

> **ES:** `io.StringIO` es un objeto tipo archivo en memoria. Facilita probar código CSV sin tocar el disco.

## Round trips as a test / Round trips como prueba

A reliable test for serialization code is `decode(encode(x)) == x`. Include
awkward values: commas, quotes, newlines, empty strings, unicode.

> **ES:** Una prueba confiable para código de serialización es `decode(encode(x)) == x`. Incluye valores incómodos: comas, comillas, saltos de línea, cadenas vacías, unicode.

## Gotchas / Trampas comunes

- CSV has no types; `"007"` becomes `7` if you convert, losing the zeros.
- `json.dumps` of floats like `nan` produces non-standard JSON.
- Reading a missing file raises `FileNotFoundError`; decide whether that means
  "use defaults" or "report an error".
- Do not build JSON or CSV with f-strings; escaping is easy to get wrong.

> **ES:**
>
> - CSV no tiene tipos; `"007"` se vuelve `7` si lo conviertes, perdiendo los ceros.
> - `json.dumps` de flotantes como `nan` produce JSON no estándar.
> - Leer un archivo inexistente lanza `FileNotFoundError`; decide si eso significa "usar valores por defecto" o "reportar un error".
> - No construyas JSON ni CSV con f-strings; es fácil equivocarse con el escape.

## Exercises / Ejercicios

Files:

> **ES:** Archivos:

- `exercises/18_json_csv/data_formats.py` — implement the stubs
- `exercises/18_json_csv/test_data_formats.py` — the tests
- Reference: `solutions/18_json_csv/data_formats.py`

> **ES:**
>
> - `exercises/18_json_csv/data_formats.py` — implementa los stubs
> - `exercises/18_json_csv/test_data_formats.py` — las pruebas
> - Referencia: `solutions/18_json_csv/data_formats.py`

Run: `uv run pytest exercises/18_json_csv`

> **ES:** Ejecuta: `uv run pytest exercises/18_json_csv`
