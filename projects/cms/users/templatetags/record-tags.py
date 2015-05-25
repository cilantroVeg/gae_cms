# -*- coding: utf-8 -*-

## record_tags.py
################

from django.template import Library
from pages.models import Record, Language
from django.conf import settings
from pages.api import *
from pages.views import normalize_text
import logging
logger = logging.getLogger(__name__)
register = Library()

@register.filter
def get_bible_books(bible):
    response_format = 'json'
    books = bible_books(None,bible,response_format)
    book_array = []
    for book in books:
        book_array.append(book["book_id"])
    return book_array

@register.filter
def detruncate(str):
    return str.replace(".", '');

@register.filter
def to_keywords(str):
    return str.replace(" ", ' ,');

@register.filter
def get_record(key, language='en'):
    cache_key = str(language) + '_get_record_' + str(key)
    data = get_cache(cache_key)
    if data:
        return data
    else:
        if language:
            l = Language.objects.filter(code=language).first()
            if l:
                record = Record.objects.filter(key=key, language=l).first()
            else:
                record = None
        else:
            record = Record.objects.filter(key=key).first()
        if record:
            set_cache(cache_key,record.value)
            return record.value
        else:
            return settings.APP_NAME

@register.filter
def translate(key, language_code):
    if language_code == 'es':
        spanish = {
            'Home': 'Inicio',
            'Contact Us': 'Contacto',
            'Register': 'Registro',
            'Your email': 'Su Email ...',
            'Password confirmation': 'Confirmar password ...',
            'Read More': 'Leer',
            'Contact Form': 'Forma De Contacto',
            'Your Name': 'Su Nombre ...',
            'Your Email': 'Su Email ...',
            'Your Comment': 'Su Mensaje ...',
            'Site map': 'Mapa del sitio',
            'Send Message': 'Enviar',
            'Magic Angel Foundation': 'FUNDACION ANGEL MAGICO',
        }
        return spanish[key]
    else:
        return key


@register.filter
def truncate_str(str, length):
    str = normalize_text(str)
    return (str[:length] + '..') if len(str) > length else str

@register.filter
def string_to_array(value):
    """Removes all values of arg from the given string"""
    if value:
        return value.split(",")
    else:
        return None

@register.filter
def string_replace_null(value):
    """Removes all values of arg from the given string"""
    return value.replace('null','')