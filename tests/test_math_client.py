"""Tests for the math client functionality."""

import pytest

from jarvis.math_client import (
    EMPTY_QUESTION_ERROR,
    create_math_agent,
    solve_math_problem,
)


@pytest.mark.asyncio
async def test_create_math_agent() -> None:
    """Test creating a math agent."""
    agent = await create_math_agent()
    assert agent is not None


@pytest.mark.asyncio
async def test_solve_math_problem_with_invalid_input() -> None:
    """Test solving a math problem with invalid input."""
    with pytest.raises(ValueError, match=EMPTY_QUESTION_ERROR):
        await solve_math_problem("")
