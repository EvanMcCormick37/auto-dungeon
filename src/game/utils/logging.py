# Create src/auto-dungeon/utils/logging.py
"""Structured logging configuration."""

import logging
import sys
from pathlib import Path
from typing import Optional
from rich.logging import RichHandler
from rich.console import Console


def setup_logging(
    level: str = "INFO",
    log_file: Optional[Path] = None,
    enable_color: bool = True,
) -> logging.Logger:
    """Configure application logging with Rich formatting."""
    
    # Create logger
    logger = logging.getLogger("dungeon")
    logger.setLevel(getattr(logging, level.upper()))
    
    # Remove existing handlers
    logger.handlers.clear()
    
    # Console handler with Rich
    if enable_color:
        console_handler = RichHandler(
            console=Console(stderr=True),
            rich_tracebacks=True,
            tracebacks_show_locals=True,
            show_time=True,
            show_path=False,
        )
    else:
        console_handler = logging.StreamHandler(sys.stderr)
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        console_handler.setFormatter(formatter)
    
    console_handler.setLevel(getattr(logging, level.upper()))
    logger.addHandler(console_handler)
    
    # File handler (if specified)
    if log_file:
        log_file.parent.mkdir(parents=True, exist_ok=True)
        file_handler = logging.FileHandler(log_file)
        file_formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s'
        )
        file_handler.setFormatter(file_formatter)
        file_handler.setLevel(logging.DEBUG)  # Always log DEBUG to file
        logger.addHandler(file_handler)
    
    return logger


# Create convenience functions
def get_logger(name: str) -> logging.Logger:
    """Get a child logger."""
    return logging.getLogger(f"dungeon.{name}")