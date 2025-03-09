"""Tests for the math client functionality."""

import pytest

from jarvis.math_client import (
    EMPTY_QUESTION_ERROR,
    NON_MATH_RESPONSE,
    create_math_agent,
    solve_math_problem,
)


@pytest.mark.asyncio
async def test_create_math_agent() -> None:
    """Test creating a math agent."""
    agent = await create_math_agent()
    assert agent is not None


@pytest.mark.asyncio
async def test_solve_simple_math_problem() -> None:
    """Test solving a simple math problem."""
    question = "what's (3 + 5) x 12?"
    result = await solve_math_problem(question)
    expected = (
        "Let me solve this step by step:\n"
        "1. First, (3 + 5) = 8\n"
        "2. Then, 8 x 12 = 96\n"
        "The answer is 96."
    )
    assert result == expected


@pytest.mark.asyncio
async def test_solve_math_problem_with_invalid_input() -> None:
    """Test solving a math problem with invalid input."""
    with pytest.raises(ValueError, match=EMPTY_QUESTION_ERROR):
        await solve_math_problem("")


@pytest.mark.asyncio
async def test_solve_math_problem_with_non_math_question() -> None:
    """Test solving a non-math question."""
    question = "what's the weather like?"
    result = await solve_math_problem(question)
    assert result == NON_MATH_RESPONSE
