from google.appengine.api import memcache
from pages.api import *
from django.conf import settings
import logging
logger = logging.getLogger(__name__)

# ...
def categories(request):
    # Get Request Language
    request_language = get_request_language(request)["request_language"]
    # Get Languages
    languages =  query_api(request_language, 'languages')
    # Get Categories
    categories = query_api(request_language, 'categories')
    pages = []
    if categories and 'categories' in categories:
        for c in categories["categories"]:
            pages = []
            if c["parent"] is None:
                pages_in_c = query_api(request_language, 'pages', {'category_slug': c["slug"]})
                try:
                    for p in pages_in_c["pages"]:
                        pages.append(p)
                except:
                    logger.error('context_processors/categories')
                c["page_array"] = pages
        categories = categories["categories"]
    return {'categories': categories,  'languages': languages, 'pages': pages, 'request_language':request_language, 'template_frontpage': settings.TEMPLATE_FRONTPAGE, 'template_page': settings.TEMPLATE_PAGE,'template_admin': settings.ADMIN_PAGE, 'api_page': settings.TEMPLATE_API}

# ...
def is_logged_in(request):
    try:
        if request.user.is_authenticated():
            return {'is_logged_in': True}
    except:
        logger.error('context_processors/is_logged_in')
        return {'is_logged_in': False}
    return {'is_logged_in': False}

# ...
def is_admin(request):
    if hasattr(request.user, 'email'):
        if request.user.email in settings.ADMIN_USERS_EMAILS:
            return {'is_admin': True}
    return {'is_admin': False}

# ...
def get_request_language(request):
    language_code = str(request.path)[1:3]
    if language_code in ('en','es','fr','de','pt','ru','iw','zh'):
        return {'request_language': language_code}
    else:
        return {'request_language': 'en'}

def app_name(request):
    return {'app_name': settings.APP_NAME}
