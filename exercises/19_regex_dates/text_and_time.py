"""Lesson 19: regular expressions and dates.

ES: Lección 19: expresiones regulares y fechas.
"""

from datetime import date, timedelta


def extract_emails(text: str) -> list[str]:
    """Return all email addresses in text, in order.

    An address is word characters, dots, '+' or '-' before '@', then a domain
    with at least one dot: "ada@example.com", "a.b+c@mail.co.uk".

    ES: Devuelve todas las direcciones de email del texto, en orden. Una
    dirección son caracteres de palabra, puntos, '+' o '-' antes de '@', y luego
    un dominio con al menos un punto.
    """
    raise NotImplementedError


def parse_log_line(line: str) -> dict[str, str] | None:
    """Parse '2024-03-05 14:22:01 ERROR Disk full' into
    {"date": "2024-03-05", "time": "14:22:01", "level": "ERROR",
    "message": "Disk full"}. Levels are upper-case letters.
    Return None if the line does not match.

    ES: Analiza la línea de log en un dict con date, time, level y message. Los
    niveles son letras mayúsculas. Devuelve None si la línea no coincide.
    """
    raise NotImplementedError


def days_between(start: str, end: str) -> int:
    """Number of days from start to end, both ISO dates ('2024-03-05').
    Negative if end is before start.

    ES: Número de días de start a end, ambas fechas ISO. Negativo si end es
    anterior a start.
    """
    raise NotImplementedError


def age_on(birth: date, on: date) -> int:
    """Whole years of age on the given date (birthday counts on the day).

    ES: Años cumplidos en la fecha dada (el cumpleaños cuenta ese mismo día).
    """
    raise NotImplementedError


def convert_timezone(iso_local: str, from_tz: str, to_tz: str) -> str:
    """Interpret a naive ISO datetime ('2024-01-15T09:00:00') in from_tz
    (an IANA name like 'America/New_York'), convert to to_tz and return
    the result as an ISO string including the UTC offset.

    ES: Interpreta un datetime ISO naive en from_tz (nombre IANA), conviértelo
    a to_tz y devuelve una cadena ISO que incluya el desfase UTC.
    """
    raise NotImplementedError


def format_duration(delta: timedelta) -> str:
    """Format a non-negative timedelta as '1d 02h 03m' (days, zero-padded
    hours and minutes; seconds are dropped).

    ES: Da formato a un timedelta no negativo como '1d 02h 03m' (días, horas y
    minutos con ceros a la izquierda; se descartan los segundos).
    """
    raise NotImplementedError
