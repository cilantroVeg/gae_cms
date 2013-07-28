# -*- coding: utf-8 -*-

## record_tags.py
################

from django.template import Library, Node, TemplateSyntaxError
from django.conf import settings
from pages.models import Record

register = Library()


@register.filter
def get_record(key):
    try:
        return Record.objects.get(key=key).value
    except:
        return 'Key '+ key + ' Not Found'