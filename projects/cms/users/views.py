# https://docs.djangoproject.com/en/dev/topics/auth/default/
import logging
from pages.context_processors import *

log = logging.getLogger(__name__)
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib.auth import login
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.conf import settings
from pages.models import Record


#from django.contrib.auth.models import Group, Permission
#from django.contrib.contenttypes.models import ContentType



#######################
# User Related Methods
#######################


def enter(request):
    if is_logged_in(request):
        return redirect('/', False)
    return render_to_response('users/signup.html',
                              context_instance=RequestContext(request))


def not_found(request):
    return render_to_response('template/404.html',
                              context_instance=RequestContext(request))


def exit_request(request):
    logout(request)
    request.session = None
    return redirect('/', False)


@require_http_methods(["POST"])
def process_create_account(request):
    try:
        u = User.objects.filter(email=request.POST['email'])
    except:
        u = False # user does not exist in database
    if u:
        return render_to_response('users/signup.html', {'error_message': "Email is already taken"},
                                  context_instance=RequestContext(request))
    User.objects.create_user(request.POST['email'], request.POST['email'], request.POST['password'])
    user = authenticate(username=request.POST['email'], password=request.POST['password'])
    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect('/', False)
    else:
        return render_to_response('users/signup.html', {'error_message': "Email is already taken"},
                                  context_instance=RequestContext(request))


@require_http_methods(["POST"])
def process_sign_up(request):
    username = request.POST['email_2']
    password = request.POST['password_2']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect('/', False)
    else:
        # Return an 'invalid login' error message.
        return render_to_response('users/signup.html', {'error_message': "Email and Password Don't Match"},
                                  context_instance=RequestContext(request))


def front_page(request):
    from django.utils import translation
    thread_language = translation.get_language()
    languages = Language.objects.filter(is_enabled=True)
    for language in languages:
        if language.code in thread_language:
            return redirect('/'+language.code, False)
    return redirect('/en', False)


def front_page_language(request,language):
    image_array = Image.objects.all()[:7]
    return render_to_response('users/front_page.html', {'image_array': image_array, 'request_language': language}, context_instance=RequestContext(request))


# Custom 404 and 500
def my_custom_404_view(request):
    return render_to_response('template/404.html',
                              context_instance=RequestContext(request))


def my_custom_500_view(request):
    return render_to_response('template/500.html',
                              context_instance=RequestContext(request))

# Social Auth
def logged_in(request):
    return redirect('/', False)


def login_error(request):
    return render_to_response('users/signup.html', {'error_message': "Incorrect login. Please try again"},
                              context_instance=RequestContext(request))

# Contact Form
def contact(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
        error_message = message_contains_url(request.POST['contact_comment'])
        if error_message:
            try:
                data = {'contact_email': request.POST['contact_email'], 'contact_name': request.POST['contact_name'], 'contact_message': request.POST['contact_message']}
            except:
                data = {}
        else:
            if form.is_valid():
                contact_name = form.cleaned_data['contact_name']
                contact_email = form.cleaned_data['contact_email']
                contact_comment = form.cleaned_data['contact_comment']
                subject = 'Contact Form ' + Record.objects.get(key='WEBSITE_NAME').value + ': \'' + contact_name + '\': \'' + contact_email + '\''
                recipients = settings.ADMIN_USERS_EMAILS
                sender = 'Contact Form ' + Record.objects.get(key='WEBSITE_NAME').value + " <" + settings.SERVER_EMAIL + ">"
                from google.appengine.api import mail
                mail.send_mail(sender=sender, to=recipients, subject=subject, body=contact_comment)
                return HttpResponseRedirect('/thanks/')
    else:
        form = ContactForm()
        error_message = ''
    return render(request, 'users/contact.html', {'form': form, 'error_message': error_message,'request_language':'en'})

def message_contains_url(message):
    from django.utils.html import urlize
    import re, string
    error_message = False
    # Strip Non Alpha Numeric
    message = re.sub(r'[^a-zA-Z0-9\.]',' ', message)
    if (urlize(message) != message) or message.find('buy') > 0 or message.find('shop') > 0:
        error_message = 'Please do not include links or emails in the message. Sorry for the inconvenience.'
    return error_message

def thanks(request):
    return render_to_response(request, 'users/thanks.html')

# ...
def user_form(request, id=None):
    if is_admin_user(request):
        instance = get_object_or_404(User, id=id) if id is not None else None
        form = UserForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/users/')
        return render_to_response("users/user_form.html", {"form": form, "id": id}, context_instance=RequestContext(request))
    else:
        return redirect('/', False)

# ...
def user_list(request):
    if is_admin_user(request):
        return render_to_response("users/user_list.html", {"user_list": User.objects.all()}, context_instance=RequestContext(request))
    else:
        return redirect('/', False)

# ...
def user_delete(request, id=None):
    if is_admin_user(request):
        instance = get_object_or_404(User, id=id) if id is not None else None
        instance.delete()
        return redirect('/users/')
    else:
        return redirect('/', False)
    

# ...
def is_admin_user(request):
    try:
        if request.user.email in settings.ADMIN_USERS:
            return True
        else:
            return False
    except:
        return False
