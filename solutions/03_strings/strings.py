"""Lesson 3 exercises: string methods, slicing, f-string formatting."""


def initials(name: str) -> str:
    """Return upper-case initials of each word: "ada king lovelace" -> "AKL"."""
    return "".join(word[0] for word in name.split()).upper()


def is_palindrome(text: str) -> bool:
    """True if text reads the same backwards, ignoring case and non-alphanumerics.

    "A man, a plan, a canal: Panama" -> True
    """
    cleaned = [c.lower() for c in text if c.isalnum()]
    return cleaned == cleaned[::-1]


def truncate(text: str, width: int) -> str:
    """Shorten text to at most `width` characters, ending with "..." if it was cut.

    Text that already fits is returned unchanged. Assume width >= 3.
    truncate("hello world", 8) -> "hello..."
    """
    if len(text) <= width:
        return text
    return text[: width - 3] + "..."


def caesar(text: str, shift: int) -> str:
    """Shift ASCII letters by `shift` (wrapping, case kept); leave others alone."""
    out = []
    for c in text:
        if "a" <= c <= "z":
            out.append(chr((ord(c) - ord("a") + shift) % 26 + ord("a")))
        elif "A" <= c <= "Z":
            out.append(chr((ord(c) - ord("A") + shift) % 26 + ord("A")))
        else:
            out.append(c)
    return "".join(out)


def format_receipt(items: list[tuple[str, float]], width: int = 20) -> str:
    """Build a receipt, one line per item plus a total line, joined by newlines.

    Each line is the name left-aligned and the price right-aligned with 2 decimals,
    the whole line `width` characters wide (price field is 8 wide).
    The last line is "TOTAL" with the sum.
    format_receipt([("tea", 2.5)], width=13) -> "tea      2.50\nTOTAL    2.50"
    """
    rows = [*items, ("TOTAL", sum(price for _, price in items))]
    return "\n".join(f"{name:<{width - 8}}{price:>8.2f}" for name, price in rows)


def word_wrap(text: str, width: int) -> list[str]:
    """Greedily wrap text into lines of at most `width` characters, breaking on spaces.

    Words longer than `width` get their own line unbroken.
    """
    lines: list[str] = []
    current = ""
    for word in text.split():
        if current and len(current) + 1 + len(word) <= width:
            current += " " + word
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines
