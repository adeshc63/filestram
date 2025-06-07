import re
from os import environ, getenv

id_pattern = re.compile(r'^.\d+$')

# Modified by @marvaldoom

# Bot information
SESSION = environ.get('SESSION', 'WebMarvalDoom')
API_ID = int(environ.get('API_ID', '25928682'))
API_HASH = environ.get('API_HASH', '65b01e4ef42f8b3a1d5fd988e5aee5c9')
BOT_TOKEN = environ.get('BOT_TOKEN', "1587356098:AAFoXvkUzi3_O116zyr4L9R8tQ0w54joG54")
BOT_USERNAME = environ.get("BOT_USERNAME", 'Adsh4_bot') # without @ 

# Admins, Channels & Users
BIN_CHANNEL = int(environ.get("BIN_CHANNEL", '-1002141063405')) # admin your channel in stream 
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", '-1002141063405')) # admin your channel in users log 
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '821243884').split()] # 3567788, 678899, 5889467
OWNER_USERNAME = environ.get("OWNER_USERNAME", 'BOT_OWNER26') # without @ 

# pics information
PICS = environ.get('PICS', 'https://envs.sh/_pM.jpg')

# channel link information
CHANNEL = environ.get('CHANNEL', 'https://t.me/marvaldoom')
SUPPORT = environ.get('SUPPORT', 'https://t.me/marvaldoom')

# Modified by @marvaldoom

# file limit information
ENABLE_LIMIT = environ.get("ENABLE_LIMIT", False) # True and False
RATE_LIMIT_TIMEOUT = int(environ.get("RATE_LIMIT_TIMEOUT", "600"))  # limit time 600 = 10 minutes 
MAX_FILES = int(environ.get("MAX_FILES", "10"))  # file limit 10 file Olay

# Modified by @marvaldoom

# ban information
BANNED_CHANNELS = [int(banned_channels) if id_pattern.search(banned_channels) else banned_channels for banned_channels in environ.get('BANNED_CHANNELS', '').split()]   
BAN_CHNL = [int(ban_chal) if id_pattern.search(ban_chal) else ban_chal for ban_chal in environ.get('BAN_CHNL', '').split()]
BAN_ALERT = environ.get('BAN_ALERT' , '<b>ʏᴏᴜʀ ᴀʀᴇ ʙᴀɴɴᴇᴅ ᴛᴏ ᴜsᴇ ᴛʜɪs ʙᴏᴛ.ᴄᴏɴᴛᴀᴄᴛ [ᴄʜᴀᴛ ᴏᴡɴᴇʀ](https://telegram.me/AV_SUPPORT_GROUP) ᴛᴏ ʀᴇsᴏʟᴠᴇ ᴛʜᴇ ɪssᴜᴇ!!</b>')

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://Lodu12:Lodu12@doremon.reqbb.mongodb.net/")
DATABASE_NAME = environ.get('DATABASE_NAME', "FileStream")

# fsub  information
AUTH_PICS = environ.get('AUTH_PICS', 'https://envs.sh/AwV.jpg')              
AUTH_CHANNEL = (environ.get("AUTH_CHANNEL", "-1002141063405"))
FSUB = environ.get("FSUB", True)

# port information
PORT = int(getenv('PORT', '2626'))
NO_PORT = bool(getenv('NO_PORT', False))

# Modified by @marvaldoom

# time information
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))

# Online Stream and Download
BIND_ADDRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
WORKERS = int(getenv('WORKERS', '4'))
MULTI_CLIENT = False
name = str(environ.get('name', 'marvaldoom'))
APP_NAME = None
if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = str(getenv('APP_NAME')) #dont need to fill anything here
else:
    ON_HEROKU = False
FQDN = str(getenv('FQDN', BIND_ADDRESS)) if not ON_HEROKU or getenv('FQDN', '') else APP_NAME+'.herokuapp.com'
HAS_SSL=bool(getenv('HAS_SSL',False))
if HAS_SSL:
    URL = "https://ideal-thomasin-adeshc63-9dae396e.koyeb.app/".format(FQDN)
else:
    URL = "https://ideal-thomasin-adeshc63-9dae396e.koyeb.app/".format(FQDN, "" if NO_PORT else ":" + str(PORT))
      
# Modified by @marvaldoom
