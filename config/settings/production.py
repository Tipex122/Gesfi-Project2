from .base import *

ALLOWED_HOSTS = []

DEBUG = env.bool('DJANGO_DEBUG', default=False)

