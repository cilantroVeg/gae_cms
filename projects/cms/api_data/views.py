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

def bible_user_select_language(request):
    # List Languages
    # http://dbt.io/library/volumelanguagefamily?key=DBT_KEY=audio&v=2
    return True

def bible_user_select_bible(request):
    # List Bibles
    # http://dbt.io/library/volume?key=DBT_KEY=audio&language_family_code=ENG&v=2
    return True

def bible_get_text():
    # User Select Text
    # http://dbt.io/text/verse?key={API-Key}&dam_id=ENGESVN2ET&book_id=Matt&chapter_id=3&v=2
    return True

def bible_get_audio(request):
    # List books
    # http://dbt.io/library/book?key={API-Key}&dam_id=ENGESV&v=2
    # Location
    # http://dbt.io/audio/location?key={API-Key}&v=2
    # Get Audio Path
    # http://dbt.io/audio/path?key={API-Key}&dam_id=ENGESVN2DA&book_id=Matt&chapter_id=3&v=2
    return True


def bible_get_coyright():
    # Copyright
    # http://dbt.io/library/metadata?key={API-Key}&dam_id=ENGESVN2DA&v=2
    return True

    



