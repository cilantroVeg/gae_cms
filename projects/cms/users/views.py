# https://docs.djangoproject.com/en/dev/topics/auth/default/
import logging
import pprint
from users.models import *
log = logging.getLogger(__name__)
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate
from django.contrib.auth import logout
#from django.contrib.auth.models import Group, Permission
#from django.contrib.contenttypes.models import ContentType



#######################
# User Related Methods
#######################


def is_logged_in(request):
    if not request.user.is_authenticated():
        return False
    else:
        return True


def enter(request):
    if is_logged_in(request):
        return redirect('/', False)
    return render_to_response('users/signup.html', {'is_logged_in': is_logged_in(request)},
                              context_instance=RequestContext(request))


def not_found(request):
    return render_to_response('template/404.html', {'is_logged_in': is_logged_in(request)},
                              context_instance=RequestContext(request))


def exit_request(request):
    logout(request)
    request.session['is_logged_in'] = False
    request.session['email'] = None
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
    request.session['is_logged_in'] = True
    request.session['email'] = request.POST['email']
    request.session['user_id'] = User.id
    return redirect('/', False)


@require_http_methods(["POST"])
def process_sign_up(request):
    username = request.POST['email_2']
    password = request.POST['password_2']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            request.session['is_logged_in'] = True
            request.session['email'] = request.POST['email_2']
            # Redirect to a success page.
            return redirect('/', False)
    else:
        # Return an 'invalid login' error message.
        return render_to_response('users/signup.html', {'error_message': "Email and Password Don't Match"},
                                  context_instance=RequestContext(request))


def front_page(request):
    for key, value in request.session.items(): # .iteritems() in Python 2.x
        pprint.pprint(value)
    if is_logged_in(request) is False:
        return render_to_response('users/signup.html', {'is_logged_in': is_logged_in(request)},
                                  context_instance=RequestContext(request))
    else:
        return render_to_response('users/front_page.html', {'is_logged_in': is_logged_in(request)},
                                  context_instance=RequestContext(request))

# Custom 404 and 500
def my_custom_404_view(request):
    return render_to_response('template/404.html', {'is_logged_in': is_logged_in(request)},
                              context_instance=RequestContext(request))

def my_custom_500_view(request):
    return render_to_response('template/500.html', {'is_logged_in': is_logged_in(request)},
                              context_instance=RequestContext(request))

# Social Auth
def logged_in(request):
    request.session['is_logged_in'] = True
    return redirect('/', False)

def login_error(request):
    return render_to_response('users/signup.html', {'error_message': "Incorrect login. Please try again"},
                              context_instance=RequestContext(request))