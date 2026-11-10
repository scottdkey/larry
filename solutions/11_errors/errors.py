"""Lesson 11 reference solution."""

import json
from collections.abc import Mapping


def parse_int(text: str, default: int = 0) -> int:
    try:
        return int(text)
    except ValueError:
        return default


def safe_divide(a: float, b: float) -> float | None:
    try:
        return a / b
    except ZeroDivisionError:
        return None


def get_nested(data: Mapping[str, object], keys: list[str]) -> object | None:
    current: object = data
    for key in keys:
        try:
            current = current[key]  # ty: ignore[not-subscriptable]
        except (KeyError, TypeError):
            return None
    return current


class InsufficientFundsError(Exception):
    def __init__(self, balance: int, amount: int) -> None:
        super().__init__(f"cannot withdraw {amount}; balance is {balance}")
        self.balance = balance
        self.amount = amount


class Account:
    def __init__(self, balance: int = 0) -> None:
        self.balance = balance

    def withdraw(self, amount: int) -> int:
        if amount <= 0:
            raise ValueError("amount must be positive")
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        return self.balance


class ConfigError(Exception):
    pass


def load_config(text: str) -> dict[str, object]:
    try:
        config = json.loads(text)
    except json.JSONDecodeError as exc:
        raise ConfigError("config is not valid JSON") from exc
    if not isinstance(config, dict):
        raise ConfigError("config must be a JSON object")
    return config


def run_all(tasks: list, log: list[str]) -> int:
    failures = 0
    for task in tasks:
        log.append("start")
        try:
            task()
        except Exception:
            failures += 1
            log.append("failed")
        else:
            log.append("ok")
        finally:
            log.append("end")
    return failures
