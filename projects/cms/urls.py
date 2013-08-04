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
    url(r'^contact/', 'users.views.contact'),
    url(r'^thanks/', 'users.views.thanks'),

    # Page
    url(r'^language/new/$', 'pages.views.language_form'),
    url(r'^language/edit/(?P<id>\d+)/$', 'pages.views.language_form'),
    url(r'^language/delete/(?P<id>\d+)/$', 'pages.views.language_delete'),
    url(r'^languages/', 'pages.views.language_list'),

    url(r'^category/new/$', 'pages.views.category_form'),
    url(r'^category/edit/(?P<id>\d+)/$', 'pages.views.category_form'),
    url(r'^category/delete/(?P<id>\d+)/$', 'pages.views.category_delete'),
    url(r'^categories/', 'pages.views.category_list'),

    url(r'^page/new/$', 'pages.views.page_form'),
    url(r'^page/edit/(?P<id>\d+)/$', 'pages.views.page_form'),
    url(r'^page/delete/(?P<id>\d+)/$', 'pages.views.page_delete'),
    url(r'^pages/', 'pages.views.page_list'),
    
    url(r'^record/new/$', 'pages.views.record_form'),
    url(r'^record/edit/(?P<id>\d+)/$', 'pages.views.record_form'),
    url(r'^record/delete/(?P<id>\d+)/$', 'pages.views.record_delete'),
    url(r'^records/', 'pages.views.record_list'),
    
    url(r'^spreadsheet/new/$', 'pages.views.spreadsheet_form'),
    url(r'^spreadsheet/edit/(?P<id>\d+)/$', 'pages.views.spreadsheet_form'),
    url(r'^spreadsheet/delete/(?P<id>\d+)/$', 'pages.views.spreadsheet_delete'),
    url(r'^spreadsheets/', 'pages.views.spreadsheet_list'),
    
    
    url(r'^user/new/$', 'users.views.user_form'),
    url(r'^user/edit/(?P<id>\d+)/$', 'users.views.user_form'),
    url(r'^user/delete/(?P<id>\d+)/$', 'users.views.user_delete'),
    url(r'^users/', 'users.views.user_list'),
    
    url(r'^image/new/$', 'pages.views.image_form'),
    url(r'^image/edit/(?P<id>\d+)/$', 'pages.views.image_form'),
    url(r'^image/delete/(?P<id>\d+)/$', 'pages.views.image_delete'),
    url(r'^images/', 'pages.views.image_list'),

    # Flickr Callback
    url(r'^flickr-callback/', 'pages.views.flickr_callback'),
)


handler404 = 'users.views.my_custom_404_view'
handler500 = 'users.views.my_custom_500_view'