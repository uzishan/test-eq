# common settings
try:
    from .common import *
except ImportError:
    print "Couldn't import settings.common"

DATABASES['default'] = dj_database_url.config()
