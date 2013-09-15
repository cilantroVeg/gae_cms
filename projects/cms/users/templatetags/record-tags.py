# -*- coding: utf-8 -*-

## record_tags.py
################

from django.template import Library
from pages.models import Record, Language

register = Library()


@register.filter
def get_record(key):
    try:
        return Record.objects.get(key=key).value
    except:
        return 'Key ' + key + ' Not Found'



@register.filter
def translate(key, language_code):
    if language_code == 'es':
        spanish = {
            'Home': 'Inicio',

        }
        return spanish[key]
    else:
        return key