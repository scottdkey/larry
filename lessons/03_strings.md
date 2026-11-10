# Lesson 3: Strings / Lección 3: Cadenas de texto

Goals: use common string methods, slice text, and format output with f-strings.

> **ES:** Objetivos: usar métodos comunes de cadenas, cortar texto (slicing) y dar formato a la salida con f-strings.

## Strings are immutable sequences / Las cadenas son secuencias inmutables

A `str` is a sequence of characters. You can index and loop over it, but never change it in place; every "modification" returns a new string.

> **ES:** Un `str` es una secuencia de caracteres. Puedes acceder por índice y recorrerlo, pero nunca modificarlo en su lugar; cada "modificación" devuelve una cadena nueva.

```python
word = "python"
word[0]  # 'p'
word[-1]  # 'n'
len(word)  # 6
word[0] = "P"  # TypeError: strings are immutable
word.capitalize()  # 'Python' (new string; word is unchanged)
```

Quote with `'...'` or `"..."`. Triple quotes `"""..."""` span lines. Prefix `r` for raw strings (useful for Windows paths and regexes): `r"C:\new"`.

> **ES:** Usa comillas `'...'` o `"..."`. Las comillas triples `"""..."""` abarcan varias líneas. El prefijo `r` crea cadenas crudas (raw), útiles para rutas de Windows y expresiones regulares: `r"C:\new"`.

## Slicing / Slicing (cortes)

`text[start:stop:step]`, stop excluded, every part optional. Negative indexes count from the end.

> **ES:** `text[start:stop:step]`: `stop` se excluye y cada parte es opcional. Los índices negativos cuentan desde el final.

```python
s = "abcdef"
s[1:4]  # 'bcd'
s[:2]  # 'ab'
s[-2:]  # 'ef'
s[::2]  # 'ace'
s[::-1]  # 'fedcba'  (reversed)
```

Slices never raise `IndexError` for out-of-range bounds; they just clip: `"abc"[:100]` is `'abc'`.

> **ES:** Los slices nunca lanzan `IndexError` por límites fuera de rango; simplemente se recortan: `"abc"[:100]` es `'abc'`.

## Handy methods / Métodos útiles

```python
"  hi  ".strip()  # 'hi'
"Hello".lower(), "Hello".upper()
"hello world".title()  # 'Hello World'
"a,b,c".split(",")  # ['a', 'b', 'c']
"a  b\tc".split()  # ['a', 'b', 'c']  (any whitespace)
"-".join(["a", "b", "c"])  # 'a-b-c'
"hello".replace("l", "L")  # 'heLLo'
"hello".startswith("he")  # True
"hello".find("l")  # 2 (-1 if missing)
"hello".count("l")  # 2
"abc123".isalnum()  # True
"42".isdigit()  # True
"a" in "cat"  # True
```

Building a big string? Collect pieces in a list and `"".join(pieces)`; repeated `+=` in a loop is slower and noisier.

> **ES:** ¿Vas a construir una cadena grande? Junta los pedazos en una lista y usa `"".join(pieces)`; repetir `+=` en un bucle es más lento y más desordenado.

`removeprefix` and `removesuffix` strip an exact prefix or suffix. Unlike `strip("abc")`, which removes any of those *characters* from the ends.

> **ES:** `removeprefix` y `removesuffix` quitan un prefijo o sufijo exacto. A diferencia de `strip("abc")`, que quita cualquiera de esos *caracteres* de los extremos.

## f-strings

Put an expression in `{}` after an `f` prefix:

> **ES:** Pon una expresión dentro de `{}` después del prefijo `f`:

```python
name, score = "Ada", 93.456
f"{name} scored {score}"  # 'Ada scored 93.456'
f"{score:.1f}"  # '93.5'
f"{1234567:,}"  # '1,234,567'
f"{0.256:.0%}"  # '26%'
f"{name!r}"  # "'Ada'"
f"{score=}"  # 'score=93.456'  (great for debugging)
```

### Alignment and padding / Alineación y relleno

The format spec is `[fill][align][width][.precision][type]`. Align is `<` left, `>` right, `^` center.

> **ES:** La especificación de formato es `[fill][align][width][.precision][type]`. Alineación: `<` izquierda, `>` derecha, `^` centro.

```python
f"{'tea':<8}|"  # 'tea     |'
f"{2.5:>8.2f}|"  # '    2.50|'
f"{'hi':^6}|"  # '  hi  |'
f"{7:03d}"  # '007'
f"{'x':*^7}"  # '***x***'
```

The width itself can be computed with a nested field:

> **ES:** El ancho también se puede calcular con un campo anidado:

```python
width = 10
f"{'tea':<{width}}"
```

## Characters and numbers / Caracteres y números

`ord("a")` gives 97 and `chr(97)` gives `'a'`. Letters are consecutive, which makes things like shifting ciphers easy:

> **ES:** `ord("a")` da 97 y `chr(97)` da `'a'`. Las letras son consecutivas, lo que facilita cosas como los cifrados por desplazamiento:

```python
chr((ord("c") - ord("a") + 3) % 26 + ord("a"))  # 'f'
```

The `%` operator wraps around, even for negative numbers.

> **ES:** El operador `%` da la vuelta (wrap around), incluso con números negativos.

## Common gotchas / Errores comunes

- `"5" + 5` is a `TypeError`. Convert: `"5" + str(5)` or `f"5{5}"`.
- `split()` with no arguments drops empty strings; `split(" ")` does not.
- `strip()` only touches the ends, never the middle.
- `.lower()` returns a new string. Remember to use the result.
- Comparing text case-insensitively: use `.casefold()` for non-English text, `.lower()` is fine for basics.
- `str.isalnum()` is False for the empty string.

> **ES:**
> - `"5" + 5` es un `TypeError`. Convierte: `"5" + str(5)` o `f"5{5}"`.
> - `split()` sin argumentos descarta las cadenas vacías; `split(" ")` no.
> - `strip()` solo afecta los extremos, nunca el medio.
> - `.lower()` devuelve una cadena nueva. Recuerda usar el resultado.
> - Para comparar texto sin distinguir mayúsculas: usa `.casefold()` con texto que no sea inglés; `.lower()` basta para casos simples.
> - `str.isalnum()` es False para la cadena vacía.

## Exercises / Ejercicios

Stubs are in `exercises/03_strings/strings.py`.

> **ES:** Los esqueletos (stubs) están en `exercises/03_strings/strings.py`.

1. `initials`
2. `is_palindrome`
3. `truncate` (slicing)
4. `caesar` (`ord`/`chr`)
5. `format_receipt` (f-string alignment)
6. `word_wrap`

> **ES:**
> 1. `initials`
> 2. `is_palindrome`
> 3. `truncate` (slicing)
> 4. `caesar` (`ord`/`chr`)
> 5. `format_receipt` (alineación con f-strings)
> 6. `word_wrap`

Run the tests:

> **ES:** Ejecuta las pruebas:

```sh
uv run pytest exercises/03_strings
```

Reference solutions are in `solutions/03_strings/`.

> **ES:** Las soluciones de referencia están en `solutions/03_strings/`.
