import json
from datetime import date

import pytest
from data_formats import (
    Event,
    csv_to_json,
    decode_event,
    encode_event,
    load_json,
    read_csv_rows,
    to_json,
    write_csv,
)


def test_to_json_sorted_and_indented():
    assert to_json({"b": 1, "a": [1, 2]}) == (
        '{\n  "a": [\n    1,\n    2\n  ],\n  "b": 1\n}'
    )


def test_to_json_keeps_unicode_escaped_roundtrip():
    assert json.loads(to_json({"k": "café"})) == {"k": "café"}


def test_read_csv_rows_basic():
    text = "name,age\nAda,36\nLin,29\n"
    assert read_csv_rows(text) == [
        {"name": "Ada", "age": "36"},
        {"name": "Lin", "age": "29"},
    ]


def test_read_csv_rows_quoted():
    text = 'name,note\n"Smith, J","said ""hi""\nthere"\n'
    assert read_csv_rows(text) == [{"name": "Smith, J", "note": 'said "hi"\nthere'}]


def test_write_csv():
    rows = [{"name": "Ada", "age": 36}, {"name": "Smith, J", "age": 5}]
    assert write_csv(rows, ["name", "age"]) == 'name,age\nAda,36\n"Smith, J",5\n'


def test_write_csv_field_order():
    assert write_csv([{"b": 2, "a": 1}], ["a", "b"]) == "a,b\n1,2\n"


def test_csv_roundtrip():
    rows = [{"x": 'a "q", b', "y": "line1\nline2"}]
    assert read_csv_rows(write_csv(rows, ["x", "y"])) == rows


def test_csv_to_json():
    out = csv_to_json("name,age\nAda,36\n", ["age"])
    assert json.loads(out) == [{"name": "Ada", "age": 36}]
    assert out == '[\n  {\n    "age": 36,\n    "name": "Ada"\n  }\n]'


def test_event_roundtrip():
    e = Event("launch", date(2024, 3, 5), ["a", "b"])
    text = encode_event(e)
    assert json.loads(text)["when"] == "2024-03-05"
    assert decode_event(text) == e


def test_load_json_missing_returns_default(tmp_path):
    assert load_json(tmp_path / "nope.json", {"a": 1}) == {"a": 1}


def test_load_json_reads(tmp_path):
    f = tmp_path / "d.json"
    f.write_text('{"k": [1, 2]}')
    assert load_json(f, {}) == {"k": [1, 2]}


def test_load_json_invalid(tmp_path):
    f = tmp_path / "bad.json"
    f.write_text("{oops")
    with pytest.raises(ValueError):
        load_json(f, {})
