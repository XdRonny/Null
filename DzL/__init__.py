from telethon.sessions import MemorySession
from DzL.core.bot import DzBot
from DzL.core.dir import dirr
from DzL.core.git import git
from telethon import TelegramClient
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

#telthom
telethn = TelegramClient(MemorySession(), API_ID, API_HASH)

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
