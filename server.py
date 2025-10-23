# server.py
from fastmcp import FastMCP

mcp = FastMCP("Demo 🚀")

@mcp.tool
def suma(a: int, b: int) -> int:
    """Suma dos numeros"""
    return a + b

@mcp.tool
def multiplica(a: float, b: float) -> float:
    """Multiplica dos numeros"""
    return a * b

@mcp.tool
def divide(a: float, b: float) -> float:
    """Divide dos numeros"""
    return a / b

if __name__ == "__main__":
    mcp.run()