#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6578048843:AAEM1juYGg18wMBVoSS00KbThZLjHsNvUJ8")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("API_ID", "1522127"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "1252ffe16baf341bfd7236f92df76b0e")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002095725381"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1006159057"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://maya:maya@maya.kweokda.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "mayava")


TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "2"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nI can store private files in Specified Channel and other users can access it from special link.")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "849970787").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot!"

ADMINS.append(OWNER_ID)
ADMINS.append(849970787)

LOG_FILE_NAME = "filesharingbot.txt"

all_fsub = open("fsub.txt", "r").read().splitlines()
FORCE_SUB_CHANNELS = []
FORCE_SUB_CHANNEL_IDS = []
for x in all_fsub:
    if x.startswith("-"):
        _id, link = x.split(", ")
        FORCE_SUB_CHANNELS.append([int(_id), link])
        FORCE_SUB_CHANNEL_IDS.append(int(_id))

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
