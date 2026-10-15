# Bulletproof Calculator (practice)

A small practice project for the Clean Code, Testing & Git module. It contains one function, `divide_funds(total, parts)`, built to never crash.

## What it does

- Divides `total` by `parts` and returns the result.
- Returns `None` instead of crashing on a zero divisor (`ZeroDivisionError`) or invalid input types (`TypeError`).
- Logs `INFO` for each successful calculation and `ERROR` with a traceback for each failure.

## What I practiced

- **Exception handling:** `try`/`except` with specific exceptions, not a bare `except`.
- **Logging:** a module-level logger, `INFO` and `ERROR` levels, tracebacks with `logger.exception`.
- **Code quality:** Black for formatting, Ruff for linting, mypy for type checking, and a Google-style docstring with type hints.
- **Testing:** pytest tests for a valid division, division by zero and invalid types, with `caplog` to check log output.
- **Coverage:** 100% with `pytest-cov`.

## Setup

```powershell
poetry install
```

## Run the checks

```powershell
poetry run black --check src tests
poetry run ruff check src tests
poetry run mypy src
poetry run pytest --cov=black_practice --cov-report=term-missing
```

## Project layout

```
src/black_practice/hands_on.py   the divide_funds function
tests/test_first.py              pytest tests
```