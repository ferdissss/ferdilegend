from pyrogram import Client
from .utils import rate_limit

class UserBotHelper:
    def __init__(self, session_name: str = "userbot"):
        self.app = Client(session_name)
    
    async def send_message_safe(self, chat_id, text):
        """Flood korumalı mesaj gönderme"""
        await self.app.send_message(chat_id, text)
        rate_limit(1.0)
