# common settings
try:
    from .common import *
except ImportError:
    print "Couldn't import settings.common"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase',
    }
}