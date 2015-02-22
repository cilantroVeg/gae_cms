# views.py

# imports
from pages.context_processors import *
from django.contrib.auth.models import *
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib.auth import login
import logging
logger = logging.getLogger(__name__)

################
# User Methods
################

# ...
def enter(request):
    from pages.context_processors import is_logged_in
    is_logged_in = is_logged_in(request)
    if is_logged_in['is_logged_in']:
        return redirect('/', False)
    else:
        return render_to_response('users/signup.html', context_instance=RequestContext(request))

# ...
def not_found(request):
    return render_to_response('template/404.html',context_instance=RequestContext(request))

# ...
def exit_request(request):
    logout(request)
    request.session = None
    return redirect('/', False)

# ...
@require_http_methods(["POST"])
def process_create_account(request):
    try:
        u = User.objects.filter(email=request.POST['email'])
    except:
        logger.error('views/process_create_account')
        u = False
    if u:
        return render_to_response('users/signup.html', {'error_message': "Email is already taken"}, context_instance=RequestContext(request))
    User.objects.create_user(request.POST['email'], request.POST['email'], request.POST['password'])
    user = authenticate(username=request.POST['email'], password=request.POST['password'])
    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect('/', False)
    else:
        return render_to_response('users/signup.html', {'error_message': "Email is already taken"}, context_instance=RequestContext(request))

# ...
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
        return render_to_response('users/signup.html', {'error_message': "Email and Password Don't Match"}, context_instance=RequestContext(request))

# ...
def logged_in(request):
    return redirect('/', False)

# ...
def login_error(request):
    return render_to_response('users/signup.html', {'error_message': "Incorrect login. Please try again"}, context_instance=RequestContext(request))

# ...
def user_form(request, id=None):
    if is_admin(request)['is_admin']:
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
    if is_admin(request)['is_admin']:
        return render_to_response("users/user_list.html", {"user_list": User.objects.all()}, context_instance=RequestContext(request))
    else:
        return redirect('/', False)

# ...
def user_delete(request, id=None):
    if is_admin(request)['is_admin']:
        instance = get_object_or_404(User, id=id) if id is not None else None
        instance.delete()
        return redirect('/users/')
    else:
        return redirect('/', False)
    
# ...
def user_profile_form(request, id=None):
    if is_admin(request)['is_admin']:
        instance = get_object_or_404(UserProfile, id=id) if id is not None else None
        form = UserProfileForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/user_profiles/')
        return render_to_response("users/user_profile_form.html", {"form": form, "id": id}, context_instance=RequestContext(request))
    else:
        return redirect('/', False)

# ...
def user_profile_list(request):
    if is_admin(request)['is_admin']:
        return render_to_response("users/user_profile_list.html", {"user_profile_list": UserProfile.objects.all()}, context_instance=RequestContext(request))
    else:
        return redirect('/', False)