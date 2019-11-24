"""Development settings."""

import os

from celery.schedules import crontab

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

# Celery
CELERY_BROKER_URL = os.environ["REDIS_URL"]
CELERY_RESULT_BACKEND = os.environ["REDIS_URL"]
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ENABLE_UTC = False
CELERY_TIMEZONE = 'America/Bogota'
CELERY_BEAT_SCHEDULE = {
    'scraping': {
        'task': 'worlds.tasks.scraping',
        # 'schedule': crontab(hour=23, minute=58, day_of_week='mon')
        'schedule': crontab()
    }
}
