# meta developer: @Berki_modul

__version__ = (1, 5, 3)
import os
import logging
from .. import loader, utils
import random
import time
import datetime
from telethon import functions
from telethon.tl.custom import Message

logger = logging.getLogger("Selfiepron")

@loader.tds
class Randompronorphoto(loader.Module):
    """Your the best friend in pron bro 
    
       модуль отправляет прон с небольшим шансом"""
    strings = {
        "name": "Selfie_or_pron",
        "loading_photo": "<emoji document_id=5215327832040811010>⏳</emoji> <b>loading your selfie/pron photo...</b>",
        "error_loading": "<b>Failed to get photos. Please unblock @SelfieRuBot</b>",
        "search": "<emoji document_id=5328311576736833844>🔴</emoji> loading your photo..."
    }
    
    async def Selfipocmd(self, message):
        """-> random photo"""

        await utils.answer(message, self.strings("loading_photo"))
        
        async with self._client.conversation("@SelfieRuBot") as conv:
            
            await conv.send_message("📸 Photo")
        
            otvet = await conv.get_response()
          
            if otvet.photo:
                phota = await self._client.download_media(otvet.photo, "selfie_pron")
                await message.client.send_message(
                    message.peer_id,
                    file=phota,
                    reply_to=getattr(message, "reply_to_msg_id", None),
                    )

                os.remove(phota)
                
                await message.delete()