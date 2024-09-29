import re
import logging
from os import environ
from Script import script

def is_enabled(setting, default):
    data = environ.get(setting, str(default))
    if data.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif data.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        print(f"Error - {setting} is invalid, exiting now")
        exit()

def is_valid_ip(ip):
    ip_pattern = r'\b(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b'
    return re.match(ip_pattern, ip) is not None

def get_env_or_exit(var_name, default=None):
    value = environ.get(var_name, default)
    if not value:
        print(f"Error - {var_name} is missing, exiting now")
        exit()
    return value

# Bot Information
API_ID = int(get_env_or_exit('API_ID', '27002519'))
API_HASH = get_env_or_exit('API_HASH', '1033ee721101d78366b4ac46aadf3930')
BOT_TOKEN = get_env_or_exit('BOT_TOKEN')
PORT = int(environ.get('PORT', '80'))

# Bot Pics
PICS = environ.get('PICS', 'https://i.postimg.cc/prXPRvsh/IXPs2c-Wx-Tt2-Ep-A5-Dcr6-QQ.webp').split()

# Bot Admins
ADMINS = [int(admin) for admin in get_env_or_exit('ADMINS', '6174868004').split()]

# Channels
INDEX_CHANNELS = [int(ch) if ch.startswith("-") else ch for ch in environ.get('INDEX_CHANNELS', '-1002208295766 -1002233820213 -1002227944470 -1002185234412').split()]
AUTH_CHANNEL = [int(ch) for ch in environ.get('AUTH_CHANNEL', '-1002233212878').split()]
LOG_CHANNEL = int(get_env_or_exit('LOG_CHANNEL', '-1002183671823'))

IS_FSUB = is_enabled('IS_FSUB', True)

# Support group
SUPPORT_GROUP = int(get_env_or_exit('SUPPORT_GROUP', '-1002155777503'))

# MongoDB Information
DATABASE_URL = get_env_or_exit('DATABASE_URL', "mongodb+srv://ayushpritysingh098:z0aMVL9ofTSOGqir@cluster0.9r9gs.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = environ.get('DATABASE_NAME', 'Cluster0')
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Files')

# Links
SUPPORT_LINK = environ.get('SUPPORT_LINK', 'https://t.me/Netfilix_movie_shaport')
OWNER_USERNAME = environ.get('OWNER_USERNAME', 'https://t.me/Hansaka_Anuhas')
UPDATES_LINK = environ.get('UPDATES_LINK', 'https://t.me/+Ie4mNf6lL5RjYjM1')
FILMS_LINK = environ.get('FILMS_LINK', 'https://t.me/n_flixmovie')
TUTORIAL = environ.get('TUTORIAL', 'https://t.me/APSmo/7')
VERIFY_TUTORIAL = environ.get('VERIFY_TUTORIAL', '')

# Bot Settings
DELETE_TIME = int(environ.get('DELETE_TIME', 300))
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
MAX_BTN = int(environ.get('MAX_BTN', 10))
LANGUAGES = [lang.lower() for lang in environ.get('LANGUAGES', 'hindi english telugu tamil kannada malayalam marathi punjabi').split()]
QUALITY = [quality.lower() for quality in environ.get('QUALITY', '360p 480p 720p 1080p 2160p').split()]
IMDB_TEMPLATE = environ.get('IMDB_TEMPLATE', script.IMDB_TEMPLATE)
FILE_CAPTION = environ.get('FILE_CAPTION', script.FILE_CAPTION)
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'shortxlinks.com')
SHORTLINK_API = environ.get('SHORTLINK_API', 'fa2a0768fc8d2a51b22e46293634a52670a73c7a')
VERIFY_EXPIRE = int(environ.get('VERIFY_EXPIRE', 86400))
WELCOME_TEXT = environ.get('WELCOME_TEXT', script.WELCOME_TEXT)
PM_FILE_DELETE_TIME = int(environ.get('PM_FILE_DELETE_TIME', 3600))
INDEX_EXTENSIONS = [ext.lower() for ext in environ.get('INDEX_EXTENSIONS', 'mp4 mkv').split()]
STICKERS_IDS = environ.get('STICKERS_IDS', '🍌').split() # CAACAgUAAxkBAAJ-dGb5YVm8l-qU7K_awyk1a7lHEgmQAAIrCgADAWhU63GjQhJebuA2BA').split()

# Boolean Settings
GROUP_FSUB = is_enabled('GROUP_FSUB', False)
PM_SEARCH = is_enabled('PM_SEARCH', False)
IS_VERIFY = is_enabled('IS_VERIFY', False)
AUTO_DELETE = is_enabled('AUTO_DELETE', True)
WELCOME = is_enabled('WELCOME', False)
PROTECT_CONTENT = is_enabled('PROTECT_CONTENT', False)
LONG_IMDB_DESCRIPTION = is_enabled('LONG_IMDB_DESCRIPTION', False)
LINK_MODE = is_enabled('LINK_MODE', True)
AUTO_FILTER = is_enabled('AUTO_FILTER', True)
IMDB = is_enabled('IMDB', False)
SPELL_CHECK = is_enabled('SPELL_CHECK', True)
SHORTLINK = is_enabled('SHORTLINK', True)

# Premium Info
PAYMENT_QR = environ.get('PAYMENT_QR', 'https://i.postimg.cc/NFbZ4r7L/Google-Pay-QR-2.png')
OWNER_UPI_ID = environ.get('OWNER_UPI_ID', 'singhayush88805@okaxis')

# Stream Settings
IS_STREAM = is_enabled('IS_STREAM', True)
BIN_CHANNEL = int(get_env_or_exit('BIN_CHANNEL', '-1002237538640'))
URL = get_env_or_exit('URL', 'https://t.me/+kP4LSVcocBVhZjc1')

if URL.startswith(('https://', 'http://')):
    if not URL.endswith('/'):
        URL += '/'
elif is_valid_ip(URL):
    URL = f'http://{URL}/'
else:
    print('Error - URL is not valid, exiting now')
    exit()
