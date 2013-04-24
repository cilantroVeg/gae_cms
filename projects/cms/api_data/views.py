# Create your views here.
# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext, loader
from movies.models import Movie, Code, User, Static
from multimedia.utils import *
from django.core.mail import send_mail
from django.views.decorators.http import require_http_methods
from django.views.decorators.cache import never_cache
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.utils import simplejson as json

def get_wiki_data(request):
    return True

def get_lyrics_data(request):
    return True

def get_yahoo_flick_data(request):
    return True

def get_photo_bucket_data(request):
    return True

def get_google_maps_data(request):
    return True

def get_recipes_data(request):
    return True

def get_youtube_data(request):
    return True

def get_wiki_data(request):
    return True