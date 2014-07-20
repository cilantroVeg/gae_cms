# Create your views here.
from django.http import HttpResponse
from django.contrib.humanize.templatetags.humanize import naturalday
from django.conf import settings
from pages.models import *
from google.appengine.api import urlfetch
from django.utils.html import *
import json
import urllib2
import urllib
import json
import re
import feedparser
import datetime
import time
import requests

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
            p['content_no_html'] = strip_tags(p['content'] )
            p['author'] = page.user.first_name if page.user else None
            p['category'] = page.category.name
            p['category_slug'] = page.category.slug
            p['feed_type'] = None
            p['twitter_hashtags'] = page.twitter_hashtags
            p['feed_source']= page.feed_source
            p['feed_image_url'] = None
            p['image_url']= page.image_url
            p['video_url']= page.video_url
            p['audio_url']= page.audio_url
            p['priority']= page.priority
            p['is_enabled']= page.is_enabled
            p['created_at'] = str(naturalday(page.created_at))
            p['timestamp'] = time.mktime(page.created_at)
            pages.append(p)
    response_data['pages'] = pages
    return HttpResponse(json.dumps((response_data)), content_type="application/json", status=422)

# ...
def images(request,language_code):
    response_data = {}
    images = []
    image_set = []
    if validate_token(request):
        if request.REQUEST.get('page_slug', None):
            pag_slug = Page.objects.filter(slug=request.REQUEST['page_slug'])[:1]
            if pag_slug:
                image_set = Image.objects.order_by('name').filter(page_id=pag_slug[0].id)
        else:
            image_set = Image.objects.order_by('name')
        for image in image_set:
            i = {}
            i['id'] = image.id
            i['page_slug'] = image.page.slug if image.page else None
            i['name'] = image.name
            i['slug'] = image.slug
            i['picasa_photo_url'] = image.picasa_photo_url
            i['picasa_thumb_url'] = image.picasa_thumb_url
            i['height'] = image.height
            i['width'] = image.width
            i['created_at'] = str(naturalday(image.created_at))
            images.append(i)
    response_data['images'] = images
    return HttpResponse(json.dumps((response_data)), content_type="application/json", status=422)

# ...
def feed_pages(request, language_code):
    response_data = {}
    pages = []
    page_set = {}
    language = validate_language(language_code)
    if validate_token(request) and language:
        feeds = Feed.objects.all()
        # Iterate feeds and add items to page_set
        for feed in feeds:
            pages = parse_feed(feed)
            page_set[feed.source_type] = pages # sorted(pages, key=lambda k: k['timestamp'], reverse=True)
    response_data['pages'] = page_set
    return HttpResponse(json.dumps((response_data)), content_type="application/json", status=422)


# ...
def validate_token(request):
    return (settings.API_ACCESS_TOKEN == request.REQUEST['access_token']) or (settings.API_ACCESS_TOKEN_1 == request.REQUEST['access_token'])

# ...
def validate_language(language_code):
    return Language.objects.filter(code=language_code)[:1]

# ...
def query_api(language_code, api_request, extra_parameters={}):
    url = build_url(language_code, api_request, extra_parameters)
    result = urlfetch.fetch(url)
    try:
        data = json.loads(result.content)
    except:
        data = None
    return data

def build_url(language_code, api_request, extra_parameters):
    url = str(settings.SITE_URL) + '/api/' + str(language_code) + '/' + api_request + '?access_token=' + settings.API_ACCESS_TOKEN
    url = url + '&' + urllib.urlencode(extra_parameters)
    return url

def parse_feed(feed):
    feed_url = feed.feed_url
    source_type = feed.source_type
    pages = []
    if source_type == 'YAHOO':
        info = feedparser.parse(feed_url)
        for entry in info.entries:
            match = re.search(r'src="(.*?)"', entry.content[0]["value"])
            if match:
                image_url = match.groups()[0]
            else:
                image_url = None
            if image_url:
                p = {}
                p['id'] = None
                p['title'] = entry.title
                p['headline'] = (entry.title[:29] + '..') if len(entry.title) > 29 else entry.title
                p['slug'] = slugify(entry.title)
                p['content'] = entry.description
                p['content_no_html'] = strip_tags(p['content'] )
                p['author'] = None
                p['category'] = source_type
                p['category_slug'] = slugify(source_type)
                p['feed_type'] = source_type
                p['twitter_hashtags'] = None
                p['feed_source']= entry.link
                p['feed_image_url']= feed.logo_url
                p['image_url']= image_url
                p['video_url']= None
                p['audio_url']= None
                p['priority']= 2
                p['is_enabled']= True
                p['created_at'] = str(naturalday(datetime.datetime.fromtimestamp(time.mktime(entry.published_parsed))))
                p['timestamp'] = time.mktime(entry.published_parsed)
                if len(entry.description) > 140:
                    pages.append(p)
    elif source_type == 'GREENPEACE':
        info = feedparser.parse(feed_url)
        for entry in info.entries:
            match = re.search(r'src="(.*?)"', entry.description)
            if match:
                image_url = match.groups()[0]
            else:
                image_url = None
            if image_url:
                p = {}
                p['id'] = None
                p['title'] = entry.title
                p['headline'] = (entry.title[:29] + '..') if len(entry.title) > 29 else entry.title
                p['slug'] = slugify(entry.title)
                p['content'] = entry.description
                p['content_no_html'] = strip_tags(p['content'] )
                p['author'] = None
                p['category'] = source_type
                p['category_slug'] = slugify(source_type)
                p['feed_type'] = source_type
                p['twitter_hashtags'] = None
                p['feed_source']= entry.link
                p['feed_image_url']= feed.logo_url
                p['image_url']= image_url
                p['video_url']= None
                p['audio_url']= None
                p['priority']= 2
                p['is_enabled']= True
                p['created_at'] = str(naturalday(datetime.datetime.fromtimestamp(time.mktime(entry.published_parsed))))
                p['timestamp'] = time.mktime(entry.published_parsed)
                if len(entry.description) > 140:
                    pages.append(p)
    elif source_type == 'PETA':
        info = feedparser.parse(feed_url)
        for entry in info.entries:
            match = re.search(r'[href|src]="(.*(png|jpg))"', entry.description)
            if match:
                image_url = match.groups()[0]
            else:
                image_url = None
            if image_url:
                p = {}
                p['id'] = None
                p['title'] = entry.title
                p['headline'] = (entry.title[:29] + '..') if len(entry.title) > 29 else entry.title
                p['slug'] = slugify(entry.title)
                p['content'] = entry.description
                p['content_no_html'] = strip_tags(p['content'] )
                p['author'] = None
                p['category'] = source_type
                p['category_slug'] = slugify(source_type)
                p['feed_type'] = source_type
                p['twitter_hashtags'] = None
                p['feed_source']= entry.link
                p['feed_image_url']= feed.logo_url
                p['image_url']= image_url
                p['video_url']= None
                p['audio_url']= None
                p['priority']= 2
                p['is_enabled']= True
                p['created_at'] = str(naturalday(datetime.datetime.fromtimestamp(time.mktime(entry.published_parsed))))
                p['timestamp'] = time.mktime(entry.published_parsed)
                if len(entry.description) > 140:
                    pages.append(p)
    elif source_type == 'WWF':
        info = feedparser.parse(feed_url)
        for entry in info.entries:
            match = re.search(r'[href|src]="(.*(png|jpg))"', entry.description)
            if match:
                image_url = match.groups()[0]
            else:
                image_url = None
            if True:
                p = {}
                p['id'] = None
                p['title'] = entry.title
                p['headline'] = (entry.title[:29] + '..') if len(entry.title) > 29 else entry.title
                p['slug'] = slugify(entry.title)
                p['content'] = entry.description
                p['content_no_html'] = strip_tags(p['content'] )
                p['author'] = None
                p['category'] = source_type
                p['category_slug'] = slugify(source_type)
                p['feed_type'] = source_type
                p['twitter_hashtags'] = None
                p['feed_source']= entry.link
                p['feed_image_url']= feed.logo_url
                p['image_url']= image_url
                p['video_url']= None
                p['audio_url']= None
                p['priority']= 2
                p['is_enabled']= True
                p['created_at'] = str(naturalday(datetime.datetime.fromtimestamp(time.mktime(entry.published_parsed))))
                p['timestamp'] = time.mktime(entry.published_parsed)
                if len(entry.description) > 140:
                    pages.append(p)
    else:
        return None
    return pages


# Bible
# ...
def bible_languages(request,media,return_type=None):
    response_data = {}
    if media =='text':
        r = requests.get(settings.DBT_LANGUAGE_TEXT_URL)
    elif media == 'audio':
        r = requests.get(settings.DBT_LANGUAGE_AUDIO_URL)
    elif media == 'video':
        r = requests.get(settings.DBT_LANGUAGE_VIDEO_URL)
    else:
        r = requests.get(settings.DBT_LANGUAGE_TEXT_URL)
    if r.status_code == 200:
        response_data['languages'] = r.json()
    else:
        response_data['languages'] = None
    if return_type:
        return response_data['languages']
    else:
        return HttpResponse(json.dumps(response_data), content_type="application/json",status=r.status_code)

# ...
def bible_list(request,media,language_code,return_type=None):
    response_data = {}
    if media =='text':
        r = requests.get(settings.DBT_GET_BIBLES_FOR_LANGUAGE_URL + '&media=text&language_family_code=' + language_code)
    elif media == 'audio':
        r = requests.get(settings.DBT_GET_BIBLES_FOR_LANGUAGE_URL + '&media=audio&language_family_code=' + language_code)
    elif media == 'video':
        r = requests.get(settings.DBT_GET_BIBLES_FOR_LANGUAGE_URL + '&media=video&language_family_code=' + language_code)
    else:
        r = requests.get(settings.DBT_GET_BIBLES_FOR_LANGUAGE_URL + '&media=text&language_family_code=' + language_code)
    if r.status_code == 200:
        response_data['bibles'] = r.json()
    else:
        response_data['bibles'] = None
    if return_type:
        return response_data['bibles']
    else:
        return HttpResponse(json.dumps(response_data), content_type="application/json",status=r.status_code)

# ...
def bible_books(request,dam_id,return_type=None):
    response_data = {}
    r = requests.get(settings.DBT_GET_BIBLE_BOOKS_URL + '&dam_id=' + dam_id)
    if r.status_code == 200:
        response_data['books'] = r.json()
    else:
        response_data['books'] = None
    if return_type:
        return response_data['books']
    else:
        return HttpResponse(json.dumps(response_data), content_type="application/json",status=r.status_code)


# ...
def bible_book_text(request,dam_id,book_id,chapter_id,return_type=None):
    response_data = {}
    r = requests.get(settings.DBT_GET_BIBLE_BOOKS_TEXT_URL + '&dam_id=' + dam_id + '&book_id=' + book_id + '&chapter_id=' + str(chapter_id))
    if r.status_code == 200:
        response_data['text'] = r.json()
    else:
        response_data['text'] = None
    if return_type:
        return response_data['text']
    else:
        return HttpResponse(json.dumps(response_data), content_type="application/json",status=r.status_code)

# ...
def bible_copyright(request,dam_id,return_type=None):
    response_data = {}
    r = requests.get(settings.DBT_GET_COPYRIGHT_URL + '&dam_id=' + str(dam_id))
    if r.status_code == 200:
        response_data['copyright'] = r.json()
    else:
        response_data['copyright'] = None
    if return_type:
        return response_data['copyright']
    else:
        return HttpResponse(json.dumps(response_data), content_type="application/json",status=r.status_code)

