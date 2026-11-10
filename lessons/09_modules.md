# Lesson 9: Modules and the Standard Library / Lección 9: Módulos y la biblioteca estándar

Goals: import code, understand packages, write scripts that are also
importable, and tour a few batteries-included modules.

> **ES:** Objetivos: importar código, entender los paquetes, escribir scripts
> que también se puedan importar y recorrer algunos módulos de la biblioteca
> estándar ("baterías incluidas").

## Modules and imports / Módulos e importaciones

Any `.py` file is a module. Its name is the filename without `.py`.

> **ES:** Cualquier archivo `.py` es un módulo. Su nombre es el nombre del
> archivo sin `.py`.

```python
import math
from pathlib import Path
from collections import Counter as Count  # rename on import

math.sqrt(16)
```

Prefer `import x` or `from x import name` over `from x import *`, which
hides where names come from.

> **ES:** Prefiere `import x` o `from x import name` en lugar de
> `from x import *`, que oculta de dónde vienen los nombres.

Python looks for modules in `sys.path`: the script's directory first, then
installed packages. A module is executed once, then cached in `sys.modules`.

> **ES:** Python busca módulos en `sys.path`: primero el directorio del script
> y luego los paquetes instalados. Un módulo se ejecuta una sola vez y después
> queda en caché en `sys.modules`.

## Packages / Paquetes

A directory of modules is a *package*:

> **ES:** Un directorio de módulos es un *paquete*:

```
shop/
    __init__.py      # may be empty
    cart.py
    pricing.py
```

```python
from shop.cart import Cart
from . import pricing  # relative import, only inside the package
```

Avoid naming your own file after a stdlib module (`random.py`, `json.py`):
it will shadow the real one.

> **ES:** Evita nombrar tu propio archivo como un módulo de la biblioteca
> estándar (`random.py`, `json.py`): ocultará al verdadero.

## `if __name__ == "__main__"`

When a file is run directly, Python sets `__name__` to `"__main__"`. When it
is imported, `__name__` is the module's name. Use that to keep side effects
out of imports:

> **ES:** Cuando un archivo se ejecuta directamente, Python asigna
> `"__main__"` a `__name__`. Cuando se importa, `__name__` es el nombre del
> módulo. Aprovecha eso para mantener los efectos secundarios fuera de las
> importaciones:

```python
import sys


def main(argv: list[str]) -> int:
    print(f"hello {' '.join(argv)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
```

Now `uv run python hello.py world` runs it, while `import hello` in a test
does not. Keeping logic in `main(argv)` makes it easy to test.

> **ES:** Ahora `uv run python hello.py world` lo ejecuta, mientras que
> `import hello` en una prueba no. Mantener la lógica en `main(argv)` facilita
> probarla.

## A stdlib tour / Un recorrido por la stdlib

```python
from datetime import date

(date(2024, 3, 1) - date(2024, 1, 1)).days  # 60
date.fromisoformat("2024-01-31")

from collections import Counter

Counter("banana").most_common(1)  # [("a", 3)]

import re

re.findall(r"\d+", "a1b22")  # ["1", "22"]

import json

json.dumps({"b": 1, "a": 2}, sort_keys=True)

import importlib

importlib.import_module("math")  # import by string name
```

Others worth knowing: `pathlib`, `itertools`, `functools`, `dataclasses`,
`argparse`, `logging`, `random`, `statistics`, `textwrap`, `enum`.
Browse the docs index before you reach for a third-party package.

> **ES:** Otros que vale la pena conocer: `pathlib`, `itertools`, `functools`,
> `dataclasses`, `argparse`, `logging`, `random`, `statistics`, `textwrap`,
> `enum`. Revisa el índice de la documentación antes de recurrir a un paquete
> de terceros.

## Gotchas / Trampas comunes

- Circular imports (`a` imports `b` imports `a`) fail confusingly; move
  shared code into a third module.
- Imports at the top of the file, grouped stdlib / third-party / local;
  `ruff` can sort them for you.
- `import x` inside a function works but is usually a smell.
- Mutable module-level state is shared by everyone who imports the module.

> **ES:**
> - Las importaciones circulares (`a` importa `b` que importa `a`) fallan de
>   forma confusa; mueve el código compartido a un tercer módulo.
> - Las importaciones van al inicio del archivo, agrupadas en stdlib /
>   terceros / locales; `ruff` puede ordenarlas por ti.
> - `import x` dentro de una función funciona, pero suele ser mala señal.
> - El estado mutable a nivel de módulo es compartido por todos los que
>   importan ese módulo.

## Exercises / Ejercicios

This lesson uses a single module: `exercises/09_modules/modules.py`.
Implement the functions, and add an `if __name__ == "__main__":` block at the
bottom; one test runs the file as a real script. Tests are in
`test_modules.py`.

> **ES:** Esta lección usa un solo módulo: `exercises/09_modules/modules.py`.
> Implementa las funciones y agrega un bloque `if __name__ == "__main__":` al
> final; una prueba ejecuta el archivo como un script real. Las pruebas están
> en `test_modules.py`.

```
uv run pytest exercises/09_modules
```
