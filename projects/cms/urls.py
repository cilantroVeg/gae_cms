from django.conf.urls import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),
    url('^$', 'users.views.front_page'),
    # User Session
    url(r'^enter/', 'users.views.enter'),
    url(r'^exit/', 'users.views.exit_request'),
    url(r'^forgot_password/', 'users.views.forgot_password'),
    url(r'^process_sign_up/', 'users.views.process_sign_up'),
    url(r'^process_create_account/', 'users.views.process_create_account'),
    url(r'^process_forgot_password/', 'users.views.process_forgot_password'),
)


handler404 = 'users.views.my_custom_404_view'
handler500 = 'users.views.my_custom_500_view'