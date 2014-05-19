from google.appengine.api import memcache
from pages.api import *
from django.conf import settings

# ...
def categories(request):
    # Get Request Language
    request_language = get_request_language(request)["request_language"]
    # Get Languages
    languages =  query_api(request_language, 'languages')
    # Get Categories
    categories = query_api(request_language, 'categories')
    pages = []
    for c in categories["categories"]:
        pages = []
        if c["parent"] is None:
            pages_in_c = query_api(request_language, 'pages', {'category_slug': c["slug"]})
            for p in pages_in_c["pages"]:
                pages.append(p)
            c["page_array"] = pages
    return {'categories': categories["categories"],  'languages': languages, 'pages': pages, 'request_language':request_language, 'template_frontpage': settings.TEMPLATE_FRONTPAGE, 'template_page': settings.TEMPLATE_PAGE, 'api_page': settings.TEMPLATE_API}

# ...
def is_logged_in(request):
    if not request.user.is_authenticated():
        return {'is_logged_in': False}
    else:
        return {'is_logged_in': True}

# ...
def is_admin(request):
    try:
        if (request.user.email in settings.ADMIN_USERS_EMAILS):
            return {'is_admin': True}
    except:
        return {'is_admin': False}
    return {'is_admin': False}

# ...
def get_request_language(request):
    language_code = str(request.path)[1:3]
    if language_code in ('en','es','fr','de','pt','ru','iw','zh'):
        return {'request_language': language_code}
    else:
        return {'request_language': 'en'}