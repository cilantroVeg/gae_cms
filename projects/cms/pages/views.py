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

def get_category_tree(request):
    return True

def get_sub_categories(category_id):
    return True

def get_pages_by_category(category_id):
    return True

def get_page_content(page_id):
    return True

def get_page_photos(page_id):
    return True

def add_page_form(page_id):
    return True

def add_page_form_process(page_id):
    return True

def add_page_form(page_id):
    return True

def add_page_form_action(page_id):
    return True

def add_category_form(page_id):
    return True

def add_category_form_action(page_id):
    return True


