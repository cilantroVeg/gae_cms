# Create your views here.
from django.shortcuts import redirect

# ...
def method(request):
    return redirect('/', False)