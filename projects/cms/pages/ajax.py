# Create your views here.
from django.http import HttpResponse
from django.contrib.humanize.templatetags.humanize import naturalday
from django.conf import settings
from pages.models import *
from google.appengine.api import urlfetch
from google.appengine.api import memcache
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
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.db.models import get_model

# ...
def get_gallery_list(request):
    galleries = Gallery.objects.filter(is_enabled=True)
    gallery_list = []
    for gallery_item in galleries:
        gallery = {}
        gallery['id'] = gallery_item.id
        gallery['name'] = gallery_item.name
        gallery['slug'] = gallery_item.slug
        gallery['description'] = gallery_item.description
        gallery_list.append(gallery)
    return HttpResponse(json.dumps(gallery_list), content_type="application/json",status=200)

# ...
@csrf_exempt
@require_http_methods(["POST"])
def save_model(request,model_name,id):
    json_response = {}
    model = get_model('pages', model_name)
    if model:
        pk = request.POST.get('pk', None)
        name = request.POST.get('name', None)
        value = request.POST.get('value', None)
        object = model.objects.get(id=pk)
        if (type(getattr(object, name)) is bool) or (name == 'is_enabled'):
            setattr(object, name, bool(int(value)))
        elif type(getattr(object, name)) is unicode:
            setattr(object, name, value)
        elif type(getattr(object, name)) is int or (name == 'order'):
            setattr(object, name, int(value))
        elif (type(getattr(object, name)) is Gallery) or (name == 'gallery'):
            setattr(object, name, Gallery.objects.get(id=value))
        object.save()
        json_response['success'] = True
        json_response['new_value'] = getattr(object, name)
    else:
        json_response['success'] = False
        json_response['msg'] = 'Server Error Test'
    return HttpResponse(json.dumps(json_response), content_type="application/json",status=200)


# ...
def get_page_list(request):
    pages = Page.objects.filter(is_enabled=True)
    page_list = []
    for page_item in pages:
        page = {}
        page['id'] = page_item.id
        page['title'] = page_item.title
        page['headline'] = page_item.headline
        page_list.append(page)
    return HttpResponse(json.dumps(page_list), content_type="application/json",status=200)

# ...
def get_gallery_details(request,id):
    images = Image.objects.filter(gallery=id)
    image_list=[]
    if images:
        for image_item in images:
            image = {}
            image['id'] = image_item.id
            image['name'] = image_item.name
            image['description'] = image_item.description
            image['slug'] = image_item.slug
            image['picasa_photo_url'] = image_item.picasa_photo_url
            image['picasa_medium_url'] = image_item.picasa_medium_url
            image['picasa_thumb_url'] = image_item.picasa_thumb_url
            image_list.append(image)
    return HttpResponse(json.dumps(image_list), content_type="application/json",status=200)

# ...
def get_page_details(request,id):
    page = Page.objects.filter(id=id)[:1]
    page_object={}
    if page:        
        page_object['id'] = page[0].id
        page_object['title'] = page[0].title
        page_object['content'] = page[0].content
        page_object['slug'] = page[0].slug
        page_object['headline'] = page[0].headline
    return HttpResponse(json.dumps(page_object), content_type="application/json",status=200)

# ...
def get_cache(key):
    key = re.sub(r'\W+', '', str(key) + str(settings.APP_NAME))
    data = memcache.get(key)
    if data:
        return data
    else:
        return None

# ...
def set_cache(key,data):
    key = re.sub(r'\W+', '', str(key) + str(settings.APP_NAME))
    memcache.add(key, data, 60*60*24*30*12)
    return data

# ...
def request_url(url):
    try:
        r = requests.get(url)
    except:
        try:
            r = requests.get(url)
        except:
            r = None
    return r

#...
def xx_log(key, value):
    import sys
    print >> sys.stderr, 'OUTPUT VARIABLE CONTENT ' + str(key) + ': ' + str(value)