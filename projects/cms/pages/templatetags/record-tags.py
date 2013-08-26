# -*- coding: utf-8 -*-

## record_tags.py
################

from django.template import Library
from pages.models import Record

register = Library()


@register.filter
def get_record(key):
    try:
        return Record.objects.get(key=key).value
    except:
        return 'Key ' + key + ' Not Found'