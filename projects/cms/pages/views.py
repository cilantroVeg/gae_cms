# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext, loader
from pages.models import *
from helpers.helpers import *
from django.core.mail import send_mail
from django.views.decorators.http import require_http_methods
from django.views.decorators.cache import never_cache
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.utils import simplejson as json
from django.forms.models import modelformset_factory
from django.views.generic import TemplateView
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.utils.html import *

import pprint


# ...
def category_form(request, id=None):
    if is_admin_user(request):
        instance = get_object_or_404(Category, id=id) if id is not None else None
        form = CategoryForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/categories/')
        return render_to_response("pages/category_form.html",
                                  {"form": form, "id": id, 'is_logged_in': is_logged_in(request)},
                                  context_instance=RequestContext(request))
    else:
        return redirect('/', False)

# ...
def category_list(request):
    if is_admin_user(request):
        return render_to_response("pages/category_list.html",
                                  {"category_list": Category.objects.all(), 'is_logged_in': is_logged_in(request)},
                                  context_instance=RequestContext(request))
    else:
        return redirect('/', False)

# ...
def category_delete(request, id=None):
    if is_admin_user(request):
        instance = get_object_or_404(Category, id=id) if id is not None else None
        instance.delete()
        return redirect('/categories/')
    else:
        return redirect('/', False)

# ...
def language_form(request, id=None):
    if is_admin_user(request):
        instance = get_object_or_404(Language, id=id) if id is not None else None
        form = LanguageForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/languages/')
        return render_to_response("pages/language_form.html",
                                  {"form": form, "id": id, 'is_logged_in': is_logged_in(request)},
                                  context_instance=RequestContext(request))
    else:
        return redirect('/', False)

# ...
def language_list(request):
    if is_admin_user(request):
        return render_to_response("pages/language_list.html",
                                  {"language_list": Language.objects.all(), 'is_logged_in': is_logged_in(request)},
                                  context_instance=RequestContext(request))
    else:
        return redirect('/', False)

# ...
def language_delete(request, id=None):
    if is_admin_user(request):
        instance = get_object_or_404(Language, id=id) if id is not None else None
        instance.delete()
        return redirect('/languages/')
    else:
        return redirect('/', False)

# ...
def page_form(request, id=None):
    if is_admin_user(request):
        instance = get_object_or_404(Page, id=id) if id is not None else None
        form = PageForm(request.POST or None, instance=instance)
        if form.is_valid():
            page = form.save(commit=False)
            page.user = request.user
            page.save()
            return redirect('/pages/')
        return render_to_response("pages/page_form.html", {"form": form, "id": id, "user": request.user.id,
                                                           'is_logged_in': is_logged_in(request)},
                                  context_instance=RequestContext(request))
    else:
        return redirect('/', False)

# ...
def page_list(request):
    if is_admin_user(request):
        return render_to_response("pages/page_list.html",
                                  {"page_list": Page.objects.all(), 'is_logged_in': is_logged_in(request)},
                                  context_instance=RequestContext(request))
    else:
        return redirect('/', False)

# ...
def page_delete(request, id=None):
    if is_admin_user(request):
        instance = get_object_or_404(Page, id=id) if id is not None else None
        instance.delete()
        return redirect('/pages/')
    else:
        return redirect('/', False)

# ...
def record_form(request, id=None):
    if is_admin_user(request):
        instance = get_object_or_404(Record, id=id) if id is not None else None
        form = RecordForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/records/')
        return render_to_response("pages/record_form.html",
                                  {"form": form, "id": id, 'is_logged_in': is_logged_in(request)},
                                  context_instance=RequestContext(request))
    else:
        return redirect('/', False)

# ...
def record_list(request):
    if is_admin_user(request):
        return render_to_response("pages/record_list.html",
                                  {"record_list": Record.objects.all(), 'is_logged_in': is_logged_in(request)},
                                  context_instance=RequestContext(request))
    else:
        return redirect('/', False)

# ...
def record_delete(request, id=None):
    if is_admin_user(request):
        instance = get_object_or_404(Record, id=id) if id is not None else None
        instance.delete()
        return redirect('/records/')
    else:
        return redirect('/', False)


def get_category_tree(request):
    return True


def get_sub_categories(request):
    return True


def get_pages_by_category(request):
    return True


def get_page_content(request):
    return True


# ...
def spreadsheet_form(request, id=None):
    if is_admin_user(request):
        instance = get_object_or_404(Spreadsheet, id=id) if id is not None else None
        form = SpreadsheetForm(request.POST or None, request.FILES or None, instance=instance)
        if form.is_valid():
            spreadsheet = form.save(commit=False)
            spreadsheet.name = request.POST['name']
            spreadsheet.spreadsheet_file = request.FILES['spreadsheet_file'].name
            spreadsheet.size = request.FILES['spreadsheet_file'].size
            spreadsheet.save()
            handle_spreadsheet(request.FILES['spreadsheet_file'], request.user, spreadsheet)
            return redirect('/spreadsheets/')
        return render_to_response("pages/spreadsheet_form.html",
                                  {"form": form, "id": id, 'is_logged_in': is_logged_in(request)},
                                  context_instance=RequestContext(request))
    else:
        return redirect('/', False)

# ...
def handle_spreadsheet(f, user,spreadsheet):
    import xlrd

    workbook = xlrd.open_workbook(file_contents=f.read())
    worksheets = workbook.sheet_names()
    for worksheet_name in worksheets:
        worksheet = workbook.sheet_by_name(worksheet_name)
        num_of_rows = worksheet.nrows
        if (num_of_rows != 0):
            for i in range(num_of_rows):
                if i == 0:
                    continue
                language_code = worksheet.cell(i, 0).value
                category_name = worksheet.cell(i, 1).value
                parent_category_name = worksheet.cell(i, 2).value
                page_title = worksheet.cell(i, 3).value
                page_content = worksheet.cell(i, 4).value
                image_urls = worksheet.cell(i, 5).value
                # Language
                language, language_created = Language.objects.get_or_create(code=language_code,
                                                                            defaults={'name': language_code})
                # Categories
                parent, parent_created = Category.objects.get_or_create(name=parent_category_name,
                                                                        defaults={'parent': None, 'language': language,
                                                                                  'allow_replies': True})
                category, category_created = Category.objects.get_or_create(name=category_name,
                                                                            defaults={'parent': parent,
                                                                                      'language': language,
                                                                                      'allow_replies': True})
                # Page
                page, created = Page.objects.get_or_create(category=category, title=strip_tags(page_title), defaults={'user':user})
                page.content = strip_tags(page_content)
                page.spreadsheet = spreadsheet
                page.save()


# ...
def spreadsheet_list(request):
    if is_admin_user(request):
        return render_to_response("pages/spreadsheet_list.html", {"spreadsheet_list": Spreadsheet.objects.all(),
                                                                  'is_logged_in': is_logged_in(request)},
                                  context_instance=RequestContext(request))
    else:
        return redirect('/', False)

# ...
def spreadsheet_delete(request, id=None):
    if is_admin_user(request):
        instance = get_object_or_404(Spreadsheet, id=id) if id is not None else None
        instance.delete()
        return redirect('/spreadsheets/')
    else:
        return redirect('/', False)
