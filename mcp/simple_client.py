from mcp import Client, StdioServerParameters
from mcp.types import TextContent

import asyncio
import sys
from pathlib import Path


async def main():

    try:
        server_path = Path(__file__).parent / "server.py"

        if not server_path.exists():
            raise FileNotFoundError(
                f"Server file not found: {server_path}"
            )

        server_params = StdioServerParameters(
            command=sys.executable,
            args=[str(server_path)]
        )

        async with Client(server_params) as client:

            print("=" * 60)
            print("CONNECTED TO MCP SERVER")
            print("=" * 60)

            print(f"Protocol Version: {client.protocol_version}")

            print("\nServer Info:")
            print(client.server_info)

            # ------------------------------------------
            # LIST TOOLS
            # ------------------------------------------

            print("\n" + "=" * 60)
            print("AVAILABLE TOOLS")
            print("=" * 60)

            tools = await client.list_tools()

            for tool in tools.tools:
                print(f"- {tool.name}")

            # ------------------------------------------
            # CALL search_flights
            # ------------------------------------------

            print("\n" + "=" * 60)
            print("SEARCH FLIGHTS")
            print("=" * 60)

            response = await client.call_tool(
                "search_flights",
                {
                    "origin": "Bangalore",
                    "destination": "Dubai"
                }
            )

            for content in response.content:
                if isinstance(content, TextContent):
                    print(content.text)

            # ------------------------------------------
            # CALL add
            # ------------------------------------------

            print("\n" + "=" * 60)
            print("ADD TOOL")
            print("=" * 60)

            response = await client.call_tool(
                "add",
                {
                    "a": 10,
                    "b": 20
                }
            )

            for content in response.content:
                if isinstance(content, TextContent):
                    print(content.text)

    except FileNotFoundError as e:
        print(f"File Error: {e}")

    except Exception as e:
        print(f"Unexpected Error: {type(e).__name__}: {e}")


if __name__ == "__main__":
    asyncio.run(main())