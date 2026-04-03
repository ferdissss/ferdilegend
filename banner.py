# ferdilegend/banner.py
from rich.console import Console
from pyfiglet import figlet_format
from colorama import init

init(autoreset=True)
console = Console()

def show_banner():
    """3D FERD1 Banner (Yeşil-Mavi)"""
    banner = figlet_format("FERD1", font="larry3d")   # Alternatif: "banner3-D" veya "3-d"
    
    console.print(banner, style="bold cyan")
    console.print("   LEGEND", style="bold green")
    
    console.print("\nTelegram Bot • Userbot • Scraper • Tools", style="italic magenta")
    console.print("─" * 80, style="dim")
    console.print("Hafif • Güçlü • Flood Korumalı • v0.3.0", style="bold yellow")
    console.print("Geliştirici: FerdiLegend", style="dim")
    console.print("─" * 80, style="dim")
