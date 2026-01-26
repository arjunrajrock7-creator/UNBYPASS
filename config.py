import os
from os import environ, getenv
import logging
from logging.handlers import RotatingFileHandler

#--------------------------------------------
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "8540782287:AAGDrv6eW4BjtMDYTpgxotS5m0p6ZBkSNdM")
APP_ID = int(os.environ.get("APP_ID", "31355944")) #Your API ID from my.telegram.org
API_HASH = os.environ.get("API_HASH", "167e960d46363e3098f9c1fc78496adb") #Your API Hash from my.telegram.org
#--------------------------------------------

CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1003549022692")) #Your db channel Id
OWNER = os.environ.get("OWNER", "ALONEKINGSTAR77") # Owner username without @
OWNER_ID = int(os.environ.get("OWNER_ID", "8557029592")) # Owner id
#--------------------------------------------
PORT = os.environ.get("PORT", "8001")
WEB_DOMAIN = os.environ.get("WEB_DOMAIN", "https://your-app-name.onrender.com")
#--------------------------------------------
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://botskingdom2:t7ognZuINrNfH3tj@cluster0.ystdy4m.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")
#--------------------------------------------
FSUB_LINK_EXPIRY = int(os.getenv("FSUB_LINK_EXPIRY", "10"))  # 0 means no expiry
BAN_SUPPORT = os.environ.get("BAN_SUPPORT", "https://t.me/anixzone")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "200"))
#--------------------------------------------
START_PIC = os.environ.get("START_PIC", "https://freeimage.host/i/fr18tY7")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://freeimage.host/i/fr18Dv9")

#--------------------------------------------
SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "arolinks.com")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "e49643875c2fa34dd6087254e58283d65ffc7748")
TUT_VID = os.environ.get("TUT_VID","https://t.me/anixzone")

SHORT_MSG = "<b><blockquote>⛩️ Here is Your Download Link\n\nMust Watch Tutorial Before Clicking On Download...</blockquote></b>"

SHORTENER_PIC = os.environ.get("SHORTENER_PIC", "https://freeimage.host/i/fr18bpe")
#--------------------------------------------

#--------------------------------------------
HELP_TXT = "<b><blockquote>⛩️ ᴛʜɪs ɪs ᴀɴ ғɪʟᴇ ᴛᴏ ʟɪɴᴋ ʙᴏᴛ ᴡᴏʀᴋ ғᴏʀ @ALONEKINGSTAR77\n\n❏ ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅs\n├/start : sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ\n├/about : ᴏᴜʀ ɪɴғᴏʀᴍᴀᴛɪᴏɴ\n└/help : ʜᴇʟᴘ ʀᴇʟᴀᴛᴇᴅ ʙᴏᴛ\n\n🌸 sɪᴍᴘʟʏ ᴄʟɪᴄᴋ ᴏɴ ʟɪɴᴋ ᴀɴᴅ sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ ᴊᴏɪɴ ʙᴏᴛʜ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ ᴛʜᴀᴛs ɪᴛ.....!\n\n🏮 ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ <a href=https://t.me/anixzone>ᴀʟᴏɴᴇᴋɪɴɢsᴛᴀʀ77</a></blockquote></b>"
ABOUT_TXT = (
    "<b><blockquote>"
    "🍥 <u>ʙᴏᴛ ɪɴғᴏ</u> 🍥\n\n"
    "👑 ◈ ᴄʀᴇᴀᴛᴏʀ : <a href=https://t.me/anixzone>ᴀʟᴏɴᴇᴋɪɴɢsᴛᴀʀ77</a>\n"
    "🚀 ◈ ꜰᴏᴜɴᴅᴇʀ ᴏꜰ : <a href=https://t.me/anixzone>ᴀʟᴏɴᴇᴋɪɴɢsᴛᴀʀ77</a>\n"
    "🎌 ◈ ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/anixzone>ᴀʟᴏɴᴇᴋɪɴɢsᴛᴀʀ77</a>\n"
    "🧑‍💻 ◈ ᴅᴇᴠᴇʟᴏᴘᴇʀ : <a href=https://t.me/anixzone>ᴀʟᴏɴᴇᴋɪɴɢsᴛᴀʀ77</a>\n\n"
    "💎 <i>ᴘʀᴇᴍɪᴜᴍ • ꜱᴛᴀʙʟᴇ • ꜰᴀꜱᴛ</i>"
    "</blockquote></b>"
)
#--------------------------------------------
#--------------------------------------------
START_MSG = os.environ.get(
    "START_MESSAGE",
    "<b>✨ Welcome {mention}! I’m fully active and ready to help you.\n\n"
    "<blockquote>"
    "👺 ɪ ᴀᴍ ᴀ ᴘʀᴇᴍɪᴜᴍ <u>ꜰɪʟᴇ ꜱᴛᴏʀᴇ ʙᴏᴛ</u>\n\n"
    "🔐 ɪ ꜱᴀꜰᴇʟʏ ꜱᴛᴏʀᴇ ᴘʀɪᴠᴀᴛᴇ ꜰɪʟᴇs ɪɴ ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴄʜᴀɴɴᴇʟs.\n"
    "🔗 ᴜsᴇʀs ᴄᴀɴ ᴀᴄᴄᴇss ᴛʜᴇᴍ ᴜsɪɴɢ <b>sᴘᴇᴄɪᴀʟ ʟɪɴᴋs</b>.\n\n"
    "⚡ Let me know what you need today 🇮🇳💙</blockquote></b>"
)

FORCE_MSG = os.environ.get(
    "FORCE_SUB_MESSAGE",
    "<b>🏮 ʜᴇʟʟᴏ {mention}\n\n"
    "<blockquote>"
    "📢 <u>ᴀᴄᴄᴇss ʀᴇǫᴜɪʀᴇᴅ</u>\n\n"
    "✅ ᴊᴏɪɴ ᴏᴜʀ ᴏꜰꜰɪᴄɪᴀʟ ᴄʜᴀɴɴᴇʟ\n"
    "🔄 ᴛʜᴇɴ ᴄʟɪᴄᴋ <b>ʀᴇʟᴏᴀᴅ</b> ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛᴇᴅ ꜰɪʟᴇ\n\n"
    "🌸 <i>ᴛʜᴀɴᴋ ʏᴏᴜ ꜰᴏʀ ꜱᴜᴘᴘᴏʀᴛɪɴɢ</i>"
    "</blockquote></b>"
)

#--------------------------------------------
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>• ʙʏ @ALONEKINGSTAR77</b>")
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'
BOT_STATS_TEXT = "<b>⛩️ BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "ʙᴀᴋᴋᴀ ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ!!"

#==========================(BUY PREMIUM)====================#
OWNER_TAG = os.environ.get("OWNER_TAG", "ALONEKINGSTAR77")
UPI_ID = os.environ.get("UPI_ID", "aloneking@upi")
QR_PIC = os.environ.get("QR_PIC", "https://freeimage.host/i/fr18bpe")
SCREENSHOT_URL = os.environ.get("SCREENSHOT_URL", "https://t.me/anixzone")

#Time and its price
PRICE1 = os.environ.get("PRICE1", "Free")
PRICE2 = os.environ.get("PRICE2", "50 INR")
PRICE3 = os.environ.get("PRICE3", "120 INR")
PRICE4 = os.environ.get("PRICE4", "200 INR")
PRICE5 = os.environ.get("PRICE5", "400 INR")

#===================(END)========================#

LOG_FILE_NAME = "filesharingbot.txt"

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
