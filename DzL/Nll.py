from telethon.sessions import MemorySession
from DzL.core.bot import DzBot
from DzL.core.dir import dirr
from DzL.core.git import git
from pyrogram import Client
from DzL.core.userbot import Userbot
from DzL.misc import dbb, heroku, sudo

from .logging import LOGGER


API_ID = "2857558"
API_HASH = "1038be815e038592fa2b483c13dd6c4b"


StellaCli = Client(
    session_name='StellaSession',
    api_id='2857558',
    api_hash='1038be815e038592fa2b483c13dd6c4b',
    bot_token='5443512927:AAFElVBnUHJ-DdQQAz0zctEk1A_eY3a-gR0'
)

TELEGRAM_SERVICES_IDs = (
    [
        777000, # Telegram Service Notifications
        1087968824 # GroupAnonymousBot
    ]
)
