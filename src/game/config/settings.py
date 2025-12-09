# Update src/auto-dungeon/config/settings.py
from pydantic_settings import BaseSettings
from pathlib import Path
from typing import Literal
import sys
from functools import lru_cache


def get_app_dir() -> Path:
    """Get application directory (handles both dev and packaged app)."""
    if getattr(sys, 'frozen', False):
        # Running as compiled executable
        return Path(sys.executable).parent
    else:
        # Running in development
        return Path(__file__).parent.parent.parent.parent


class Settings(BaseSettings):
    """Application settings with environment variable support."""
    
    # Application paths
    app_dir: Path = get_app_dir() 
    data_dir: Path = app_dir / "data"
    content_dir: Path = app_dir / "content"
    db_path: Path = data_dir / "db" / "dungeon.db"
    saves_dir: Path = data_dir / "saves"
    cache_dir: Path = data_dir / "cache"
    
    # LLM Settings
    ollama_host: str = "http://localhost:11434"
    router_model: str = "gemma2:2b"
    answerer_model: str = "mistral:7b"
    llm_timeout: int = 60
    llm_temperature: float = 0.7
    max_retries: int = 3
    
    # Embedding Settings
    embedding_model: str = "all-MiniLM-L6-v2"
    embedding_dimension: int = 384
    
    # Vector Database Settings
    lance_db_path: Path = data_dir / "lancedb"
    rag_top_k: int = 5
    similarity_threshold: float = 0.7
    
    # Graph Database Settings
    graph_cache_path: Path = cache_dir / "world_graph.pkl"
    
    # Logging
    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR"] = "INFO"
    log_file: Path = data_dir / "dungeon.log"
    
    # CLI Settings
    enable_color: bool = True
    enable_streaming: bool = True
    command_history_size: int = 100
    
    class Config:
        env_file = ".env"
        env_prefix = "DUNGEON_"
        case_sensitive = False
    
    def ensure_directories(self) -> None:
        """Create all necessary directories."""
        for path in [
            self.data_dir,
            self.content_dir,
            self.db_path.parent,
            self.saves_dir,
            self.cache_dir,
            self.lance_db_path,
        ]:
            path.mkdir(parents=True, exist_ok=True)


@lru_cache()
def get_settings() -> Settings:
    """Get cached settings instance."""
    settings = Settings()
    settings.ensure_directories()
    return settings


# Global settings instance
settings = get_settings()