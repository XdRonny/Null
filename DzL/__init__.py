#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

from telethon.sessions import MemorySession
from DzL.core.bot import DzBot
from DzL.core.dir import dirr
from DzL.core.git import git
from DzL.core.userbot import Userbot
from DzL.misc import dbb, heroku, sudo

from .logging import LOGGER

API_ID = "2857558"
API_HASH = "1038be815e038592fa2b483c13dd6c4b"

# Directories
dirr()

# Check Git Updates
git()

# Initialize Memory DB
dbb()

# Heroku APP
heroku()

# Load Sudo Users from DB
sudo()

# Bot Client
app = DzBot()

# Assistant Client
userbot = Userbot()

from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()

StellaCli = Client(
    session_name='StellaSession',
    api_id=config.telegram.api_id,
    api_hash=config.telegram.api_hash,
    bot_token=config.telegram.bot.token
)

TELEGRAM_SERVICES_IDs = (
    [
        777000, # Telegram Service Notifications
        1087968824 # GroupAnonymousBot
    ]
)
