from cli import app
from typer.testing import CliRunner

runner = CliRunner()


def test_greet():
    result = runner.invoke(app, ["greet", "Ada"])
    assert result.exit_code == 0
    assert result.stdout.strip() == "Hello, Ada!"


def test_greet_shout():
    result = runner.invoke(app, ["greet", "Ada", "--shout"])
    assert result.stdout.strip() == "HELLO, ADA!"


def test_add_and_bad_input():
    assert runner.invoke(app, ["add", "2", "40"]).stdout.strip() == "42"
    assert runner.invoke(app, ["add", "2", "x"]).exit_code == 2


def test_repeat_default_and_short_option():
    assert runner.invoke(app, ["repeat", "hi"]).stdout.splitlines() == ["hi", "hi"]
    result = runner.invoke(app, ["repeat", "hi", "-n", "3"])
    assert result.stdout.splitlines() == ["hi"] * 3
    result = runner.invoke(app, ["repeat", "hi", "--times", "1"])
    assert result.stdout.splitlines() == ["hi"]


def test_repeat_rejects_zero():
    for option in ("-n", "--times"):
        result = runner.invoke(app, ["repeat", "hi", option, "0"])
        assert result.exit_code == 2
        assert "No such option" not in result.output
        assert "Usage:" not in result.output
        assert result.output.strip()


def test_stats():
    result = runner.invoke(app, ["stats", "1", "2", "6"])
    assert result.stdout.splitlines() == ["min=1", "max=6", "mean=3"]


def test_convert():
    assert runner.invoke(app, ["convert", "100"]).stdout.strip() == "212.0"
    result = runner.invoke(app, ["convert", "212", "--direction", "f2c"])
    assert result.stdout.strip() == "100.0"
    assert runner.invoke(app, ["convert", "1", "--direction", "k"]).exit_code == 2
