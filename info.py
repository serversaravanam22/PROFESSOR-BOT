import re, time
from os import environ
from Script import script 
import os

id_pattern = re.compile(r'^.\d+$')

def is_enabled(value, default):
    if value.strip().lower() in ["on", "true", "yes", "1", "enable", "y"]: return True
    elif value.strip().lower() in ["off", "false", "no", "0", "disable", "n"]: return False
    else: return default


# PyroClient Setup 
SESSION = environ.get('SESSION', 'TechVJBot')
API_ID = int(environ.get('API_ID', '20902603'))
API_HASH = environ.get('API_HASH', '79e5caa103a9e9fb0183390b4800845d')
BOT_TOKEN = environ.get('BOT_TOKEN', "7807123947:AAE0_FLfTir6_UmuUGDCDZ2LF-WknnHfx8k")
# Bot settings
WEB_SUPPORT = bool(environ.get("WEBHOOK", 'True')) # for web support on/off
PICS = (environ.get('PICS' ,'https://graph.org/file/01ddfcb1e8203879a63d7.jpg https://graph.org/file/d69995d9846fd4ad632b8.jpg https://graph.org/file/a125497b6b85a1d774394.jpg https://graph.org/file/43d26c54d37f4afb830f7.jpg https://graph.org/file/60c1adffc7cc2015f771c.jpg https://graph.org/file/d7b520240b00b7f083a24.jpg https://graph.org/file/0f336b0402db3f2a20037.jpg https://graph.org/file/39cc4e15cad4519d8e932.jpg https://graph.org/file/d59a1108b1ed1c6c6c144.jpg https://te.legra.ph/file/3a4a79f8d5955e64cbb8e.jpg https://graph.org/file/d69995d9846fd4ad632b8.jpg')).split()
UPTIME = time.time()

# Admins, Channels & Users
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '6283322330').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1002473385674').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '6283322330').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information
DATABASE_URL = environ.get('DATABASE_URL', "mongodb+srv://ganeshganesh177:17032009@sasukeuchiha.k21bh.mongodb.net/?retryWrites=true&w=majority&appName=Sasukeuchiha")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
FILE_DB_URL = environ.get("FILE_DB_URL", DATABASE_URL)
FILE_DB_NAME = environ.get("FILE_DB_NAME", DATABASE_NAME)
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Filters Configuration 
MAX_RIST_BTNS = int(environ.get('MAX_RIST_BTNS', "10"))
START_MESSAGE = environ.get('START_MESSAGE', script.START_TXT)
BUTTON_LOCK_TEXT = environ.get("BUTTON_LOCK_TEXT", script.BUTTON_LOCK_TEXT)
FORCE_SUB_TEXT = environ.get('FORCE_SUB_TEXT', script.FORCE_SUB_TEXT)

WELCOM_PIC = environ.get("WELCOM_PIC", "")
WELCOM_TEXT = environ.get("WELCOM_TEXT", script.WELCOM_TEXT)
PMFILTER = is_enabled(environ.get('PMFILTER', "True"), True)
G_FILTER = is_enabled(environ.get("G_FILTER", "True"), True)
BUTTON_LOCK = is_enabled(environ.get("BUTTON_LOCK", "True"), True)
RemoveBG_API = environ.get("RemoveBG_API", "")

# url shortner
SHORT_URL = environ.get("SHORT_URL")
SHORT_API = environ.get("SHORT_API")

# Others
IMDB_DELET_TIME = int(environ.get('IMDB_DELET_TIME', "300"))
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', 0))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'MKN_BOTZ_DISCUSSION_GROUP')
P_TTI_SHOW_OFF = is_enabled(environ.get('P_TTI_SHOW_OFF', "True"), True)
PM_IMDB = is_enabled(environ.get('PM_IMDB', "True"), True)
IMDB = is_enabled(environ.get('IMDB', "True"), True)
SINGLE_BUTTON = is_enabled(environ.get('SINGLE_BUTTON', "True"), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "{file_name}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", None)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", script.IMDB_TEMPLATE)
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled(environ.get('MELCOW_NEW_USERS', "True"), True)
PROTECT_CONTENT = is_enabled(environ.get('PROTECT_CONTENT', "False"), False)
PUBLIC_FILE_STORE = is_enabled(environ.get('PUBLIC_FILE_STORE', "True"), True)
LOG_MSG = "{} Iꜱ Rᴇsᴛᴀʀᴛᴇᴅ....✨\n\n🗓️ Dᴀᴛᴇ : {}\n⏰ Tɪᴍᴇ : {}\n\n🖥️ Rᴇᴏᴩ: {}\n🉐 Vᴇʀsɪᴏɴ: {}\n🧾 Lɪᴄᴇɴꜱᴇ: {}\n©️ Cᴏᴩʏʀɪɢʜᴛ: {}"


#Newfeatures vars developer - Anshvachhani99 ✨🌸
DIRECT_GEN_DB = int(os.environ.get("DIRECT_GEN_DB", "-1002473385674"))
DIRECT_GEN_URL = os.environ.get("DIRECT_GEN_URL", "jeevanmoviessbot.koyeb.app/")
DIRECT_GEN = bool(DIRECT_GEN_DB and DIRECT_GEN_URL)
POST_MODE= bool(environ.get('POST_MODE', True))
POST_SHORT_API = environ.get('POST_SHORT_API', 'bcb93413e5dd9aaf092ab03269420e6f928aae2c')
POST_SHORT_URL = environ.get('POST_SHORT_URL', 'publicearn.com')
HOW_TO_POST_SHORT = environ.get('HOW_TO_POST_SHORT', 'https://t.me/How_To_Get_Movie')



