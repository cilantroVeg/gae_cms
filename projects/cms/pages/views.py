# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext, loader
from pages.models import *
from users.views import *
from django.core.mail import send_mail
from django.views.decorators.http import require_http_methods
from django.views.decorators.cache import never_cache
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.utils import simplejson as json
from django.forms.models import modelformset_factory

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

def get_category_tree(request):
    return True

def get_sub_categories(request):
    return True

def get_pages_by_category(request):
    return True

def get_page_content(request):
    return True


def language_form(request):
    if is_admin_user(request):
        if request.method == 'POST':
            form = LanguageForm(request.POST)
            if form.is_valid():
                form.save()
                return render_to_response("pages/language_list.html", {"language_list": Language.objects.all()},context_instance=RequestContext(request))
            else:
                return render_to_response("pages/language_form.html", {"form": form},context_instance=RequestContext(request))
        else:
            form = LanguageForm()
            return render_to_response("pages/language_form.html", {"form": form},context_instance=RequestContext(request))
    else:
        return redirect('/', False)


def category_form(request):
    if is_admin_user(request):
        if request.method == 'POST':
            form = CategoryForm(request.POST)
            if form.is_valid():
                form.save()
                return render_to_response("pages/category_list.html", {"category_list": Category.objects.all()},context_instance=RequestContext(request))
            else:
                return render_to_response("pages/category_form.html", {"form": form},context_instance=RequestContext(request))
        else:
            form = CategoryForm()
            return render_to_response("pages/category_form.html", {"form": form},context_instance=RequestContext(request))
    else:
        return redirect('/', False)


def page_form(request):
    if is_admin_user(request):
        if request.method == 'POST':
            form = PageForm(request.POST)
            if form.is_valid():
                form.save()
                return render_to_response("pages/page_list.html", {"page_list": Page.objects.all()},context_instance=RequestContext(request))
            else:
                return render_to_response("pages/page_form.html", {"form": form},context_instance=RequestContext(request))
        else:
            form = PageForm()
            return render_to_response("pages/page_form.html", {"form": form},context_instance=RequestContext(request))
    else:
        return redirect('/', False)


def language_list(request):
    if is_admin_user(request):
        return render_to_response("pages/language_list.html", {"language_list": Language.objects.all()},context_instance=RequestContext(request))
    else:
        return redirect('/', False)


def category_list(request):
    if is_admin_user(request):
        return render_to_response("pages/category_list.html", {"category_list": Category.objects.all()},context_instance=RequestContext(request))
    else:
        return redirect('/', False)


def page_list(request):
    if is_admin_user(request):
        return render_to_response("pages/page_list.html", {"page_list": Page.objects.all()},context_instance=RequestContext(request))
    else:
        return redirect('/', False)


from django.http import HttpResponseRedirect
from django.shortcuts import render


def spreadsheet_form(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            instance = Spreadsheet(file_field=request.FILES['file'])
            instance.save()
            return render_to_response("pages/spreadsheet_list.html", {"spreadsheet_list": Spreadsheet.objects.all()},context_instance=RequestContext(request))
    else:
        form = UploadFileForm()
    return render_to_response("pages/spreadsheet_form.html", {"form": form},context_instance=RequestContext(request))