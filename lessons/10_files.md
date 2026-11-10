# Lesson 10: Files / Lección 10: Archivos

Goals: use `pathlib` for paths, read and write text, handle JSON, and test
file code safely with `tmp_path`.

> **ES:** Objetivos: usar `pathlib` para las rutas, leer y escribir texto,
> manejar JSON y probar código de archivos de forma segura con `tmp_path`.

## pathlib

`Path` objects replace string juggling with `os.path`:

> **ES:** Los objetos `Path` reemplazan el malabarismo de cadenas con
> `os.path`:

```python
from pathlib import Path

root = Path("data")
note = root / "notes" / "today.txt"  # `/` joins paths
note.name  # "today.txt"
note.stem  # "today"
note.suffix  # ".txt"
note.parent  # Path("data/notes")
note.exists(), note.is_file(), note.is_dir()
Path.home(), Path.cwd()
```

## Reading and writing text / Leer y escribir texto

For small files, one call does it:

> **ES:** Para archivos pequeños, basta una sola llamada:

```python
note.parent.mkdir(parents=True, exist_ok=True)
note.write_text("hello\nworld\n", encoding="utf-8")
text = note.read_text(encoding="utf-8")
lines = text.splitlines()  # ["hello", "world"]
```

Always pass `encoding="utf-8"`; the platform default differs between machines.

> **ES:** Pasa siempre `encoding="utf-8"`; el valor por defecto de la
> plataforma cambia de una máquina a otra.

For appending or big files, use `open` in a `with` block, which closes the
file even if an error occurs:

> **ES:** Para agregar al final o para archivos grandes, usa `open` dentro de
> un bloque `with`, que cierra el archivo incluso si ocurre un error:

```python
with note.open("a", encoding="utf-8") as f:
    f.write("another line\n")

with note.open(encoding="utf-8") as f:
    for line in f:  # one line at a time, constant memory
        print(line.rstrip("\n"))
```

Modes: `"r"` read (default), `"w"` overwrite (truncates!), `"a"` append.

> **ES:** Modos: `"r"` lectura (por defecto), `"w"` sobrescribir (¡trunca el
> archivo!), `"a"` agregar al final (append).

## Finding files / Buscar archivos

```python
list(root.iterdir())  # direct children
sorted(root.glob("*.txt"))  # this directory only
sorted(root.rglob("*.txt"))  # recursive
```

Order is not guaranteed, so `sorted` when it matters.

> **ES:** El orden no está garantizado, así que usa `sorted` cuando importe.

## JSON

```python
import json

path.write_text(json.dumps({"a": 1}, indent=2), encoding="utf-8")
data = json.loads(path.read_text(encoding="utf-8"))
```

## Testing with tmp_path / Pruebas con tmp_path

pytest gives every test a fresh, empty temporary directory via the `tmp_path`
fixture (a `Path`). Never test against real files in your home directory.

> **ES:** pytest le da a cada prueba un directorio temporal nuevo y vacío
> mediante el fixture `tmp_path` (un `Path`). Nunca pruebes con archivos reales
> de tu directorio personal.

```python
def test_roundtrip(tmp_path):
    p = tmp_path / "x.txt"
    p.write_text("hi\n", encoding="utf-8")
    assert p.read_text(encoding="utf-8") == "hi\n"
```

## Gotchas / Trampas comunes

- `"w"` erases the file immediately, even if your code then fails.
- `read_text()` loads everything; iterate the file for large inputs.
- `rglob("*.txt")` also matches *directories* named `x.txt`; check `is_file()`.
- Windows uses `\`; building paths with `/` on `Path` keeps your code portable.
- Reading a missing file raises `FileNotFoundError` (see lesson 11).

> **ES:**
> - `"w"` borra el archivo de inmediato, incluso si tu código falla después.
> - `read_text()` lo carga todo; itera el archivo cuando la entrada es grande.
> - `rglob("*.txt")` también coincide con *directorios* llamados `x.txt`;
>   verifica con `is_file()`.
> - Windows usa `\`; construir rutas con `/` en `Path` mantiene tu código
>   portable.
> - Leer un archivo que no existe lanza `FileNotFoundError` (ver lección 11).

## Exercises / Ejercicios

Stubs are in `exercises/10_files/files.py`; tests in `test_files.py` use
`tmp_path`.

> **ES:** Los stubs están en `exercises/10_files/files.py`; las pruebas en
> `test_files.py` usan `tmp_path`.

```
uv run pytest exercises/10_files
```
