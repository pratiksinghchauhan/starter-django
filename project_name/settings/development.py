# Python imports
from os.path import join

# project imports
from .common import *

# uncomment the following line to include i18n
# from .i18n import *


# ##### DEBUG CONFIGURATION ###############################
DEBUG = True

# allow all hosts during development
ALLOWED_HOSTS = ["*"]

# adjust the minimal login
LOGIN_URL = "/admin"
LOGIN_REDIRECT_URL = "/swagger"
LOGOUT_REDIRECT_URL = "/swagger"

# ##### DATABASE CONFIGURATION ############################
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": join(PROJECT_ROOT, "run", "dev.sqlite3"),
    }
}

# ##### APPLICATION CONFIGURATION #########################

INSTALLED_APPS = DEFAULT_APPS + THIRD_PARTY_APPS + CUSTOM_APPS
