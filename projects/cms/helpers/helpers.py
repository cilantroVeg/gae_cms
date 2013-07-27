from django.conf import settings


# ...
def is_logged_in(request):
    if not request.user.is_authenticated():
        return False
    else:
        return True

# ...
def is_admin_user(request):
    try:
        if request.user.email in settings.ADMIN_USERS:
            return True
        else:
            return False
    except:
        return False


