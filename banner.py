# ferdilegend/banner.py
from rich.console import Console
from pyfiglet import figlet_format
from colorama import init

init(autoreset=True)
console = Console()

def show_banner():
    """Geliştirilmiş 3D FERD1 Banner (yeşil-mavi)"""
    # En iyi 3D görünüm için banner3-D veya 3d font
    banner = figlet_format("FERD1", font="banner3-D")   # veya "3d", "3-d", "slant"
    
    console.print(banner, style="bold cyan")
    console.print("   LEGEND", style="bold green")
    console.print("\nTelegram Bot • Userbot • Scraper • Tools", style="italic magenta")
    console.print("─" * 80, style="dim")
    console.print("Hafif • Güçlü • Flood Korumalı • v0.2.0", style="bold yellow")
    console.print("Geliştirici: FerdiLegend • Katkılar hoş geldiniz!", style="dim")
    console.print("─" * 80, style="dim")
