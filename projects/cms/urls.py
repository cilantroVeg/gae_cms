from django.conf.urls import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
    # Admin URL's
    url(r'^admin/', include(admin.site.urls)),
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),

    # Frontpage
    url('^$', 'users.views.front_page'),

    # User Session
    url(r'^enter/', 'users.views.enter'),
    url(r'^exit/', 'users.views.exit_request'),
    url(r'^process_sign_up/', 'users.views.process_sign_up'),
    url(r'^process_create_account/', 'users.views.process_create_account'),
    url(r'', include('social_auth.urls')),
    (r'', include('django.contrib.auth.urls')),
    url(r'^logged-in/', 'users.views.logged_in'),
    url(r'^login-error/', 'users.views.login_error'),
)


handler404 = 'users.views.my_custom_404_view'
handler500 = 'users.views.my_custom_500_view'