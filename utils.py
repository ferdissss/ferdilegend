import asyncio
import time
from rich.console import Console

console = Console()

def rate_limit(delay: float = 1.2):
    """Akıllı rate limit (flood guard)"""
    time.sleep(delay)
    console.print(f"[dim]Rate limit uygulandı: {delay}s bekleme[/dim]")

async def async_rate_limit(delay: float = 1.2):
    await asyncio.sleep(delay)
