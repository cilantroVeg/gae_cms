# Initialize App Engine and import the default settings (DB backend, etc.).
# If you want to use a different backend you have to remove all occurences
# of "djangoappengine" from this file.
import sys
for p in ['lib']:   #  ,'lib/openid', 'lib/oauth2', 'lib/httplib2', 'lib/social_auth'
    sys.path.insert(0, p)

from djangoappengine.settings_base import *

import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

ADMIN_USERS = ['arturo@magicangel.org', 'rosegpeterson@gmail.com']
CMS_EMAIL = ['cms@magicangel.org']

# Activate django-dbindexer for the default database
DATABASES['native'] = DATABASES['default']
DATABASES['default'] = {'ENGINE': 'dbindexer', 'TARGET': 'native'}
AUTOLOAD_SITECONF = 'indexes'

SECRET_KEY = '=r-$b*8hglm+858&9t043hlm6-&6-3d3vfc4((7yd0dbrakhvi'

INSTALLED_APPS = (
#    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.sessions',
    'djangotoolbox',
    'autoload',
    'dbindexer',
    'django.contrib.admin',
    'users',
    'social_auth',
    'pages',
    # djangoappengine should come last, so it can override a few manage.py commands
    'djangoappengine',
)



ACCOUNT_ACTIVATION_DAYS = 7 # One-week activation window; you may, of course, use a different value.

MIDDLEWARE_CLASSES = (
    # This loads the index definitions, so it has to come first
    'autoload.middleware.AutoloadMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'pages.context_processors.categories',
    'pages.context_processors.is_logged_in',
    'pages.context_processors.is_admin',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #     'django.template.loaders.eggs.Loader',
)

FILE_UPLOAD_HANDLERS = (
    "django.core.files.uploadhandler.MemoryFileUploadHandler",
)

# This test runner captures stdout and associates tracebacks with their
# corresponding output. Helps a lot with print-debugging.
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



AUTHENTICATION_BACKENDS = (
    'social_auth.backends.twitter.TwitterBackend',
    'social_auth.backends.facebook.FacebookBackend',
    'social_auth.backends.google.GoogleOAuthBackend',
    'social_auth.backends.google.GoogleOAuth2Backend',
    'social_auth.backends.google.GoogleBackend',
    'social_auth.backends.yahoo.YahooBackend',
    'django.contrib.auth.backends.ModelBackend',
)

import access_keys
TWITTER_CONSUMER_KEY         = access_keys.IP_TWEET_KEY
TWITTER_CONSUMER_SECRET      = access_keys.IP_TWEET_SECRET
FACEBOOK_APP_ID              = access_keys.IP_FACEBOOK_KEY
FACEBOOK_API_SECRET          = access_keys.IP_FACEBOOK_SECRET
GOOGLE_CONSUMER_KEY          = ''
GOOGLE_CONSUMER_SECRET       = ''
GOOGLE_OAUTH2_CLIENT_ID      = ''
GOOGLE_OAUTH2_CLIENT_SECRET  = ''
FLICKR_API_KEY = access_keys.FLICKR_KEY
FLICKR_API_SECRET = access_keys.FLICKR_SEC
PICASA_KEY = access_keys.PICASA_EMAIL
PICASA_PASSWORD = access_keys.PICASA_PASSWORD


LOGIN_URL          = '/enter/'
LOGIN_REDIRECT_URL = '/logged-in/'
LOGIN_ERROR_URL    = '/login-error/'
SOCIAL_AUTH_BACKEND_ERROR_URL = '/login-error/'

SOCIAL_AUTH_NEW_USER_REDIRECT_URL = '/logged-in/'
SOCIAL_AUTH_NEW_ASSOCIATION_REDIRECT_URL = '/logged-in/'
SOCIAL_AUTH_USERNAME_IS_FULL_EMAIL = True
SOCIAL_AUTH_SESSION_EXPIRATION = False
SOCIAL_AUTH_RAISE_EXCEPTIONS = False

FACEBOOK_EXTENDED_PERMISSIONS = ['email']


AUTH_PROFILE_MODULE = 'users.models.UserProfile'


SOCIAL_AUTH_PIPELINE = (
    'social_auth.backends.pipeline.social.social_auth_user',
    'social_auth.backends.pipeline.associate.associate_by_email',
    'social_auth.backends.pipeline.user.get_username',
    'social_auth.backends.pipeline.user.create_user',
    'social_auth.backends.pipeline.social.associate_user',
    'social_auth.backends.pipeline.user.update_user_details',
)

FILE_UPLOAD_TEMP_DIR = '/tmp'
# Add to your settings file
CONTENT_TYPES = ['image', 'video']
FILE_UPLOAD_MAX_MEMORY_SIZE = 7621440


EMAIL_BACKEND = 'djangoappengine.mail.EmailBackend'