"""Tests for the math server functionality."""

import pytest

from jarvis.math_server import add, multiply

# Test constants
POSITIVE_A = 2
POSITIVE_B = 3
POSITIVE_SUM = 5
NEGATIVE_A = -2
NEGATIVE_B = -3
NEGATIVE_SUM = -5
POSITIVE_PRODUCT = 6
NEGATIVE_PRODUCT = -6
ZERO = 0
FIVE = 5


def test_add_positive_numbers() -> None:
    """Test adding two positive numbers."""
    assert add(POSITIVE_A, POSITIVE_B) == POSITIVE_SUM


def test_add_negative_numbers() -> None:
    """Test adding two negative numbers."""
    assert add(NEGATIVE_A, NEGATIVE_B) == NEGATIVE_SUM


def test_add_zero() -> None:
    """Test adding zero to a number."""
    assert add(FIVE, ZERO) == FIVE
    assert add(ZERO, FIVE) == FIVE
    assert add(ZERO, ZERO) == ZERO


def test_multiply_positive_numbers() -> None:
    """Test multiplying two positive numbers."""
    assert multiply(POSITIVE_A, POSITIVE_B) == POSITIVE_PRODUCT


def test_multiply_negative_numbers() -> None:
    """Test multiplying two negative numbers."""
    assert multiply(NEGATIVE_A, NEGATIVE_B) == POSITIVE_PRODUCT


def test_multiply_negative_and_positive() -> None:
    """Test multiplying a negative and positive number."""
    assert multiply(NEGATIVE_A, POSITIVE_B) == NEGATIVE_PRODUCT
    assert multiply(POSITIVE_A, NEGATIVE_B) == NEGATIVE_PRODUCT


def test_multiply_by_zero() -> None:
    """Test multiplying by zero."""
    assert multiply(FIVE, ZERO) == ZERO
    assert multiply(ZERO, FIVE) == ZERO
    assert multiply(ZERO, ZERO) == ZERO


def test_add_invalid_types() -> None:
    """Test adding with invalid types raises TypeError."""
    with pytest.raises(TypeError):
        add("2", 3)  # type: ignore[arg-type]
    with pytest.raises(TypeError):
        add(2, "3")  # type: ignore[arg-type]


def test_multiply_invalid_types() -> None:
    """Test multiplying with invalid types raises TypeError."""
    with pytest.raises(TypeError):
        multiply("2", 3)  # type: ignore[arg-type]
    with pytest.raises(TypeError):
        multiply(2, "3")  # type: ignore[arg-type]
