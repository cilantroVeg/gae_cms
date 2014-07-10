from django.conf.urls import *
from django.views.generic import RedirectView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
    # Admin URL's
    url(r'^admin/', include(admin.site.urls)),
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),
    url('', include('social.apps.django_app.urls', namespace='social')),

    # User Session
    url(r'^enter/', 'users.views.enter'),
    url(r'^exit/', 'users.views.exit_request'),
    url(r'^process_sign_up/', 'users.views.process_sign_up'),
    url(r'^process_create_account/', 'users.views.process_create_account'),
    (r'', include('django.contrib.auth.urls')),
    url(r'^logged-in/', 'users.views.logged_in'),
    url(r'^login-error/', 'users.views.login_error'),

    # Page - languages
    url(r'^language/new/$', 'pages.views.language_form'),
    url(r'^language/edit/(?P<id>\d+)/$', 'pages.views.language_form'),
    url(r'^language/delete/(?P<id>\d+)/$', 'pages.views.language_delete'),
    url(r'^languages/', 'pages.views.language_list'),

    # Frontpage
    url('^$', 'pages.views.front_page'),
    url(r'^(?P<language>[a-z]{2})$', 'pages.views.front_page_language'),
    url(r'^contact/', 'pages.views.contact'),
    url(r'^thanks/', 'pages.views.thanks'),

    # Page - categories
    url(r'^category/new/$', 'pages.views.category_form'),
    url(r'^category/edit/(?P<id>\d+)/$', 'pages.views.category_form'),
    url(r'^category/edit/$', 'pages.views.category_formset'),
    url(r'^category/delete/(?P<id>\d+)/$', 'pages.views.category_delete'),
    url(r'^categories/', 'pages.views.category_list'),
    url(r'^(?P<language>[a-z]{2})/categories/$', 'pages.views.category_list'),
    url(r'^(?P<language>[a-z]{2})/c/(?P<slug>[-\w]+)/$', 'pages.views.category_view'),

    # Page - pages
    url(r'^page/new/$', 'pages.views.page_form'),
    url(r'^page/edit/(?P<id>\d+)/$', 'pages.views.page_form'),
    url(r'^page/delete/(?P<id>\d+)/$', 'pages.views.page_delete'),
    url(r'^pages/', 'pages.views.page_list'),
    url(r'^(?P<language>[a-z]{2})/(?P<slug>[-\w]+)/$', 'pages.views.page_view'),
    url(r'^api/$', 'pages.views.page_api'),

    # Page - images
    url(r'^image/new/$', 'pages.views.image_form'),
    url(r'^image/edit/(?P<id>\d+)/$', 'pages.views.image_form'),
    url(r'^image/delete/(?P<id>\d+)/$', 'pages.views.image_delete'),
    url(r'^images/', 'pages.views.image_list'),
    url(r'^(?P<language>[a-z]{2})/i/(?P<slug>[-\w]+)/$', 'pages.views.image_view'),

    # Page - records
    url(r'^record/new/$', 'pages.views.record_form'),
    url(r'^record/edit/(?P<id>\d+)/$', 'pages.views.record_form'),
    url(r'^record/delete/(?P<id>\d+)/$', 'pages.views.record_delete'),
    url(r'^records/', 'pages.views.record_list'),
    
    # Page - feed_archives
    url(r'^feed_archive/new/$', 'pages.views.feed_archive_form'),
    url(r'^feed_archive/edit/(?P<id>\d+)/$', 'pages.views.feed_archive_form'),
    url(r'^feed_archive/delete/(?P<id>\d+)/$', 'pages.views.feed_archive_delete'),
    url(r'^feed_archives/', 'pages.views.feed_archive_list'),
    
    # Page - feed_sources
    url(r'^feed_source/new/$', 'pages.views.feed_source_form'),
    url(r'^feed_source/edit/(?P<id>\d+)/$', 'pages.views.feed_source_form'),
    url(r'^feed_source/delete/(?P<id>\d+)/$', 'pages.views.feed_source_delete'),
    url(r'^feed_sources/', 'pages.views.feed_source_list'),

    # Page - spreadsheets
    url(r'^spreadsheet/new/$', 'pages.views.spreadsheet_form'),
    url(r'^spreadsheet/edit/(?P<id>\d+)/$', 'pages.views.spreadsheet_form'),
    url(r'^spreadsheet/delete/(?P<id>\d+)/$', 'pages.views.spreadsheet_delete'),
    url(r'^spreadsheets/', 'pages.views.spreadsheet_list'),

    # sitemap
    url(r'^sitemap/', 'pages.views.sitemap'),

    # users
    url(r'^user/new/$', 'users.views.user_form'),
    url(r'^user/edit/(?P<id>\d+)/$', 'users.views.user_form'),
    url(r'^user/delete/(?P<id>\d+)/$', 'users.views.user_delete'),
    url(r'^users/', 'users.views.user_list'),

    # Admin
    url(r'^delete_cache/', 'pages.views.delete_cache'),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/template/simple/favicon.ico')),

    # API InterPegasus CMS
    url(r'^(?P<language>[a-z]{2})/i/(?P<slug>[-\w]+)/$', 'pages.views.image_view'),

    url(r'^api/(?P<language_code>[a-z]{2})/languages', 'pages.api.languages'),
    url(r'^api/(?P<language_code>[a-z]{2})/categories', 'pages.api.categories'),
    url(r'^api/(?P<language_code>[a-z]{2})/pages', 'pages.api.pages'),
    url(r'^api/(?P<language_code>[a-z]{2})/images', 'pages.api.images'),
)

handler404 = 'pages.views.my_custom_404_view'
handler500 = 'pages.views.my_custom_500_view'