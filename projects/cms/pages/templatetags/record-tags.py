# -*- coding: utf-8 -*-

## record_tags.py
################

from django.template import Library
from pages.models import Record, Language

register = Library()


@register.filter
def get_record(key, language=None):
    try:
        if language is None:
            return Record.objects.get(key=key).value
        else:
            return Record.objects.get(key=key, language_id=language.id).value
    except:
        return 'Key ' + key + ' Not Found'


@register.filter
def translate(key, language_code):
    if language_code == 'es':
        spanish = {
            'Home': 'Top',
            'Home': 'Top',
            'Home': 'Top',
            'Home': 'Top',
            'Home': 'Top',
            'Home': 'Top',
            'Home': 'Top',
            'Home': 'Top',
            'Home': 'Top',
            'Home': 'Top'
        }
        return spanish[key]
    else:
        return language_code