#this will work for mcp server 1.x not for mcp server >=1.4.0
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Travel MCP Server")


@mcp.tool()
def add(a: int, b: int) -> int:
    return a + b


@mcp.tool()
def search_flights(
    origin: str,
    destination: str
) -> str:
    return (
        f"Available flight found from "
        f"{origin} to {destination}. "
        f"Flight EK501 costs ₹28,000."
    )


@mcp.tool()
def book_hotel(
    city: str,
    nights: int
) -> str:
    return f"Hotel booked in {city} for {nights} nights."


if __name__ == "__main__":
    mcp.run()