
# ferdilegend/__init__.py
from .banner import show_banner
from .scraper import TelegramScraper
from .userbot import UserBotHelper
from .utils import rate_limit

__version__ = "0.3.0"

__all__ = ["show_banner", "TelegramScraper", "UserBotHelper", "rate_limit"]

# Paket import edildiğinde otomatik 3D banner çıksın
show_banner()
