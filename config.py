import os
from os import environ, getenv
import logging
from logging.handlers import RotatingFileHandler

#--------------------------------------------
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "8332413341:AAFQC6aMBmqEaD01LH5b1h_bDTjCTmPBG5g")
APP_ID = int(os.environ.get("APP_ID", "31355944")) #Your API ID from my.telegram.org
API_HASH = os.environ.get("API_HASH", "167e960d46363e3098f9c1fc78496adb") #Your API Hash from my.telegram.org
#--------------------------------------------

CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1003834448258")) #Your db channel Id
FORCE_SUB_CHANNELS = [int(i) for i in os.environ.get("FORCE_SUB_CHANNELS", "-1003834448258").split()]
OWNER = os.environ.get("OWNER", "ALONEKINGSTAR77") # Owner username without @
OWNER_ID = int(os.environ.get("OWNER_ID", "8557029592")) # Owner id
#--------------------------------------------
PORT = int(os.environ.get("PORT", "8001"))
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
RECAPTCHA_SITE_KEY = os.environ.get("RECAPTCHA_SITE_KEY", "")
RECAPTCHA_SECRET_KEY = os.environ.get("RECAPTCHA_SECRET_KEY", "")

SHORT_MSG = "<b><blockquote>⛩️ Here is Your Download Link\n\nMust Watch Tutorial Before Clicking On Download...</blockquote></b>"

SHORTENER_PIC = os.environ.get("SHORTENER_PIC", "https://freeimage.host/i/fr18bpe")
#--------------------------------------------

#--------------------------------------------
HELP_TXT = """<b><blockquote>⛩️ ᴛʜɪs ɪs ᴀɴ ғɪʟᴇ ᴛᴏ ʟɪɴᴋ ʙᴏᴛ ᴡᴏʀᴋ ғᴏʀ @ALONEKINGSTAR77

❏ ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅs
├ /start : sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ
├ /about : ᴏᴜʀ ɪɴғᴏʀᴍᴀᴛɪᴏɴ
└ /help : ʜᴇʟᴘ ʀᴇʟᴀᴛᴇᴅ ʙᴏᴛ

🌸 sɪᴍᴘʟʏ ᴄʟɪᴄᴋ ᴏɴ ʟɪɴᴋ ᴀɴᴅ sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ ᴊᴏɪɴ ʙᴏᴛʜ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ ᴛʜᴀᴛs ɪᴛ.....!

🏮 ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ <a href=https://t.me/anixzone>ᴀʟᴏɴᴇᴋɪɴɢsᴛᴀʀ77</a></blockquote></b>"""

ADMIN_HELP_TXT = """<b><blockquote>⛩️ ᴀᴅᴍɪɴ ᴄᴏᴍᴍᴀɴᴅs

❏ ʟɪɴᴋ ɢᴇɴᴇʀᴀᴛɪᴏɴ
├ /genlink : ɢᴇɴᴇʀᴀᴛᴇ sɪɴɢʟᴇ ʟɪɴᴋ
├ /batch : ɢᴇɴᴇʀᴀᴛᴇ ʙᴀᴛᴄʜ ʟɪɴᴋ
└ /custom_batch : ɢᴇɴᴇʀᴀᴛᴇ ᴄᴜsᴛᴏᴍ ʙᴀᴛᴄʜ

❏ ᴜsᴇʀ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ
├ /ban : ʙᴀɴ ᴀ ᴜsᴇʀ
├ /unban : ᴜɴʙᴀɴ ᴀ ᴜsᴇʀ
└ /users : sʜᴏᴡ ᴀʟʟ ᴜsᴇʀs

❏ ʙʀᴏᴀᴅᴄᴀsᴛ
└ /broadcast : sᴇɴᴅ ᴍᴇssᴀɢᴇ ᴛᴏ ᴀʟʟ ᴜsᴇʀs

🏮 ᴘᴏᴡᴇʀᴇᴅ ʙʏ <a href=https://t.me/anixzone>ᴀʟᴏɴᴇᴋɪɴɢsᴛᴀʀ77</a></blockquote></b>"""

CMD_TXT = """<b><blockquote>⛩️ ᴀᴅᴍɪɴ ᴄᴏᴍᴍᴀɴᴅs ʟɪsᴛ

❏ ᴜsᴇʀ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ
├ /ban : ʙᴀɴ ᴀ ᴜsᴇʀ
├ /unban : ᴜɴʙᴀɴ ᴀ ᴜsᴇʀ
├ /users : sʜᴏᴡ ᴀʟʟ ᴜsᴇʀs
└ /premium_users : sʜᴏᴡ ᴀʟʟ ᴘʀᴇᴍɪᴜᴍ ᴜsᴇʀs

❏ ʟɪɴᴋ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ
├ /addchnl : ᴀᴅᴅ ғsᴜʙ ᴄʜᴀɴɴᴇʟ
├ /delchnl : ᴅᴇʟᴇᴛᴇ ғsᴜʙ ᴄʜᴀɴɴᴇʟ
├ /listchnl : ʟɪsᴛ ᴀʟʟ ᴄʜᴀɴɴᴇʟs
├ /fsub_mode : ᴛᴏɢɢʟᴇ ʀᴇǫᴜᴇsᴛ ᴍᴏᴅᴇ
├ /genlink : ɢᴇɴᴇʀᴀᴛᴇ sɪɴɢʟᴇ ʟɪɴᴋ
├ /batch : ɢᴇɴᴇʀᴀᴛᴇ ʙᴀᴛᴄʜ ʟɪɴᴋ
└ /custom_batch : ɢᴇɴᴇʀᴀᴛᴇ ᴄᴜsᴛᴏᴍ ʙᴀᴛᴄʜ

❏ sʏsᴛᴇᴍ
├ /stats : sʜᴏᴡ ʙᴏᴛ sᴛᴀᴛs
├ /broadcast : sᴇɴᴅ ᴍᴇssᴀɢᴇ ᴛᴏ ᴀʟʟ
└ /addpremium : ᴀᴅᴅ ᴘʀᴇᴍɪᴜᴍ ᴜsᴇʀ

🏮 ᴘᴏᴡᴇʀᴇᴅ ʙʏ <a href=https://t.me/anixzone>ᴀʟᴏɴᴇᴋɪɴɢsᴛᴀʀ77</a></blockquote></b>"""

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
