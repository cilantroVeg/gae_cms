from django.conf import settings

from pages.models import *
from google.appengine.api import memcache


# ...
def categories(request):
    if memcache.get('categories') is not None:
        categories = memcache.get('categories')
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
            if category.parent.id == 1:
                for page in pages:
                    if page_count == 4:
                        break
                    elif page.category.id == category.id:
                        page_count = page_count + 1;
                        page_array.append({'id': page.id, 'slug': page.slug, 'title': page.title, 'headline': page.headline})
                if page_count < 4:
                    for sub_category in categories:
                        if sub_category.parent.id == category.id:
                            for page in pages:
                                if page_count == 4:
                                    break
                                elif page.category.id == sub_category.id:
                                    page_count = page_count + 1;
                                    page_array.append({'id': page.id, 'slug': page.slug, 'title': page.title, 'headline': page.headline})

            category_array.append({'id': category.id, 'name': category.name, 'slug': category.slug, 'language_code': language_code, 'parent_id': parent_id, 'page_array': page_array, 'page_count': page_count})

        memcache.add('categories', category_array)
    return {'categories': categories}

# ...
def is_logged_in(request):
    if not request.user.is_authenticated():
        return {'is_logged_in': False}
    else:
        return {'is_logged_in': True}

# ...
def is_admin_user(request):
    try:
        if request.user.email in settings.ADMIN_USERS:
            return {'is_admin_user': True}
        else:
            return {'is_admin_user': False}
    except:
        return {'is_admin_user': False}