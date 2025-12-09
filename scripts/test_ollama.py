#!/usr/bin/env python3
"""Test Ollama connection and models."""

import ollama
from rich.console import Console
from rich.table import Table

console = Console()

def test_connection():
    """Test Ollama connection."""
    try:
        models = ollama.list()
        console.print("[green]✓[/green] Ollama connection successful!")
        
        # Display available models
        table = Table(title="Available Models")
        table.add_column("Model", style="cyan")
        table.add_column("Size", style="magenta")
        
        for model in models.get('models', []):
            name = model.get('name', 'Unknown')
            size = model.get('size', 0)
            size_gb = size / (1024**3)
            table.add_row(name, f"{size_gb:.2f} GB")
        
        console.print(table)
        
        # Test a simple generation
        console.print("\n[cyan]Testing generation...[/cyan]")
        response = ollama.generate(
            model='gemma2:2b',
            prompt='Say "Hello from the dungeon!" in 5 words or less.'
        )
        console.print(f"[green]Response:[/green] {response['response']}")
        
    except Exception as e:
        console.print(f"[red]✗[/red] Ollama connection failed: {e}")
        return False
    
    return True

if __name__ == "__main__":
    test_connection()
EOF

chmod +x scripts/test_ollama.py
python scripts/test_ollama.py