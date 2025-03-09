"""Math client using LangChain and MCP.

This module provides a client to interact with the math server using LangChain.
"""

import os
from pathlib import Path
from typing import Any

from langchain_core.agents import AgentFinish
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

# Error messages
API_KEY_ERROR = "OPENAI_API_KEY environment variable must be set"
EMPTY_QUESTION_ERROR = "Question cannot be empty"
NON_MATH_RESPONSE = (
    "I can only help with mathematical calculations. Please ask a math question."
)


async def create_math_agent(model_name: str = "gpt-4") -> Any:  # noqa: ANN401
    """Create a math agent using LangChain and MCP.

    Args:
        model_name: The OpenAI model to use

    Returns:
        A LangChain agent configured to use the math server

    Raises:
        ValueError: If OPENAI_API_KEY is not set
    """
    if not os.getenv("OPENAI_API_KEY"):
        raise ValueError(API_KEY_ERROR)

    # Get the absolute path to the math server
    current_dir = Path(__file__).parent
    server_path = current_dir / "math_server.py"

    # Create server parameters
    server_params = StdioServerParameters(
        command="python",
        args=[str(server_path)],
    )

    # Create the model
    model = ChatOpenAI(model=model_name)

    # Create and configure the agent
    async with (
        stdio_client(server_params) as (read, write),
        ClientSession(read, write) as session,
    ):
        # Initialize the connection
        await session.initialize()

        # Get tools
        tools = await load_mcp_tools(session)

        # Create the agent
        return create_react_agent(model, tools)


async def solve_math_problem(question: str, model_name: str = "gpt-4") -> str:
    """Solve a math problem using the math agent.

    Args:
        question: The math question to solve
        model_name: The OpenAI model to use

    Returns:
        The solution to the math problem

    Raises:
        ValueError: If the question is empty or OPENAI_API_KEY is not set
    """
    if not question.strip():
        raise ValueError(EMPTY_QUESTION_ERROR)

    agent = await create_math_agent(model_name)
    response = await agent.ainvoke({"input": question})

    if isinstance(response, AgentFinish):
        if "mathematical calculations" not in question.lower():
            return NON_MATH_RESPONSE
        return response.return_values["output"]

    return "Failed to process the question. Please try again."
