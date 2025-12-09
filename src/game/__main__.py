# Update src/auto-dungeon/__main__.py
"""Entry point for the dungeon crawler application."""

from autodungeon.config.settings import settings
from autodungeon.utils.logging import setup_logging


def main() -> None:
    """Main entry point."""
    # Setup logging
    logger = setup_logging(
        level=settings.log_level,
        log_file=settings.log_file,
        enable_color=settings.enable_color,
    )
    
    logger.info("Starting Dungeon Crawler")
    logger.debug(f"Configuration: {settings}")
    
    # TODO: Initialize CLI app
    print("Dungeon Crawler - Coming Soon!")
    

if __name__ == "__main__":
    main()