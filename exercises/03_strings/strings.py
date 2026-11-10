"""Lesson 3 exercises: string methods, slicing, f-string formatting."""


def initials(name: str) -> str:
    """Return upper-case initials of each word: "ada king lovelace" -> "AKL".

    ES: Devuelve las iniciales en mayúscula de cada palabra.
    """
    raise NotImplementedError


def is_palindrome(text: str) -> bool:
    """True if text reads the same backwards, ignoring case and non-alphanumerics.

    "A man, a plan, a canal: Panama" -> True

    ES: True si el texto se lee igual al revés, ignorando mayúsculas y
    caracteres no alfanuméricos.
    """
    raise NotImplementedError


def truncate(text: str, width: int) -> str:
    """Shorten text to at most `width` characters, ending with "..." if it was cut.

    Text that already fits is returned unchanged. Assume width >= 3.

    ES: Acorta el texto a `width` caracteres como máximo, terminando en "..."
    si se cortó. Si ya cabe, se devuelve igual.
    truncate("hello world", 8) -> "hello..."
    """
    raise NotImplementedError


def caesar(text: str, shift: int) -> str:
    """Shift ASCII letters by `shift` (wrapping, case kept); leave others alone.

    ES: Desplaza las letras ASCII `shift` posiciones (con vuelta, conserva mayúsculas).
    """
    raise NotImplementedError


def format_receipt(items: list[tuple[str, float]], width: int = 20) -> str:
    """Build a receipt, one line per item plus a total line, joined by newlines.

    Each line is the name left-aligned and the price right-aligned with 2 decimals,
    the whole line `width` characters wide (price field is 8 wide).
    The last line is "TOTAL" with the sum.

    ES: Arma un recibo: nombre a la izquierda y precio a la derecha (2 decimales),
    cada línea de `width` caracteres (campo de precio de 8). La última es "TOTAL".
    format_receipt([("tea", 2.5)], width=13) -> "tea      2.50\nTOTAL    2.50"
    """
    raise NotImplementedError


def word_wrap(text: str, width: int) -> list[str]:
    """Greedily wrap text into lines of at most `width` characters, breaking on spaces.

    Words longer than `width` get their own line unbroken.

    ES: Ajusta el texto en líneas de máximo `width` caracteres, cortando en espacios.
    Las palabras más largas que `width` van solas en su línea, sin partir.
    """
    raise NotImplementedError
