# settings.py

import sys
import access_keys

for p in ['lib']:
    sys.path.insert(0, p)

from djangoappengine.settings_base import *

import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DEBUG = False
ADMIN_USERS = access_keys.ADMIN_USERS
ADMIN_USERS_EMAILS = access_keys.ADMIN_USERS_EMAILS
SERVER_EMAIL = access_keys.SERVER_EMAIL

# Activate django-dbindexer for the default database
DATABASES['native'] = DATABASES['default']
DATABASES['default'] = {'ENGINE': 'dbindexer', 'TARGET': 'native'}
AUTOLOAD_SITECONF = 'indexes'

SECRET_KEY = '=r-$b*8hglm+858&9t043hlm6-&6-3d3vfc4((7yd0dbrakhvi'

ALLOWED_HOSTS = ['127.0.0.1','www.magicangel.org','magicangel.org','www.interpegasus.com','interpegasus.com', 'nrwl.org', 'www.nrwl.org', 'yiyask.com', 'www.yiyask.com', '1.happy-planet.appspot.com', 'happy-planet.appspot.com', 'arturo.interpegasus.com','bible-love.appspot.com','bible7.co', 'www.bible7.co', 'portfolio.interpegasus.com']

INSTALLED_APPS = (
#   'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.sessions',
    'djangotoolbox',
    'autoload',
    'dbindexer',
    'django.contrib.admin',
    'social.apps.django_app.default',
    'users',
    'pages',
    # djangoappengine should come last, so it can override a few manage.py commands
    'djangoappengine',
)

ACCOUNT_ACTIVATION_DAYS = 7 # One-week activation window; you may, of course, use a different value.

# CACHE_BACKEND = 'memcached://?timeout=0'

MIDDLEWARE_CLASSES = (
    # This loads the index definitions, so it has to come first
    'autoload.middleware.AutoloadMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # 'django.middleware.cache.UpdateCacheMiddleware',
    # 'django.middleware.cache.FetchFromCacheMiddleware',
)

# CACHE_MIDDLEWARE_SECONDS=60*60*24*7

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'pages.context_processors.categories',
    'pages.context_processors.is_logged_in',
    'pages.context_processors.is_admin',
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

FILE_UPLOAD_HANDLERS = (
    "django.core.files.uploadhandler.MemoryFileUploadHandler",
)

TEST_RUNNER = 'djangotoolbox.test.CapturingTestSuiteRunner'

ADMIN_MEDIA_PREFIX = '/media/admin/'
TEMPLATE_DIRS = (os.path.join(os.path.dirname(__file__), 'templates'),)

ROOT_URLCONF = 'urls'

STATIC_ROOT = os.path.join(os.path.dirname(__file__), 'static')
MEDIA_ROOT = '/tmp'
STATICFILES_DIRS = (
    os.path.join(os.path.dirname(__file__), 'static'),
)
STATIC_URL = '/static/'
MEDIA_URL = '/static/'

# Keys
SOCIAL_AUTH_TWITTER_KEY = access_keys.IP_TWEET_KEY
SOCIAL_AUTH_TWITTER_SECRET = access_keys.IP_TWEET_SECRET
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = access_keys.IP_GOOGLE_KEY
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = access_keys.IP_GOOGLE_SECRET
FLICKR_API_KEY = access_keys.FLICKR_KEY
FLICKR_API_SECRET = access_keys.FLICKR_SEC
PICASA_KEY = access_keys.PICASA_EMAIL
PICASA_PASSWORD = access_keys.PICASA_PASSWORD
API_ACCESS_TOKEN = access_keys.API_ACCESS_TOKEN
API_ACCESS_TOKEN_1 = access_keys.API_ACCESS_TOKEN_1

NRWL_TWEET_KEY = access_keys.NRWL_TWEET_KEY
NRWL_TWEET_SECRET = access_keys.NRWL_TWEET_SECRET
NRWL_ACCESS_TOKEN = access_keys.NRWL_ACCESS_TOKEN
NRWL_ACCESS_SECRET = access_keys.NRWL_ACCESS_SECRET

AUTH_PROFILE_MODULE = 'users.models.UserProfile'

FILE_UPLOAD_TEMP_DIR = '/tmp'
# Add to your settings file
CONTENT_TYPES = ['image', 'video']
FILE_UPLOAD_MAX_MEMORY_SIZE = 35000000

EMAIL_BACKEND = 'djangoappengine.mail.EmailBackend'

AUTHENTICATION_BACKENDS = (
    'social.backends.facebook.FacebookOAuth2',
    'social.backends.google.GoogleOAuth',
    'social.backends.google.GoogleOAuth2',
    'social.backends.google.GoogleOpenId',
    'social.backends.google.GooglePlusAuth',
    'social.backends.twitter.TwitterOAuth',
    'social.backends.email.EmailAuth',
    'social.backends.username.UsernameAuth',
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details',
    #'social.pipeline.picture.save_profile_picture',
)

LOGIN_REDIRECT_URL = '/'

# apps
#APP_NAME = 'arturoportfolio7'
#APP_NAME = 'arturopegasus7'
#APP_NAME = 'happy-planet'
#APP_NAME = 'bible-love'
#APP_NAME = 'yiyask7'
#APP_NAME = 'interpegasus-cms'
APP_NAME = 'interpegasuslove'


CACHE_ENABLED = True

if True:
    SITE_URL = 'http://127.0.0.1:8080'
elif APP_NAME == 'interpegasus-cms':
    SITE_URL = 'http://www.magicangel.org'
    SOCIAL_AUTH_FACEBOOK_KEY = access_keys.MAF_FACEBOOK_KEY
    SOCIAL_AUTH_FACEBOOK_SECRET = access_keys.MAF_FACEBOOK_SECRET
elif APP_NAME == 'interpegasuslove':
    SITE_URL = 'http://www.interpegasus.com'
    SOCIAL_AUTH_FACEBOOK_KEY = access_keys.IP_FACEBOOK_KEY
    SOCIAL_AUTH_FACEBOOK_SECRET = access_keys.IP_FACEBOOK_SECRET
elif APP_NAME == 'happy-planet':
    SITE_URL = 'http://www.nrwl.org'
    SOCIAL_AUTH_FACEBOOK_KEY = access_keys.NRWL_FACEBOOK_KEY
    SOCIAL_AUTH_FACEBOOK_SECRET = access_keys.NRWL_FACEBOOK_SECRET
elif APP_NAME == 'arturopegasus7':
    SITE_URL = 'http://arturo.interpegasus.com'
    SOCIAL_AUTH_FACEBOOK_KEY = access_keys.AG_FACEBOOK_KEY
    SOCIAL_AUTH_FACEBOOK_SECRET = access_keys.AG_FACEBOOK_SECRET
elif APP_NAME == 'arturoportfolio7':
    SITE_URL = 'http://portfolio.interpegasus.com'
    SOCIAL_AUTH_FACEBOOK_KEY = access_keys.PORTFOLIO_FACEBOOK_KEY
    SOCIAL_AUTH_FACEBOOK_SECRET = access_keys.PORTFOLIO_FACEBOOK_SECRET
elif APP_NAME == 'bible-love':
    SITE_URL = 'http://bible7.co'
    SOCIAL_AUTH_FACEBOOK_KEY = access_keys.BIBLE_FACEBOOK_KEY
    SOCIAL_AUTH_FACEBOOK_SECRET = access_keys.BIBLE_FACEBOOK_SECRET
elif APP_NAME == 'yiyask7':
    SITE_URL = 'http://www.yiyask.com'
    SOCIAL_AUTH_FACEBOOK_KEY = access_keys.YIYASK_FACEBOOK_KEY
    SOCIAL_AUTH_FACEBOOK_SECRET = access_keys.YIYASK_FACEBOOK_SECRET

# templates
TEMPLATE_FRONTPAGE = 'template/'+APP_NAME+'/template-frontpage.html'
TEMPLATE_PAGE = 'template/'+APP_NAME+'/template-page.html'
ADMIN_PAGE = 'template/'+APP_NAME+'/template-admin.html'
TEMPLATE_API = 'template/template-api.html'

#session
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
SESSION_COOKIE_AGE = 2592000

# DBT
DBT_KEY = access_keys.DBT_KEY
DBT_LANGUAGE_TEXT_URL  = access_keys.DBT_LANGUAGE_TEXT_URL
DBT_LANGUAGE_AUDIO_URL = access_keys.DBT_LANGUAGE_AUDIO_URL
DBT_LANGUAGE_VIDEO_URL = access_keys.DBT_LANGUAGE_VIDEO_URL
DBT_GET_BIBLES_FOR_LANGUAGE_URL = access_keys.DBT_GET_BIBLES_FOR_LANGUAGE_URL
DBT_GET_BIBLE_BOOKS_URL =  access_keys.DBT_GET_BIBLE_BOOKS_URL
DBT_GET_BIBLE_BOOKS_TEXT_URL =  access_keys.DBT_GET_BIBLE_BOOKS_TEXT_URL
DBT_GET_COPYRIGHT_URL = access_keys.DBT_GET_COPYRIGHT_URL

CAPTCHA_SITE_KEY = access_keys.CAPTCHA_SITE_KEY
CAPTCHA_SITE_SECRET = access_keys.CAPTCHA_SITE_SECRET

LOGGING = {
    'version': 1,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
            }
        },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
            },
        }
    }

LOG_TO_CONSOLE = True