import platform

# Helper Functions
def load_version():
    try:
        with open('version.txt', 'r') as file:
            version = file.read()
            [ major, minor, micro ] = version.split('.')
            checksum = int(major) * 10000 + int(minor) * 100 + int(micro)
            return checksum 
    except Exception:
        return -1
        
# Popup Settings
POPUP_DURATION = 5
POPUP_AUTO_PLAY = True
POPUP_THEME = 'default'
POPUP_WIDTH = 400
POPUP_POSITION = (1, 1)
POPUP_TRANSPARENCY = 230
POPUP_TITLE_LENGTH = 120
POPUP_BODY_LENGTH = 400
POPUP_DISPLAY = 0

# Application Settings
APP_ID = 'FeedNotifier'
APP_NAME = 'Feed Notifier'
APP_VERSION = '2.3.1'
APP_URL = 'http://www.feednotifier.com/'
USER_AGENT = '%s/%s +%s' % (APP_ID, APP_VERSION, APP_URL)
DEFAULT_POLLING_INTERVAL = 60 * 15
USER_IDLE_TIMEOUT = 60
DISABLE_WHEN_IDLE = True
ITEM_CACHE_AGE = 60 * 60 * 24 * 1
FEED_CACHE_SIZE = 500
MAX_WORKER_THREADS = 10
PLAY_SOUND = True
SOUND_PATH = 'sounds/notification.wav'

# Initial Setup
DEFAULT_FEED_URLS = [
    'http://www.feednotifier.com/welcome.xml',
]

# Proxy Settings
USE_PROXY = False
PROXY_URL = ''

# Updater Settings
LOCAL_VERSION = load_version()
VERSION_URL = 'http://www.fbergeron.com/feednotifier/version.txt'
INSTALLER_URL = 'http://www.fbergeron.com/feednotifier/installer.exe'
if platform.system() == 'Windows': 
    CHECK_FOR_UPDATES = True
else:
    CHECK_FOR_UPDATES = False
UPDATE_INTERVAL = 60 * 60 * 24 * 1
UPDATE_TIMESTAMP = 0

del load_version

