from django.conf import settings

from pages.models import *
from google.appengine.api import memcache
from django.shortcuts import get_object_or_404

# ...
def categories(request):
    # Get All Categories
    languages = Language.objects.filter(is_enabled=True)
    if memcache.get('category_array') is not None:
        category_array = memcache.get('category_array')
    else:
        categories = Category.objects.all()
        pages = Page.objects.all()
        category_array = []
        for category in categories:
            if category.parent is not None:
                parent_id = category.parent.id
            else:
                parent_id = None
            if category.language is None:
                language_code = 'en'
            else:
                language_code = category.language.code
            page_array = []
            for page in pages:
                    if page.category.id == category.id:
                        headline = (page.content[:80] + '..') if len(page.content) > 80 else page.content
                        page_array.append({'id': page.id, 'slug': page.slug, 'title': page.title, 'headline': headline})
            category_array.append({'id': category.id, 'name': category.name, 'slug': category.slug, 'language_code': language_code, 'parent_id': parent_id, 'page_array': page_array, 'page_count': len(page_array)})
        memcache.add('category_array', category_array)
    return {'categories': category_array, 'languages': languages, 'template_frontpage': settings.TEMPLATE_FRONTPAGE, 'template_page': settings.TEMPLATE_PAGE, 'api_page': settings.TEMPLATE_API}

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
def request_language(request,language=''):
    if language:
        language = get_object_or_404(Language, code=language)
        return {'request_language': language.code}
    else:
        return {'request_language': 'en'}
