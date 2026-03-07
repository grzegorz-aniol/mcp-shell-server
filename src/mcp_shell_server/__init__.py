"""MCP Shell Server Package."""

from . import server

__version__ = "0.1.0"
__all__ = ["main", "server"]


def main():
    """Main entry point for the package."""
    import argparse
    import asyncio

    parser = argparse.ArgumentParser(description="MCP Shell Server")
    parser.add_argument(
        "--transport",
        choices=("stdio", "streamableHttp"),
        default="stdio",
        help="Transport protocol (default: stdio)",
    )
    args = parser.parse_args()

    asyncio.run(server.main(transport=args.transport))


if __name__ == "__main__":
    main()
