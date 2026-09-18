from fastmcp import FastMCP
import json

mcp = FastMCP("Simple Calculator Server")

@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp.resource("info://server")
def server_info() -> str:
    """Get info about server"""
    info = {
        "name": "Simple Claculator Server",
        "version": "1.0.0",
        "description": "A basic MCP server wth math tool",
        "tool": ['add'],
        "author": "Gururaj"
    }
    return json.dumps(info, indent=2)

if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)