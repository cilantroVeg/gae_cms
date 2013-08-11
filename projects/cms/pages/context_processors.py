from pages.models import *

from google.appengine.api import memcache

# ...
def categories(request):
    if memcache.get('categories') is not None:
        categories = memcache.get('categories')
    else:
        categories = Category.objects.all()
        categories_array = []
        for category in categories:
            if category.parent is not None:
                parent_id = category.parent.id
            else:
                parent_id = None
            categories_array.append({'id': category.id, 'name': category.name, 'slug': category.slug, 'language_code': category.language.code, 'parent_id': parent_id})
        memcache.add('categories', categories_array)
    ...
    show_pages = Record.objects.get(key="SHOW_PAGES_ON_FOOTER")
    if show_pages.value in ['True', '1', 'true']:
        if memcache.get('pages') is not None:
            pages = memcache.get('pages')
        else:
            pages = Page.objects.all()
            pages_array = []
            for page in pages:
                pages_array.append({'title': page.title, 'slug': page.slug, 'category_id': page.category.id, 'language_code': page.category.language.code})
            memcache.add('pages', pages_array)
    else:
        pages = None
    return {'categories': categories, 'pages': pages}



