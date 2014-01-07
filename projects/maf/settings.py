# Initialize App Engine and import the default settings (DB backend, etc.).
# If you want to use a different backend you have to remove all occurences
# of "djangoappengine" from this file.
import sys

for p in ['lib']:   #  ,'lib/openid', 'lib/oauth2', 'lib/httplib2', 'lib/social_auth'
    sys.path.insert(0, p)

from djangoappengine.settings_base import *

import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

ADMIN_USERS = ['arturo@magicangel.org'] #, 'rosegpeterson@gmail.com']
CMS_EMAIL = ['cms@magicangel.org']

# Activate django-dbindexer for the default database
DATABASES['native'] = DATABASES['default']
DATABASES['default'] = {'ENGINE': 'dbindexer', 'TARGET': 'native'}
AUTOLOAD_SITECONF = 'indexes'

SECRET_KEY = '=r-$b*8hglm+858&9t043hlm6-&6-3d3vfc4((7yd0dbrakhvi'

ALLOWED_HOSTS = ['www.magicangel.org','magicangel.org']

INSTALLED_APPS = (
#    'django.contrib.admin',
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
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
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


import access_keys
SOCIAL_AUTH_TWITTER_KEY = access_keys.IP_TWEET_KEY
SOCIAL_AUTH_TWITTER_SECRET = access_keys.IP_TWEET_SECRET
SOCIAL_AUTH_FACEBOOK_KEY = access_keys.IP_FACEBOOK_KEY
SOCIAL_AUTH_FACEBOOK_SECRET = access_keys.IP_FACEBOOK_SECRET

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = access_keys.IP_GOOGLE_KEY
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = access_keys.IP_GOOGLE_SECRET


FLICKR_API_KEY = access_keys.FLICKR_KEY
FLICKR_API_SECRET = access_keys.FLICKR_SEC
PICASA_KEY = access_keys.PICASA_EMAIL
PICASA_PASSWORD = access_keys.PICASA_PASSWORD


AUTH_PROFILE_MODULE = 'users.models.UserProfile'



FILE_UPLOAD_TEMP_DIR = '/tmp'
# Add to your settings file
CONTENT_TYPES = ['image', 'video']
FILE_UPLOAD_MAX_MEMORY_SIZE = 7621440


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

APP_NAME = 'interpegasus-cms'
# APP_NAME = 'interpegasuslove'
TEMPLATE_FRONTPAGE = 'template/'+APP_NAME+'/template-frontpage.html'
TEMPLATE_PAGE = 'template/'+APP_NAME+'/template-page.html'


