# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext, loader
from pages.models import *
from django.core.mail import send_mail
from django.views.decorators.http import require_http_methods
from django.views.decorators.cache import never_cache
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.utils import simplejson as json
from django.forms.models import modelformset_factory

def get_category_tree(request):
    return True

def get_sub_categories(request):
    return True

def get_pages_by_category(request):
    return True

def get_page_content(request):
    return True

def page_form(request):
    PageFormSet = modelformset_factory(Page)
    formset = PageFormSet()
    return render_to_response('pages/page_form.html', {'formset': formset},
                              context_instance=RequestContext(request))

def category_form(request):
    CategoryFormSet = modelformset_factory(Category)
    formset = CategoryFormSet()

    return render_to_response('pages/category_form.html', {'formset': formset},
                              context_instance=RequestContext(request))


def category_form(request):
    CategoryFormSet = modelformset_factory(Category)

    if request.method == 'POST': # If the form has been submitted...
        form = CategoryFormSet(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['your_email']
            recipients = ['contact@interpegasus.com']
            from django.core.mail import send_mail
            try:
                send_mail(subject, message, sender, recipients)
            except:
                log.debug("Issue sending email to: " + sender)
            return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        try:
            data = {'your_email': request.user.email}
        except:
            data = {}
        form = ContactForm(initial=data) # An unbound form
    return render(request, 'users/contact.html', {
        'form': form,
        })