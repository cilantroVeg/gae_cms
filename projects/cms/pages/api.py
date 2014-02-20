# Create your views here.
import json
import re
from django.http import HttpResponse
from django.contrib.humanize.templatetags.humanize import naturalday
from django.conf import settings
from pages.models import *

# ...
def languages(request,language_code):
    response_data = {}
    languages = []
    if validate_token(request) and validate_language(language_code):
        for language in Language.objects.all():
            l = {}
            l['name'] = language.name
            l['code'] = language.code
            languages.append(l)
        response_data['languages'] = languages
        return HttpResponse(json.dumps(response_data), content_type="application/json",status=200)
    else:
        response_data['languages'] = languages
        return HttpResponse(json.dumps(response_data), content_type="application/json",status=422)

# ...
def categories(request,language_code):
    response_data = {}
    categories = []
    language = validate_language(language_code)
    if validate_token(request) and language:
        if request.REQUEST.get('category_slug', None):
            cat_slug = Category.objects.filter(language=language[0], slug=request.REQUEST['category_slug'])[:1]
            if cat_slug:
                category_set = Category.objects.order_by('order').filter(language=language[0], parent_id=cat_slug[0].id)
        else:
            category_set = Category.objects.order_by('order').filter(language=language[0])
        for category in category_set:
            c = {}
            c['id'] = category.id
            c['name'] = category.name
            c['language'] = language[0].code
            c['parent'] = category.parent_id
            c['slug'] = category.slug
            c['allow_replies'] = category.allow_replies
            categories.append(c)
    response_data['categories'] = categories
    return HttpResponse(json.dumps(response_data), content_type="application/json",status=422)

# ...
def pages(request,language_code):
    response_data = {}
    pages = []
    page_set = []
    language = validate_language(language_code)
    if validate_token(request) and language:
        if request.REQUEST.get('category_slug', None):
            cat_slug = Category.objects.filter(language=language[0], slug=request.REQUEST['category_slug'])[:1]
            if cat_slug:
                page_set = Page.objects.order_by('title').filter(is_enabled = True, category_id=cat_slug[0].id)
        elif request.REQUEST.get('page_slug', None):
            page_set = Page.objects.filter(is_enabled = True, slug=request.REQUEST['page_slug'])[:1]
        else:
            page_set = Page.objects.order_by('title').filter(is_enabled = True)
        for page in page_set:
            p = {}
            p['id'] = page.id
            p['title'] = page.title
            p['headline'] = re.sub('<[^<]+?>', '', page.headline).strip()
            p['slug'] = page.slug
            p['content'] = page.content if len(page_set) == 1 else None
            p['author'] = page.user.first_name if page.user else None
            p['category'] = page.category.name
            p['category_slug'] = page.category.slug
            p['twitter_hashtags'] = page.twitter_hashtags
            p['created_at'] = str(naturalday(page.created_at))

            pages.append(p)
    response_data['pages'] = pages
    return HttpResponse(json.dumps((response_data)), content_type="application/json", status=422)


# ...
def images(request,language_code):
    response_data = {}
    if validate_token(request) and validate_language(language_code):
        languages = []
        for language in Language.objects.all():
            l = {}
            l['name'] = language.name
            l['code'] = language.code
            languages.append(l)
        response_data['languages'] = languages
        response_data['status'] = 200
        return HttpResponse(json.dumps(response_data), content_type="application/json",status=200)
    else:
        response_data['languages'] = None
        response_data['status'] = 'Please Verify Access Token and Language'
        return HttpResponse(json.dumps(response_data), content_type="application/json",status=422)



# ...
def validate_token(request):
    return settings.API_ACCESS_TOKEN == request.REQUEST['access_token']

# ...
def validate_language(language_code):
    return Language.objects.filter(code=language_code)[:1]
