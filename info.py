import re
import os
from os import environ
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

id_pattern = re.compile(r'^.\d+$')

#Dont Remove My Credit @AV_BOTz_UPDATE 
#This Repo Is By @BOT_OWNER26 
# For Any Kind Of Error Ask Us In Support Group @AV_SUPPORT_GROUP

# Bot information
SESSION = os.getenv('SESSION')
API_ID = int(os.getenv('API_ID'))
API_HASH = os.getenv('API_HASH')
BOT_TOKEN = os.getenv('BOT_TOKEN')
BOT_USERNAME = os.getenv("BOT_USERNAME")

# Admins, Channels & Users
BIN_CHANNEL = int(os.getenv("BIN_CHANNEL"))
LOG_CHANNEL = int(os.getenv("LOG_CHANNEL"))
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in os.getenv('ADMINS', '').split()]
OWNER_USERNAME = os.getenv("OWNER_USERNAME")

# pics information
PICS = os.getenv('PICS')

# channel link information
CHANNEL = os.getenv('CHANNEL')
SUPPORT = os.getenv('SUPPORT')

# file limit information
ENABLE_LIMIT = os.getenv("ENABLE_LIMIT", 'False').lower() == 'true'
RATE_LIMIT_TIMEOUT = int(os.getenv("RATE_LIMIT_TIMEOUT", "600"))
MAX_FILES = int(os.getenv("MAX_FILES", "10"))

# ban information
BANNED_CHANNELS = [int(banned_channels) if id_pattern.search(banned_channels) else banned_channels for banned_channels in os.getenv('BANNED_CHANNELS', '').split()]   
BAN_CHNL = [int(ban_chal) if id_pattern.search(ban_chal) else ban_chal for ban_chal in os.getenv('BAN_CHNL', '').split()]
BAN_ALERT = os.getenv('BAN_ALERT', '<b>ʏᴏᴜʀ ᴀʀᴇ ʙᴀɴɴᴇᴅ ᴛᴏ ᴜsᴇ ᴛʜɪs ʙᴏᴛ.ᴄᴏɴᴛᴀᴄᴛ [ᴀᴠ ᴄʜᴀᴛ ᴏᴡɴᴇʀ](https://telegram.me/marvaldoom) ᴛᴏ ʀᴇsᴏʟᴠᴇ ᴛʜᴇ ɪssᴜᴇ!!</b>')

# MongoDB information
DATABASE_URI = os.getenv('DATABASE_URI')
DATABASE_NAME = os.getenv('DATABASE_NAME')

# fsub information
AUTH_PICS = os.getenv('AUTH_PICS')
AUTH_CHANNEL = os.getenv("AUTH_CHANNEL")
FSUB = os.getenv("FSUB", 'True').lower() == 'true'

# port information
PORT = int(os.getenv('PORT', '2626'))
NO_PORT = os.getenv('NO_PORT', 'False').lower() == 'true'

# time information
PING_INTERVAL = int(os.getenv("PING_INTERVAL", "1200"))
SLEEP_THRESHOLD = int(os.getenv('SLEEP_THRESHOLD', '60'))

# Online Stream and Download
BIND_ADDRESS = str(os.getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
WORKERS = int(os.getenv('WORKERS', '4'))
MULTI_CLIENT = False
name = str(os.getenv('name', 'avbotz'))
APP_NAME = None

if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = str(os.getenv('APP_NAME'))
else:
    ON_HEROKU = False

FQDN = str(os.getenv('FQDN', BIND_ADDRESS)) if not ON_HEROKU or os.getenv('FQDN', '') else APP_NAME+'.herokuapp.com'
HAS_SSL = os.getenv('HAS_SSL', 'False').lower() == 'true'
URL = os.getenv('URL')
