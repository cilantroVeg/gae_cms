from django.conf import settings

from pages.models import *
from google.appengine.api import memcache


# ...
def categories(request):
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
            # get up to 4 pages for each main category
            page_array = []
            page_count = 0
            if category.parent is not None and category.parent.id == 1:
                page_limit = max(category.frontpage_page_limit, 4)
                for page in pages:
                    if page_count == page_limit:
                        break
                    elif page.category.id == category.id:
                        page_count += 1
                        page_array.append({'id': page.id, 'slug': page.slug, 'title': page.title, 'headline': page.content})
                if page_count < page_limit:
                    for sub_category in categories:
                        if sub_category.parent is not None and sub_category.parent.id == category.id:
                            for page in pages:
                                if page_count == page_limit:
                                    break
                                elif page.category.id == sub_category.id:
                                    page_count += 1
                                    page_array.append({'id': page.id, 'slug': page.slug, 'title': page.title, 'headline': page.content})

            category_array.append({'id': category.id, 'name': category.name, 'slug': category.slug, 'language_code': language_code, 'parent_id': parent_id, 'page_array': page_array, 'page_count': page_count})

        memcache.add('category_array', category_array)
    return {'categories': category_array, 'languages': languages}

# ...
def is_logged_in(request):
    if not request.user.is_authenticated():
        return {'is_logged_in': False}
    else:
        return {'is_logged_in': True}

# ...
def is_admin(request):
    try:
        if request.user.email in settings.ADMIN_USERS:
            return {'is_admin': True}
        else:
            return {'is_admin': False}
    except:
        return {'is_admin': False}