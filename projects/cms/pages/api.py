# Create your views here.
import json
from django.http import HttpResponse
from django.core import serializers
from django.conf import settings
from pages.models import *

# ...
def languages(request,language_code):
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
    return Language.objects.get(code=language_code)
