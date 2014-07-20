# -*- coding: utf-8 -*-

## record_tags.py
################

from django.template import Library
from pages.models import Record, Language

register = Library()


@register.filter
def get_record(key, language='en'):
    if language:
        try:
            l = Language.objects.get(code=language)
        except:
            l = None
        if l:
            record = Record.objects.filter(key=key, language=l)
        else:
            record = None
    else:
        record = Record.objects.filter(key=key)[0].value
    if record:
        return record[0].value
    else:
        return 'No Content in Language'


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
    return (str[:length] + '..') if len(str) > length else str

@register.filter
def format_testament(value):
    """Removes all values of arg from the given string"""
    if value == 'Old Testament':
        return 'NT'
    elif value == 'New Testament':
        return 'NT'
    else:
        return value