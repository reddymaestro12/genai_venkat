from mcp.server.mcpserver import MCPServer

server = MCPServer("Travel MCP Server")


# --------------------------------------------------
# TOOLS
# --------------------------------------------------

@server.tool()
def add(a: int, b: int) -> int:
    return a + b


@server.tool()
def search_flights(
    origin: str,
    destination: str
) -> str:
    return (
        f"Available flight found from "
        f"{origin} to {destination}. "
        f"Flight EK501 costs ₹28,000."
    )


@server.tool()
def book_hotel(
    city: str,
    nights: int
) -> str:
    return (
        f"Hotel booked in {city} "
        f"for {nights} nights."
    )


if __name__ == "__main__":
    server.run()