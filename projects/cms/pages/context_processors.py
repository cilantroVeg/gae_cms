
from pages.models import *

def categories(request):
    categories = Category.objects.all()
    return {'categories': categories}

def records(request):
    records = Record.objects.all()
    return {'records': records}