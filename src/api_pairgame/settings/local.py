"""Development settings."""

import os

from .base import *

# Base
DEBUG = os.environ['DEBUG'].lower() in ("yes", "true", "t", "1")

# Security
SECRET_KEY = os.environ['SECRET_KEY']
ALLOWED_HOSTS = [
    "localhost",
    "0.0.0.0",
    "127.0.0.1",
]

# Cache
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': ''
    }
}
