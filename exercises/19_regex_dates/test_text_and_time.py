from datetime import date, timedelta

import pytest
from text_and_time import (
    age_on,
    convert_timezone,
    days_between,
    extract_emails,
    format_duration,
    parse_log_line,
)


def test_extract_emails():
    text = "Mail ada@example.com or a.b+c@mail.co.uk; not me@localhost."
    assert extract_emails(text) == ["ada@example.com", "a.b+c@mail.co.uk"]


def test_extract_emails_none():
    assert extract_emails("nothing here @ all") == []


def test_parse_log_line():
    assert parse_log_line("2024-03-05 14:22:01 ERROR Disk full") == {
        "date": "2024-03-05",
        "time": "14:22:01",
        "level": "ERROR",
        "message": "Disk full",
    }


@pytest.mark.parametrize(
    "line",
    ["", "garbage", "2024-03-05 14:22:01 error lower", "2024-3-5 14:22:01 INFO x"],
)
def test_parse_log_line_no_match(line):
    assert parse_log_line(line) is None


@pytest.mark.parametrize(
    ("a", "b", "n"),
    [
        ("2024-03-05", "2024-03-06", 1),
        ("2024-02-28", "2024-03-01", 2),
        ("2023-02-28", "2023-03-01", 1),
        ("2024-03-05", "2024-03-01", -4),
    ],
)
def test_days_between(a, b, n):
    assert days_between(a, b) == n


@pytest.mark.parametrize(
    ("on", "expected"),
    [
        (date(2024, 5, 14), 23),
        (date(2024, 5, 15), 24),
        (date(2024, 5, 16), 24),
        (date(2025, 1, 1), 24),
    ],
)
def test_age_on(on, expected):
    assert age_on(date(2000, 5, 15), on) == expected


def test_age_leap_day_birthday():
    assert age_on(date(2000, 2, 29), date(2001, 2, 28)) == 0
    assert age_on(date(2000, 2, 29), date(2001, 3, 1)) == 1


def test_convert_timezone_winter():
    got = convert_timezone("2024-01-15T09:00:00", "America/New_York", "UTC")
    assert got == "2024-01-15T14:00:00+00:00"


def test_convert_timezone_summer_dst():
    got = convert_timezone("2024-07-15T09:00:00", "America/New_York", "Europe/Paris")
    assert got == "2024-07-15T15:00:00+02:00"


@pytest.mark.parametrize(
    ("delta", "expected"),
    [
        (timedelta(0), "0d 00h 00m"),
        (timedelta(days=1, hours=2, minutes=3, seconds=59), "1d 02h 03m"),
        (timedelta(hours=49), "2d 01h 00m"),
        (timedelta(minutes=75), "0d 01h 15m"),
    ],
)
def test_format_duration(delta, expected):
    assert format_duration(delta) == expected
