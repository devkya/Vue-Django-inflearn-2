from .base import *


SECRET_KEY = 'django-insecure-%ybg80g#_%8xlx0aj-k1cv3c&#%5-w)2@^md48foi%)7tpc_+='

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': { 
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}