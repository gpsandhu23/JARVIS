"""Math Server using FastMCP.

This module provides basic mathematical operations as MCP tools.
"""

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Math")

# Error messages
TYPE_ERROR_MSG = "Both arguments must be integers"


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers.

    Args:
        a: First number
        b: Second number

    Returns:
        Sum of the two numbers

    Raises:
        TypeError: If inputs are not integers
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError(TYPE_ERROR_MSG)
    return a + b


@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers.

    Args:
        a: First number
        b: Second number

    Returns:
        Product of the two numbers

    Raises:
        TypeError: If inputs are not integers
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError(TYPE_ERROR_MSG)
    return a * b


if __name__ == "__main__":
    mcp.run(transport="stdio")
