from files import (
    append_line,
    count_words,
    files_with_suffix,
    load_json,
    read_lines,
    save_json,
    write_lines,
)


def test_write_and_read_lines(tmp_path):
    path = tmp_path / "deep" / "dir" / "notes.txt"
    write_lines(path, ["one", "two"])
    assert path.read_text(encoding="utf-8") == "one\ntwo\n"
    assert read_lines(path) == ["one", "two"]


def test_unicode_round_trip(tmp_path):
    path = tmp_path / "u.txt"
    write_lines(path, ["café ☕"])
    assert read_lines(path) == ["café ☕"]


def test_append_line(tmp_path):
    path = tmp_path / "log.txt"
    append_line(path, "a")
    append_line(path, "b")
    assert read_lines(path) == ["a", "b"]


def test_count_words(tmp_path):
    path = tmp_path / "w.txt"
    path.write_text("the quick  brown\n\nfox jumps\n", encoding="utf-8")
    assert count_words(path) == 5


def test_files_with_suffix(tmp_path):
    (tmp_path / "sub").mkdir()
    (tmp_path / "b.txt").write_text("")
    (tmp_path / "a.txt").write_text("")
    (tmp_path / "sub" / "c.txt").write_text("")
    (tmp_path / "sub" / "d.md").write_text("")
    (tmp_path / "dir.txt").mkdir()
    assert files_with_suffix(tmp_path, ".txt") == ["a.txt", "b.txt", "c.txt"]


def test_json_round_trip(tmp_path):
    path = tmp_path / "data.json"
    save_json(path, {"a": 1, "b": [True, None]})
    assert load_json(path) == {"a": 1, "b": [True, None]}


def test_load_json_missing_file(tmp_path):
    assert load_json(tmp_path / "nope.json") == {}
    assert load_json(tmp_path / "nope.json", {"x": 1}) == {"x": 1}
