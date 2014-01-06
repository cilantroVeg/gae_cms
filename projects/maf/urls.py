from django.conf.urls import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
    # Admin URL's
    url(r'^admin/', include(admin.site.urls)),
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),
    url('', include('social.apps.django_app.urls', namespace='social')),

    # Frontpage
    url('^$', 'users.views.front_page'),
    url(r'^(?P<language>[a-z]{2})$', 'users.views.front_page_language'),


    # User Session
    url(r'^en/enter/', 'users.views.enter'),
    url(r'^en/exit/', 'users.views.exit_request'),
    url(r'^en/process_sign_up/', 'users.views.process_sign_up'),
    url(r'^en/process_create_account/', 'users.views.process_create_account'),
    (r'', include('django.contrib.auth.urls')),
    url(r'^en/logged-in/', 'users.views.logged_in'),
    url(r'^en/login-error/', 'users.views.login_error'),
    url(r'^en/contact/', 'users.views.contact'),
    url(r'^en/thanks/', 'users.views.thanks'),

    # Page
    url(r'^en/language/new/$', 'pages.views.language_form'),
    url(r'^en/language/edit/(?P<id>\d+)/$', 'pages.views.language_form'),
    url(r'^en/language/delete/(?P<id>\d+)/$', 'pages.views.language_delete'),
    url(r'^en/languages/', 'pages.views.language_list'),

    url(r'^en/category/new/$', 'pages.views.category_form'),
    url(r'^en/category/edit/(?P<id>\d+)/$', 'pages.views.category_form'),
    url(r'^en/category/edit/$', 'pages.views.category_formset'),
    url(r'^en/category/delete/(?P<id>\d+)/$', 'pages.views.category_delete'),
    url(r'^en/categories/', 'pages.views.category_list'),
    url(r'^(?P<language>[a-z]{2})/c/(?P<slug>[-\w]+)/$', 'pages.views.category_view'),

    url(r'^en/page/new/$', 'pages.views.page_form'),
    url(r'^en/page/edit/(?P<id>\d+)/$', 'pages.views.page_form'),
    url(r'^en/page/delete/(?P<id>\d+)/$', 'pages.views.page_delete'),
    url(r'^en/pages/', 'pages.views.page_list'),
    url(r'^(?P<language>[a-z]{2})/(?P<slug>[-\w]+)/$', 'pages.views.page_view'),

    url(r'^en/image/new/$', 'pages.views.image_form'),
    url(r'^en/image/edit/(?P<id>\d+)/$', 'pages.views.image_form'),
    url(r'^en/image/delete/(?P<id>\d+)/$', 'pages.views.image_delete'),
    url(r'^en/images/', 'pages.views.image_list'),
    url(r'^(?P<language>[a-z]{2})/i/(?P<slug>[-\w]+)/$', 'pages.views.image_view'),

    url(r'^en/record/new/$', 'pages.views.record_form'),
    url(r'^en/record/edit/(?P<id>\d+)/$', 'pages.views.record_form'),
    url(r'^en/record/delete/(?P<id>\d+)/$', 'pages.views.record_delete'),
    url(r'^en/records/', 'pages.views.record_list'),
    
    url(r'^en/spreadsheet/new/$', 'pages.views.spreadsheet_form'),
    url(r'^en/spreadsheet/edit/(?P<id>\d+)/$', 'pages.views.spreadsheet_form'),
    url(r'^en/spreadsheet/delete/(?P<id>\d+)/$', 'pages.views.spreadsheet_delete'),
    url(r'^en/spreadsheets/', 'pages.views.spreadsheet_list'),

    url(r'^en/sitemap/', 'pages.views.sitemap'),
    
    
    url(r'^en/user/new/$', 'users.views.user_form'),
    url(r'^en/user/edit/(?P<id>\d+)/$', 'users.views.user_form'),
    url(r'^en/user/delete/(?P<id>\d+)/$', 'users.views.user_delete'),
    url(r'^en/users/', 'users.views.user_list'),

    # Admin

    url(r'^en/delete_cache/', 'pages.views.delete_cache'),


)


handler404 = 'users.views.my_custom_404_view'
handler500 = 'users.views.my_custom_500_view'