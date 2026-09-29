import re
import os
from os import environ, getenv
from Script import script

id_pattern = re.compile(r'^.\d+$')

def is_enabled(value, default):
    if isinstance(value, bool):
        return value
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Helper function to safely parse integer environment variables
def get_int(key, default="0"):
    val = environ.get(key, "").strip()
    return int(val) if val and val.lstrip('-').isdigit() else int(default)

# Basic Bot Setup
SESSION = environ.get('SESSION', 'AvijitBots')
API_ID = get_int('API_ID', '35520490')
API_HASH = environ.get('API_HASH', '0ab53ccb53a79b22bb7b7b6eeadd9582')
BOT_TOKEN = environ.get('BOT_TOKEN', "8666124094:AAG1e1H8Zu87RgSpSTCUlu-XRJEqPIoQLEQ")

# UI & Customization Features
USE_CAPTION_FILTER = is_enabled(environ.get('USE_CAPTION_FILTER', "False"), False)
INDEX_CAPTION = is_enabled(environ.get('INDEX_CAPTION', "False"), False)
COVER = is_enabled(environ.get('COVER', "False"), False)
PICS = (environ.get('PICS', 'https://i.ibb.co/PzZNZHF6/IMG-20251116-113905-254.jpg https://i.ibb.co/8npWSZ5T/pic.jpg')).split()
MELCOW_PHOTO = environ.get("MELCOW_PHOTO", "https://i.ibb.co/2769f1rF/photo-2025-09-03-14-48-34-7548400762112442372.jpg")

# Channels & User IDs
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '5445462039').split() if admin]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '').split() if ch]
LOG_CHANNEL = get_int('LOG_CHANNEL', '-1003944220009')
BIN_CHANNEL = get_int('BIN_CHANNEL', '-1003944220009')
PREMIUM_LOGS = get_int('PREMIUM_LOGS', '0')
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '').split() if dch]
AUTH_CHANNELS = [int(ch) for ch in environ.get("AUTH_CHANNELS", "").split() if ch and id_pattern.match(ch)]
AUTH_REQ_CHANNELS = [int(ch) for ch in environ.get("AUTH_REQ_CHANNELS", "").split() if ch and id_pattern.match(ch)]
REQST_CHANNEL = get_int("REQST_CHANNEL", "0") or None
SUPPORT_CHAT_ID = get_int("SUPPORT_CHAT_ID", "0") or None

OWNER = get_int("OWNER", "5445462039")
CHANNEL_LINK = environ.get('CHANNEL_LINK', 'https://telegram.me/AvijitBots')
GROUP_LINK = environ.get('GROUP_LINK', 'https://telegram.me/AvijitSupport')

# Database Configuration
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://ankksnzbbz_db_user:YFKdRf9noFXdOGRn@cluster0.wqdijao.mongodb.net/?authSource=admin&retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "rdxbb")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'files')
MULTIPLE_DB = is_enabled(os.environ.get('MULTIPLE_DB', "False"), False)
DATABASE_URI2 = environ.get('DATABASE_URI2', "")

# Notifications & Previews
UPDATE_NOTIFICATION = is_enabled(environ.get('UPDATE_NOTIFICATION', "False"), False)
UPDATE_CHANNEL = get_int('UPDATE_CHANNEL', '0')
IMAGE_FETCH = is_enabled(environ.get('IMAGE_FETCH', "True"), True)
LINK_PREVIEW = is_enabled(environ.get('LINK_PREVIEW', "False"), False)
ABOVE_PREVIEW = is_enabled(environ.get('ABOVE_PREVIEW', "False"), False)
TMDB_API_KEY = environ.get('TMDB_API_KEY', '')
TMDB_POSTER = is_enabled(environ.get('TMDB_POSTER', "True"), True)
LANDSCAPE_POSTER = is_enabled(environ.get('LANDSCAPE_POSTER', "True"), True)

# Verification & Shorteners
IS_VERIFY = is_enabled(environ.get('IS_VERIFY', 'True'), True)
LOG_API_CHANNEL = get_int('LOG_API_CHANNEL', '0')
VERIFY_IMG = environ.get("VERIFY_IMG", "https://i.ibb.co/xqNtSMpS/photo-2025-09-18-15-24-38-7551450511015149572.jpg")
TUTORIAL = environ.get("TUTORIAL", "https://t.me/AvijitBots")
TUTORIAL_2 = environ.get("TUTORIAL_2", "https://t.me/AvijitBots")
TUTORIAL_3 = environ.get("TUTORIAL_3", "https://t.me/AvijitBots")
SHORTENER_API = environ.get("SHORTENER_API", "282d796bc699baed4333f8724d3ff8c5f8cc5937")
SHORTENER_WEBSITE = environ.get("SHORTENER_WEBSITE", "teraboxlinks.com")
SHORTENER_API2 = environ.get("SHORTENER_API2", "282d796bc699baed4333f8724d3ff8c5f8cc5937")
SHORTENER_WEBSITE2 = environ.get("SHORTENER_WEBSITE2", "teraboxlinks.com")
SHORTENER_API3 = environ.get("SHORTENER_API3", "282d796bc699baed4333f8724d3ff8c5f8cc5937")
SHORTENER_WEBSITE3 = environ.get("SHORTENER_WEBSITE3", "teraboxlinks.com")
TWO_VERIFY_GAP = get_int('TWO_VERIFY_GAP', "1200")
THREE_VERIFY_GAP = get_int('THREE_VERIFY_GAP', "54000")

# Bot Behaviors & Toggles
FAST_MODE = is_enabled(environ.get('FAST_MODE', "False"), False)
MAX_BTN = is_enabled((environ.get('MAX_BTN', "True")), True)
MAX_BTNS = environ.get("MAX_BTNS", "5")
MSG_ALRT = environ.get('MSG_ALRT', '𝖲𝗁𝖺𝗋𝖾 & 𝖲𝗎𝗉𝗉𝗈𝗋𝗍 𝖬𝖾 ♥️')
DELETE_TIME = get_int("DELETE_TIME", "300")
FILE_CAPTION = environ.get("FILE_CAPTION", f"{script.CAPTION}")
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
MAX_LIST_ELM = get_int("MAX_LIST_ELM", "10") or None
NO_RESULTS_MSG = is_enabled(environ.get("NO_RESULTS_MSG", "True"), True)
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), False)
IMDB = is_enabled((environ.get('IMDB', "False")), False)
TMDB_ON_SEARCH = is_enabled((environ.get('TMDB_ON_SEARCH', "False")), False)
AUTO_FILTER = is_enabled((environ.get('AUTO_FILTER', "True")), True)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "False")), False)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PM_SEARCH = is_enabled(environ.get('PM_SEARCH', 'False'), False)
EMOJI_MODE = is_enabled(environ.get('EMOJI_MODE', 'True'), True)
BUTTON_MODE = is_enabled((environ.get('BUTTON_MODE', "True")), True)
STREAM_MODE = is_enabled(environ.get('STREAM_MODE', 'True'), True)
PREMIUM_STREAM_MODE = is_enabled(environ.get('PREMIUM_STREAM_MODE', 'False'), False)
MAINTENANCE = is_enabled(environ.get('MAINTENANCE', "False"), False)

LANGUAGES = {"ᴛᴀᴍɪʟ":"tam","ᴛᴇʟᴜɢᴜ":"tel","ᴇɴɢʟɪsʜ":"eng","ʜɪɴᴅɪ":"hin","ᴊᴀᴘᴀɴᴇsᴇ":"jap"}
QUALITIES = ["360P", "480P", "720P", "1080P", "2160p"]
SEASON_COUNT = 12
SEASONS = [f"S{str(i).zfill(2)}" for i in range(1, SEASON_COUNT + 1)]
REACTIONS = ["🤝", "😇", "🤗", "😍", "👍", "🎅", "😐", "🥰", "🤩", "😱", "🤣", "😘", "👏", "😛", "😈", "🎉", "⚡️", "🫡", "🤓", "😎", "🏆", "🔥", "🤭", "🌚", "🆒", "👻", "😁"]
STAR_PREMIUM_PLANS = {10: "7day", 20: "15day", 40: "1month", 55: "45day", 75: "60day"}
BAD_WORDS = {"PrivateMovieZ", "toonworld4all", "themoviesboss", "1tamilmv", "tamilblasters", "1tamilblasters", "skymovieshd", "extraflix", "hdm2", "moviesmod", "hdhub4u", "mkvcinemas", "primefix", "join", "www", "villa", "tg", "original"}

IS_FILE_LIMIT = is_enabled(environ.get('IS_FILE_LIMIT', 'True'), True)
FILES_LIMIT = get_int("FILES_LIMIT", "48")
QUALITY_LIMIT = is_enabled(environ.get('QUALITY_LIMIT', 'False'), False)
FREE_QUALITIES = ["360p", "480p"]

PORT = get_int("PORT", "8080")
NO_PORT = is_enabled(environ.get('NO_PORT', 'False'), False)
APP_NAME = None
if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = environ.get('APP_NAME')
else:
    ON_HEROKU = False

BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', 'alyafilterbot.onrender.com'))
FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
SLEEP_THRESHOLD = get_int('SLEEP_THRESHOLD', '60')
MULTI_CLIENT = False
PING_INTERVAL = get_int("PING_INTERVAL", "1200")

HAS_SSL = is_enabled(getenv('HAS_SSL', 'True'), True)
if HAS_SSL:
    URL = "https://{}/".format(FQDN)
else:
    URL = "http://{}/".format(FQDN)

if not MULTIPLE_DB:
    DATABASE_URI2 = DATABASE_URI

LOG_STR = "Current Customized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for your queries.\n" if IMDB else "IMDB Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found, Users will be redirected to send /start to Bot PM instead of sending file directly.\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled, files will be sent in PM instead of starting the bot.\n")
LOG_STR += ("BUTTON_MODE is found, filename and file size will be shown in a single button instead of two separate buttons.\n" if BUTTON_MODE else "BUTTON_MODE is disabled, filename and file size will be shown as different buttons.\n")
LOG_STR += (f"FILE_CAPTION enabled with value {FILE_CAPTION}, your files will be sent along with this customized caption.\n" if FILE_CAPTION else "No FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled, Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode is enabled, bot will be suggesting related movies if movie name is misspelled.\n" if SPELL_CHECK_REPLY else "Spell Check Mode is disabled.\n")
