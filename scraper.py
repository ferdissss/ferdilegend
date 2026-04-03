from telethon import TelegramClient
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch
from .utils import rate_limit
from rich.progress import track
import pandas as pd

class TelegramScraper:
    def __init__(self, client: TelegramClient):
        self.client = client

    async def scrape_members(self, channel_username: str, limit: int = 1000):
        """Grup/kanal üyelerini scraper (limitlere dikkat!)"""
        console = Console()
        console.print(f"[cyan]Scraper başlatılıyor: {channel_username}[/cyan]")
        
        members = []
        offset = 0
        
        while len(members) < limit:
            participants = await self.client(GetParticipantsRequest(
                channel=channel_username,
                filter=ChannelParticipantsSearch(''),
                offset=offset,
                limit=200,
                hash=0
            ))
            
            if not participants.users:
                break
                
            for user in participants.users:
                members.append({
                    'id': user.id,
                    'username': user.username,
                    'first_name': user.first_name,
                    'last_name': user.last_name
                })
            
            offset += len(participants.users)
            rate_limit(1.5)  # Flood koruması
            
            console.print(f"[green]Toplanan üye: {len(members)}[/green]")
        
        # Pandas ile güzel tablo
        df = pd.DataFrame(members)
        console.print(df.head())
        return df

    async def scrape_messages(self, channel_username: str, limit: int = 500):
        """Mesaj scraper"""
        messages = []
        async for message in self.client.iter_messages(channel_username, limit=limit):
            messages.append({
                'id': message.id,
                'text': message.text,
                'date': message.date,
                'from_id': message.sender_id
            })
            if len(messages) % 50 == 0:
                rate_limit(0.8)
        
        df = pd.DataFrame(messages)
        return df
