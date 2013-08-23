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
    image_array = Image.objects.all()[:7]
    return render_to_response('users/front_page.html', {'image_array': image_array},
                                  context_instance=RequestContext(request))

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


def thanks(request):
    return render(request, 'users/thanks.html')

# ...
def user_form(request, id=None):
    if is_admin(request):
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
    if is_admin(request):
        return render_to_response("users/user_list.html", {"user_list": User.objects.all()}, context_instance=RequestContext(request))
    else:
        return redirect('/', False)

# ...
def user_delete(request, id=None):
    if is_admin(request):
        instance = get_object_or_404(User, id=id) if id is not None else None
        instance.delete()
        return redirect('/users/')
    else:
        return redirect('/', False)
