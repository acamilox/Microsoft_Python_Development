from calculator import add
import pytest


def test_add():
    assert add(2, 3) == 5

# Run: pytest test_example.py