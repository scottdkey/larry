import json

import pytest
from errors import (
    Account,
    ConfigError,
    InsufficientFundsError,
    get_nested,
    load_config,
    parse_int,
    run_all,
    safe_divide,
)


def test_parse_int():
    assert parse_int("42") == 42
    assert parse_int("nope") == 0
    assert parse_int("", default=-1) == -1


def test_safe_divide():
    assert safe_divide(6, 3) == 2
    assert safe_divide(1, 0) is None


def test_get_nested():
    data = {"a": {"b": {"c": 7}}, "x": 1}
    assert get_nested(data, ["a", "b", "c"]) == 7
    assert get_nested(data, ["a", "z"]) is None
    assert get_nested(data, ["x", "y"]) is None
    assert get_nested(data, []) == data


def test_withdraw_ok():
    acct = Account(100)
    assert acct.withdraw(30) == 70
    assert acct.balance == 70


def test_withdraw_insufficient():
    acct = Account(10)
    with pytest.raises(InsufficientFundsError) as info:
        acct.withdraw(50)
    assert info.value.balance == 10
    assert info.value.amount == 50
    assert str(info.value) == "cannot withdraw 50; balance is 10"
    assert acct.balance == 10


def test_withdraw_invalid_amount():
    with pytest.raises(ValueError):
        Account(10).withdraw(0)


def test_load_config():
    assert load_config('{"debug": true}') == {"debug": True}


def test_load_config_invalid_json_is_chained():
    with pytest.raises(ConfigError) as info:
        load_config("{oops")
    assert isinstance(info.value.__cause__, json.JSONDecodeError)


def test_load_config_requires_object():
    with pytest.raises(ConfigError):
        load_config("[1, 2]")


def test_run_all():
    def boom():
        raise RuntimeError("x")

    log: list[str] = []
    assert run_all([lambda: 1, boom, lambda: 2], log) == 1
    assert log == [
        "start", "ok", "end",
        "start", "failed", "end",
        "start", "ok", "end",
    ]  # fmt: skip
