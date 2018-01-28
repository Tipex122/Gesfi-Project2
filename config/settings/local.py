from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-q-3k2u^qct2_u7%=l5=(t@vn&ouc&l*!e98^2ismxv@91*^u5'

DEBUG = env.bool('DJANGO_DEBUG', default=True)
