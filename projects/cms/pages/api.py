# Create your views here.
from django.http import HttpResponse
from django.contrib.humanize.templatetags.humanize import naturalday
from django.conf import settings
from pages.models import *
from google.appengine.api import urlfetch
from google.appengine.api import memcache
from django.utils.html import *
from google.appengine.api import memcache
from django.views.decorators.csrf import csrf_exempt

import json
import urllib2
import urllib
import json
import re
import feedparser
import datetime
import time
import requests
import logging

logger = logging.getLogger(__name__)

# ...
def languages(request,language_code='en'):
    response_data = {}
    response_data['message'] = 'Success.'
    response_data['status'] = 200
    if validate_token(request) and validate_language(language_code):
        cache_key = str(language_code) + '_languages_'
        response_data['languages'] = get_cache(cache_key)
        if response_data['languages'] is None:
            languages = []
            for language in Language.objects.all():
                l = {}
                l['name'] = language.name
                l['code'] = language.code
                languages.append(l)
            response_data['languages'] = languages
            set_cache(cache_key,languages)
    else:
        response_data['languages'] = None
        response_data['message'] = 'Please verify access token and language code.'
        response_data['status'] = 403
    return HttpResponse(json.dumps(response_data), content_type="application/json",status=response_data['status'])

# ...
def categories(request,language_code='en'):
    response_data = {}
    response_data['message'] = 'Success.'
    response_data['status'] = 200
    if validate_token(request) and validate_language(language_code):
        category_slug = request.REQUEST.get('category_slug', None)
        cache_key = str(language_code) + '_categories_' + str(category_slug)
        response_data['categories'] = get_cache(cache_key)
        if response_data['categories'] is None:
            categories = []
            language = validate_language(language_code)     
            if category_slug:
                category_slug_object = Category.objects.filter(language=language[0], slug=request.REQUEST['category_slug'])[:1]
                if category_slug_object:
                    category_set = Category.objects.order_by('order').filter(language=language[0], parent_id=category_slug_object[0].id)
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
            set_cache(cache_key,categories)
    else:
        response_data['categories'] = None
        response_data['message'] = 'Please verify access token and language code.'
        response_data['status'] = 403
    return HttpResponse(json.dumps(response_data), content_type="application/json",status=response_data['status'])

# ...
def pages(request,language_code='en'):
    response_data = {}
    response_data['message'] = 'Success.'
    response_data['status'] = 200
    if validate_token(request) and validate_language(language_code):
        category_slug = request.REQUEST.get('category_slug', None)
        page_slug = request.REQUEST.get('page_slug', None)
        cache_key = str(language_code) + '_pages_' + str(category_slug) + str(page_slug)
        response_data['pages'] = get_cache(cache_key)
        if response_data['pages'] is None:
            pages = []
            page_set = []
            language = validate_language(language_code)
            if category_slug:
                category_slug_object = Category.objects.filter(language=language[0], slug=request.REQUEST['category_slug'])[:1]
                if category_slug_object:
                    page_set = Page.objects.order_by('title').filter(is_enabled = True, category_id=category_slug_object[0].id)
            elif page_slug:
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
                p['content_no_html'] = strip_tags(p['content'] ) if p['content'] else None
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
                p['timestamp'] = None
                pages.append(p)
            response_data['pages'] = pages
            set_cache(cache_key,pages)
    else:
        response_data['pages'] = None
        response_data['message'] = 'Please verify access token and language code.'
        response_data['status'] = 403
    return HttpResponse(json.dumps(response_data), content_type="application/json",status=response_data['status'])

# ...
def images(request,language_code='en'):
    response_data = {}
    response_data['message'] = 'Success.'
    response_data['status'] = 200
    if validate_token(request) and validate_language(language_code):        
        page_slug = request.REQUEST.get('page_slug', None)
        cache_key = str(language_code) + '_images_' + str(page_slug)
        response_data['images'] = get_cache(cache_key)
        if response_data['images'] is None:
            images = []
            image_set = []
            if page_slug:
                page_slug_object = Page.objects.filter(slug=request.REQUEST['page_slug'])[:1]
                if page_slug_object:
                    image_set = Image.objects.order_by('name').filter(page_id=page_slug_object[0].id)
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
            set_cache(cache_key,images)
    else:
        response_data['images'] = None
        response_data['message'] = 'Please verify access token and language code.'
        response_data['status'] = 403
    return HttpResponse(json.dumps(response_data), content_type="application/json",status=response_data['status'])    
    
# ...
def galleries(request,language_code='en'):
    response_data = {}
    response_data['message'] = 'Success.'
    response_data['status'] = 200
    if validate_token(request) and validate_language(language_code):
        cache_key = str(language_code) + '_galleries_'
        response_data['galleries'] = get_cache(cache_key)
        if response_data['galleries'] is None:
            galleries = None
            gallery_set = Gallery.objects.order_by('name')
            if gallery_set:
                galleries = []
                for gallery in gallery_set:
                    i = {}
                    i['id'] = gallery.id
                    i['name'] = gallery.name
                    i['slug'] = gallery.slug
                    i['is_enabled'] = gallery.is_enabled
                    i['is_default'] = gallery.is_default
                    i['created_at'] = str(naturalday(gallery.created_at))
                    galleries.append(i)
            response_data['galleries'] = galleries
            set_cache(cache_key,galleries)
    else:
        response_data['galleries'] = None
        response_data['message'] = 'Please verify access token and language code.'
        response_data['status'] = 403
    return HttpResponse(json.dumps(response_data), content_type="application/json",status=response_data['status'])


# ...
def feed_pages(request, language_code='en'):
    response_data = {}
    response_data['message'] = 'Success.'
    response_data['status'] = 200
    if validate_token(request) and validate_language(language_code):
        cache_key = str(language_code) + '_feed_pages_'
        response_data['pages'] = get_cache(cache_key)
        if response_data['pages'] is None:
            response_data = {}
            pages = []
            page_set = {}
            feeds = Feed.objects.all()
            for feed in feeds:
                pages = parse_feed(feed)
                page_set[feed.source_type] = pages
            response_data['pages'] = page_set
            set_cache(cache_key,page_set)
    else:
        response_data['pages'] = None
        response_data['message'] = 'Please verify access token and language code.'
        response_data['status'] = 403
    return HttpResponse(json.dumps(response_data), content_type="application/json",status=200)

# ...
def validate_token(request):
    try:
        return (settings.API_ACCESS_TOKEN == request.REQUEST['access_token']) or (settings.API_ACCESS_TOKEN_1 == request.REQUEST['access_token'])
    except:
        logger.error('api/validate_token')
        return False

# ...
def validate_language(language_code='en'):
    cache_key = str(language_code) + '_validate_language_'
    data = get_cache(cache_key)
    if data:
        return data
    else:
        response = Language.objects.filter(code=language_code).first()
        if response:
            set_cache(cache_key,[response])
        return response

# ...
def query_api(language_code, api_request, extra_parameters={}):
    # Get data from cache
    key = str(language_code) + str(api_request) + str(extra_parameters)
    data = get_cache(key)
    counter = 0
    while (data is None) and (counter < 3):
        counter = counter + 1
        try:
            url = build_url(language_code, api_request, extra_parameters)
            result = urlfetch.fetch(url)
            data = json.loads(result.content)
            set_cache(key,data)
        except:
            if (counter > 2):
                logger.error('api/query_api counter:' + str(counter))
                logger.error('URL:' + str(url))
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
    cache_key = str('bible_languages') + '_' + str(media) + '_' + str(return_type)
    response_data['languages'] = get_cache(cache_key)
    if response_data['languages'] is None:
        if media =='text':
            r = request_url(settings.DBT_LANGUAGE_TEXT_URL)
        elif media == 'audio':
            r = request_url(settings.DBT_LANGUAGE_AUDIO_URL)
        elif media == 'video':
            r = request_url(settings.DBT_LANGUAGE_VIDEO_URL)
        else:
            r = request_url(settings.DBT_LANGUAGE_TEXT_URL)
        if r.status_code == 200:
            response_data['languages'] = r.json()
            set_cache(cache_key,response_data['languages'])
        else:
            response_data['languages'] = None

    if return_type:
        return response_data['languages']
    else:
        return HttpResponse(json.dumps(response_data), content_type="application/json",status=r.status_code)

# ...
def bible_list(request,media,language_code,return_type=None):
    response_data = {}
    cache_key = str('bible_list') + '_' + str(media) + '_' + str(language_code) + '_' + str(return_type)
    response_data['bibles'] = get_cache(cache_key)
    if response_data['bibles'] is None:
        if media =='text':
            r = request_url(settings.DBT_GET_BIBLES_FOR_LANGUAGE_URL + '&media=text&language_family_code=' + language_code)
            logger.error('HERE: ' + str(settings.DBT_GET_BIBLES_FOR_LANGUAGE_URL + '&media=text&language_family_code=' + language_code))
        elif media == 'audio':
            r = request_url(settings.DBT_GET_BIBLES_FOR_LANGUAGE_URL + '&media=audio&language_family_code=' + language_code)
        elif media == 'video':
            r = request_url(settings.DBT_GET_BIBLES_FOR_LANGUAGE_URL + '&media=video&language_family_code=' + language_code)
        else:
            r = request_url(settings.DBT_GET_BIBLES_FOR_LANGUAGE_URL + '&media=text&language_family_code=' + language_code)
        if r.status_code == 200:
            response_data['bibles'] = r.json()
            set_cache(cache_key,response_data['bibles'])
        else:
            response_data['bibles'] = None
    if return_type:
        return response_data['bibles']
    else:
        return HttpResponse(json.dumps(response_data), content_type="application/json",status=r.status_code)

# ...
def bible_books(request,dam_id,return_type=None):
    response_data = {}
    cache_key = str('bible_books') + '_' + str(dam_id) + '_' + str(return_type)
    response_data['books'] = get_cache(cache_key)
    if response_data['books'] is None:
        r = request_url(settings.DBT_GET_BIBLE_BOOKS_URL + '&dam_id=' + dam_id)
        if r and r.status_code == 200:
            try:
                response_data['books'] = r.json()
                set_cache(cache_key,response_data['books'])
            except:
                logger.error('api/bible_books')
                response_data['books'] = None
        else:
            response_data['books'] = None
    if return_type:
        return response_data['books']
    else:
        return HttpResponse(json.dumps(response_data), content_type="application/json",status=r.status_code)

# ...
def bible_book_text(request,dam_id,book_id,chapter_id,return_type=None):
    response_data = {}
    r = request_url(settings.DBT_GET_BIBLE_BOOKS_TEXT_URL + '&dam_id=' + dam_id + '&book_id=' + book_id + '&chapter_id=' + str(chapter_id))
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
    cache_key = str('bible_copyright') + '_' + str(dam_id) + '_' + str(return_type)
    response_data['copyright'] = get_cache(cache_key)
    if response_data['copyright'] is None:
        r = request_url(settings.DBT_GET_COPYRIGHT_URL + '&dam_id=' + str(dam_id))
        if r.status_code == 200:
            response_data['copyright'] = r.json()
            set_cache(cache_key,response_data['copyright'])
        else:
            response_data['copyright'] = None
    if return_type:
        return response_data['copyright']
    else:
        return HttpResponse(json.dumps(response_data), content_type="application/json",status=r.status_code)

# ...
def get_cache(key):
    key = re.sub(r'\W+', '', str(key) + '_' + str(settings.APP_NAME))
    data = memcache.get(key)
    if data:
        return deserialize_entities(data)
    else:
        return None

# ...
def set_cache(key,data):
    key = re.sub(r'\W+', '', str(key) + '_' + str(settings.APP_NAME))
    memcache.add(key, serialize_entities(data), 60*60*24*7)
    return data

# ...
def serialize_entities(data):
    return (data)

# ...
def deserialize_entities(data):
    return (data)

# ...
@csrf_exempt
def validate_recaptcha(request):
    captcha_response =  request.POST.get('captcha_response', None)
    response_data = {}
    response_data['result'] = captcha_is_valid(captcha_response,request)
    return HttpResponse(json.dumps(response_data), content_type="application/json",status=200)

def captcha_is_valid(captcha_response,request):
    return True
    url = 'https://www.google.com/recaptcha/api/siteverify'
    response_data = False
    logger.info('Google Captcha Validation')
    logger.info('captcha_response:')
    logger.info(captcha_response)
    if captcha_response:
        params = {'secret': '6LdhIwMTAAAAAB7Rt27xR15hHfK4rZtWgfcEVzqj', 'response': str(captcha_response), 'remoteip': get_client_ip(request) }
        response = request_url(url,'POST',params)
        if response:
            response_json = json.loads(response.content)
            response_data = response_json['success']
            logger.info('RESPONSE SUCCESS CONTENT')
            logger.info(str(response_data))
            logger.info('CAPTCHA RESPONSE')
            logger.info(str(captcha_response))
    return response_data

# ...
def request_url(url,type='GET',params=None):
    data = None
    counter = 0
    while (data is None) and (counter < 3):
        counter = counter + 1
        if (type == 'GET'):
            try:
                data = requests.get(url)
            except:
                if (counter > 2):
                    logger.error('api/query_api GET:' + str(counter))
                    logger.error('URL:' + str(url))
                data = None
        elif (type == 'POST'):
            headers = {'content-type': 'application/json'}
            try:
                data = requests.post(url, params=params)
            except:
                if (counter > 2):
                    logger.error('api/query_api POST:' + str(counter))
                    logger.error('URL:' + str(url))
                data = None
    return data

#...
def xx_log(key, value):
    import sys
    print >> sys.stderr, 'OUTPUT VARIABLE CONTENT ' + str(key) + ': ' + str(value)

def get_client_ip(request):
    try:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
    except:
        ip=None
    return ip

def json_file(request,file_name='interpegasus_cms'):
    url = settings.SITE_URL +'/static/template/API/api-docs/' + str(file_name)
    result = urlfetch.fetch(url)
    return HttpResponse(result.content, mimetype='application/json',status=200)


def not_found(request):
    return HttpResponse(json.dumps({'status':404}), mimetype='application/json',status=404)