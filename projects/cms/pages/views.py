# views.py

import gdata.photos.service
import gdata.media
import gdata.geo
import sys
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.conf import settings
from django.utils.html import *
from django.forms.formsets import formset_factory
from django.forms.models import modelformset_factory
from pages.models import *
from pages.context_processors import is_admin
from django.shortcuts import render
from pages.api import *
from django.utils.html import strip_tags
from django.views.decorators.csrf import csrf_exempt
import logging
from django.template.defaultfilters import removetags
from wikipedia import wikipedia
from bs4 import BeautifulSoup
from context_processors import *
from lxml.html.clean import clean_html
logger = logging.getLogger(__name__)

# ...
def delete_cache(request):
    from google.appengine.api import memcache
    memcache.flush_all()
    return redirect('/', False)

# ...
def category_form(request, id=None):
    if is_admin(request)['is_admin']:
        instance = get_object_or_404(Category, id=id) if id is not None else None
        form = CategoryForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/categories/')
        return render_to_response("pages/category_form.html", {"form": form, "id": id}, context_instance=RequestContext(request))
    else:
        return redirect('/', False)


# ...
def category_formset(request):
    if is_admin(request)['is_admin']:
        CategoryFormSet = modelformset_factory(Category, exclude="slug", extra=0)

        if request.POST:
            formset = CategoryFormSet(request.POST)
            if formset.is_valid():
                formset.save()
                return redirect('/categories/')
        else:
            formset = CategoryFormSet(initial=Category.objects.values())
        return render_to_response("pages/category_formset.html", {"formset": formset}, context_instance=RequestContext(request))
    else:
        return redirect('/', False)


# ...
def category_list(request):
    if is_admin(request)['is_admin']:
        return render_to_response("pages/category_list.html", {"category_list": Category.objects.all()}, context_instance=RequestContext(request))
    else:
        return redirect('/', False)

# ...
def category_delete(request, id=None):
    if is_admin(request)['is_admin']:
        instance = get_object_or_404(Category, id=id) if id is not None else None
        instance.delete()
        return redirect('/categories/')
    else:
        return redirect('/', False)


# ...
def language_form(request, id=None):
    if is_admin(request)['is_admin']:
        instance = get_object_or_404(Language, id=id) if id is not None else None
        form = LanguageForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/languages/')
        return render_to_response("pages/language_form.html", {"form": form, "id": id}, context_instance=RequestContext(request))
    else:
        return redirect('/', False)

# ...
def language_list(request):
    if is_admin(request)['is_admin']:
        return render_to_response("pages/language_list.html", {"language_list": Language.objects.all()}, context_instance=RequestContext(request))
    else:
        return redirect('/', False)

# ...
def language_delete(request, id=None):
    if is_admin(request)['is_admin']:
        instance = get_object_or_404(Language, id=id) if id is not None else None
        instance.delete()
        return redirect('/languages/')
    else:
        return redirect('/', False)

# ...
def gallery_form(request, id=None):
    if is_admin(request)['is_admin']:
        instance = get_object_or_404(Gallery, id=id) if id is not None else None
        if instance:
            image_array = Image.objects.filter(gallery=instance)
        else:
            image_array = None
        gallery_form = GalleryForm(request.POST or None, instance=instance)
        if gallery_form.is_valid():
            gallery = gallery_form.save(commit=False)
            gallery.save()
            return redirect('/galleries/')
        return render_to_response("pages/gallery_form.html", {"gallery_form": gallery_form, "id": id, "user": request.user.id, 'image_array': image_array}, context_instance=RequestContext(request))
    else:
        return redirect('/', False)

# ...
def gallery_list(request):
    if is_admin(request)['is_admin']:
        return render_to_response("pages/gallery_list.html", {"gallery_list": Gallery.objects.all()}, context_instance=RequestContext(request))
    else:
        return redirect('/', False)

# ...
def gallery_delete(request, id=None):
    if is_admin(request)['is_admin']:
        instance = get_object_or_404(Gallery, id=id) if id is not None else None
        instance.delete()
        return redirect('/galleries/')
    else:
        return redirect('/', False)




# ...
def page_form(request, id=None):
    if is_admin(request)['is_admin']:
        instance = get_object_or_404(Page, id=id) if id is not None else None
        if instance:
            image_array = Image.objects.filter(page=instance)
        else:
            image_array = None
        page_form = PageForm(request.POST or None, instance=instance)
        if page_form.is_valid():
            page = page_form.save(commit=False)
            page.user = request.user
            page.save()
            return redirect('/pages/')
        return render_to_response("pages/page_form.html", {"page_form": page_form, "id": id, "user": request.user.id, 'image_array': image_array}, context_instance=RequestContext(request))
    else:
        return redirect('/', False)

# ...
def page_list(request):
    if is_admin(request)['is_admin']:
        return render_to_response("pages/page_list.html", {"page_list": Page.objects.all()}, context_instance=RequestContext(request))
    else:
        return redirect('/', False)

# ...
def page_delete(request, id=None):
    if is_admin(request)['is_admin']:
        instance = get_object_or_404(Page, id=id) if id is not None else None
        instance.delete()
        return redirect('/pages/')
    else:
        return redirect('/', False)

# ...
def record_form(request, id=None):
    if is_admin(request)['is_admin']:
        instance = get_object_or_404(Record, id=id) if id is not None else None
        form = RecordForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/records/')
        return render_to_response("pages/record_form.html", {"form": form, "id": id}, context_instance=RequestContext(request))
    else:
        return redirect('/', False)

# ...
def record_list(request):
    if is_admin(request)['is_admin']:
        return render_to_response("pages/record_list.html", {"record_list": Record.objects.all()}, context_instance=RequestContext(request))
    else:
        return redirect('/', False)

# ...
def record_delete(request, id=None):
    if is_admin(request)['is_admin']:
        instance = get_object_or_404(Record, id=id) if id is not None else None
        instance.delete()
        return redirect('/records/')
    else:
        return redirect('/', False)

# ...
def feed_form(request, id=None):
    if is_admin(request)['is_admin']:
        instance = get_object_or_404(Feed, id=id) if id is not None else None
        form = FeedForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/feeds/')
        return render_to_response("pages/feed_form.html", {"form": form, "id": id}, context_instance=RequestContext(request))
    else:
        return redirect('/', False)

# ...
def feed_list(request):
    if is_admin(request)['is_admin']:
        return render_to_response("pages/feed_list.html", {"feed_list": Feed.objects.all()}, context_instance=RequestContext(request))
    else:
        return redirect('/', False)

# ...
def feed_delete(request, id=None):
    if is_admin(request)['is_admin']:
        instance = get_object_or_404(Feed, id=id) if id is not None else None
        instance.delete()
        return redirect('/feeds/')
    else:
        return redirect('/', False)

# ...
def advertisement_form(request, id=None):
    if is_admin(request)['is_admin']:
        instance = get_object_or_404(Advertisement, id=id) if id is not None else None
        form = AdvertisementForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/advertisements/')
        return render_to_response("pages/advertisement_form.html", {"form": form, "id": id}, context_instance=RequestContext(request))
    else:
        return redirect('/', False)

# ...
def advertisement_list(request):
    if is_admin(request)['is_admin']:
        return render_to_response("pages/advertisement_list.html", {"advertisement_list": Advertisement.objects.all()}, context_instance=RequestContext(request))
    else:
        return redirect('/', False)

# ...
def advertisement_delete(request, id=None):
    if is_admin(request)['is_admin']:
        instance = get_object_or_404(Advertisement, id=id) if id is not None else None
        instance.delete()
        return redirect('/advertisements/')
    else:
        return redirect('/', False)

def get_category_tree(request):
    return True


def get_sub_categories(request):
    return True


def get_pages_by_category(request):
    return True


def get_page_content(request):
    return True


# ...
def spreadsheet_form(request, id=None):
    if is_admin(request)['is_admin']:
        instance = get_object_or_404(Spreadsheet, id=id) if id is not None else None
        form = SpreadsheetForm(request.POST or None, request.FILES or None, instance=instance)
        if form.is_valid():
            spreadsheet = form.save(commit=False)
            spreadsheet.name = request.POST['name']
            spreadsheet.spreadsheet_file = request.FILES['spreadsheet_file'].name
            spreadsheet.size = request.FILES['spreadsheet_file'].size
            spreadsheet.save()
            handle_spreadsheet(request.FILES['spreadsheet_file'], request.user, spreadsheet)
            return redirect('/spreadsheets/')
        return render_to_response("pages/spreadsheet_form.html", {"form": form, "id": id}, context_instance=RequestContext(request))
    else:
        return redirect('/', False)

# ...
def handle_spreadsheet(f, user, spreadsheet):
    import xlrd

    workbook = xlrd.open_workbook(file_contents=f.read())
    worksheets = workbook.sheet_names()
    for worksheet_name in worksheets:
        worksheet = workbook.sheet_by_name(worksheet_name)
        num_of_rows = worksheet.nrows
        if (num_of_rows != 0):
            for i in range(num_of_rows):
                if i == 0:
                    continue
                language_code = worksheet.cell(i, 0).value
                category_name = worksheet.cell(i, 1).value
                parent_category_name = worksheet.cell(i, 2).value
                page_title = worksheet.cell(i, 3).value
                page_content = worksheet.cell(i, 4).value
                image_urls = worksheet.cell(i, 5).value
                try:
                    extra = worksheet.cell(i, 6).value
                except:
                    logger.error('views/handle_spreadsheet')
                    extra = None
                # Language
                language, language_created = Language.objects.get_or_create(code=language_code,  defaults={'name': language_code})
                # Categories
                parent, parent_created = Category.objects.get_or_create(name=parent_category_name,
                                                                        defaults={'parent': None, 'language': language,
                                                                                  'allow_replies': True})
                category, category_created = Category.objects.get_or_create(name=category_name,
                                                                            defaults={'parent': parent,
                                                                                      'language': language,
                                                                                      'allow_replies': True})
                # Page
                page, created = Page.objects.get_or_create(category=category, title=strip_tags(page_title), defaults={'user': user})
                page.content = strip_tags(page_content)
                page.spreadsheet = spreadsheet
                page.save()


# ...
def spreadsheet_list(request):
    if is_admin(request)['is_admin']:
        return render_to_response("pages/spreadsheet_list.html", {"spreadsheet_list": Spreadsheet.objects.all(),
                                                                  },
                                  context_instance=RequestContext(request))
    else:
        return redirect('/', False)

# ...
def spreadsheet_delete(request, id=None):
    if is_admin(request)['is_admin']:
        instance = get_object_or_404(Spreadsheet, id=id) if id is not None else None
        instance.delete()
        return redirect('/spreadsheets/')
    else:
        return redirect('/', False)



def image_form(request, id=None):
    if is_admin(request)['is_admin']:
        instance = get_object_or_404(Image, id=id) if id is not None else None
        form = ImageForm(request.POST or None, request.FILES or None, instance=instance)
        if form.is_valid():
            image = form.save(commit=False)
            image.name = request.POST['name']
            image.description = form.cleaned_data['description']
            image.image_file = request.FILES['image_file'].name
            image.size = request.FILES['image_file'].size
            image.save()
            handle_image_picasa(request.FILES['image_file'], image)
            return redirect('/images/')
        else:
            return render_to_response("pages/image_form.html",
                                      {"form": form, "id": id},
                                      context_instance=RequestContext(request))

    else:
        return redirect('/', False)

# ...
def connect_picasa():
    gd_client = gdata.photos.service.PhotosService()
    gd_client.email = settings.PICASA_KEY
    gd_client.password = settings.PICASA_PASSWORD
    gd_client.source = 'exampleCo-exampleApp-1'
    gd_client.ProgrammaticLogin()
    return gd_client


def delete_picasa_photo(instance):
    try:
        gd_client = connect_picasa()
        photos = gd_client.GetFeed('/data/feed/api/user/%s/albumid/%s?kind=photo' % ('default', instance.picasa_album_id))
        for photo in photos.entry:
            if photo.gphoto_id.text == instance.picasa_photo_id:
                gd_client.Delete(photo)
    except:
        logger.error('views/delete_picasa_photo')
        return False

# ...
def handle_image_picasa(file, image, description=None,url_slug=''):
    from google.appengine.api import urlfetch
    urlfetch.set_default_fetch_deadline(120)
    gd_client = connect_picasa()
    try:
        current_album = None
        albums = gd_client.GetUserFeed()
        for album in albums.entry:
            if album.title.text == settings.APP_NAME:
                current_album = album
        if current_album is None:
            album = gd_client.InsertAlbum(title=settings.APP_NAME, summary='Photos from ' + settings.SITE_URL)
    except:
        logger.error('views/handle_image_picasa')
        album = gd_client.InsertAlbum(title=settings.APP_NAME, summary='Photos from ' + settings.SITE_URL)

    album_url = '/data/feed/api/user/%s/albumid/%s' % ('default', album.gphoto_id.text)
    image_name = image.name if image.name else 'Image'
    if description:
        image_description = description + ' ' + settings.SITE_URL + url_slug
    else:
        image_description = 'Image From ' + settings.SITE_URL + url_slug
    photo = gd_client.InsertPhotoSimple(album_url, strip_tags(image_name), strip_tags(image_description) , file, content_type='image/jpeg')
    image.picasa_album_id = album.gphoto_id.text
    image.picasa_photo_id = photo.gphoto_id.text
    import re
    thumb = re.sub('s72','s320',photo.media.thumbnail[0].url)
    medium = re.sub('s72','s1024',photo.media.thumbnail[0].url)
    full = re.sub('s72','s2048',photo.media.thumbnail[0].url)
    image.picasa_thumb_url = thumb
    picasa_medium_url = medium
    image.picasa_photo_url = full #photo.content.src
    image.save()
    return photo

# ...
def image_list(request):
    if is_admin(request)['is_admin']:
        return render_to_response("pages/image_list.html", {"image_list": Image.objects.order_by('gallery','order','name'),"gallery_list": Gallery.objects.order_by('name')}, context_instance=RequestContext(request))
    else:
        return redirect('/', False)

# ...
def image_delete(request, id=None):
    if is_admin(request)['is_admin']:
        instance = get_object_or_404(Image, id=id) if id is not None else None
        filename = instance.name
        delete_picasa_photo(instance)
        instance.delete()
        json = request.GET.get('json', 'false')
        if json == 'true':
            file_dictionary = {}
            files_array = []
            image_dictionary = {}
            image_dictionary[str(filename)] = True
            files_array.append(image_dictionary)
            file_dictionary["files"] = files_array
            import json
            return HttpResponse(json.dumps(file_dictionary), content_type="application/json",status=200)
        else:
            return redirect('/images/')
    else:
        return redirect('/', False)


# ...
def page_view(request, language, slug):
    page = get_object_or_404(Page, slug=slug)
    if is_wiki(page):
        wiki_page = process_wiki_page(language,page)
    else:
        wiki_page = None
    image_array = Image.objects.filter(page=page)
    if settings.APP_NAME == 'happy-planet':
        try:
            endangered_species = query_api(language, 'pages',{'category_slug': 'endangered-species'})['pages']
            keystone_species = query_api(language, 'pages',{'category_slug': 'endangered-species'})['pages']
        except:
            logger.error('views/page_view')
            endangered_species = None
    return render_to_response("pages/page_view.html", {"page": page,"image_array":image_array, "wiki_page":wiki_page, "endangered_species":endangered_species, "keystone_species":keystone_species},context_instance=RequestContext(request))

#...
def is_wiki(page):
    parent_category = Category.objects.get(slug=page.category.slug)
    if parent_category and (parent_category.parent.slug == 'wiki'):
        return True
    else:
        return False

#...
def process_wiki_page(language_code,page, cache_enabled=settings.CACHE_ENABLED):
    wiki_page = {}
    # Get data from cache
    key = slugify(str(language_code) + '_WIKI_' + str(page.title))
    data = get_cache(key)
    if data and cache_enabled:
        wiki_page = data
    else:
        try:
            p = wikipedia.page(page.title)
        except:
            try:
                p = wikipedia.page(page.title)
            except:
                logger.error('process_wiki_page')
        if p is None:
            return wiki_page

        wiki_page["url"] = p.url
        wiki_page["title"] = p.title
        wiki_page["html"] = removetags(p.html(),'a b i small script br')
        wiki_page["summary"] = p.summary
        wiki_page["infobox"] = get_wikipedia_info_box(wiki_page["html"])
        # CLEAN
        set_cache(key,wiki_page)

    return wiki_page

def get_wikipedia_info_box(html):
    soup = BeautifulSoup(html)
    wiki_table = soup.find("table", class_="infobox biota")
    #wiki_table.find('th').contents[0].replaceWith(p.title)
    #return clean_html(wiki_table.find('th').contents[0].replaceWith('title'))
    return clean_html(wiki_table.prettify())

# ...
def gallery_view(request, language, slug):
    if settings.APP_NAME == 'arturopegasus7':
        gallery = get_object_or_404(Gallery, slug=slug)
        if gallery:
            image_list = get_image_list(gallery.id)
        else:
            image_list = None
        return render_to_response('users/template.html', {'gallery':gallery,'image_list':image_list,'is_admin':is_admin(request)['is_admin']}, context_instance=RequestContext(request))
    else:
        return render_to_response("template/arturopegasus7/template-frontpage.html", {"gallery": gallery,"image_array":image_array},context_instance=RequestContext(request))

# ...
def page_feed_view(request, language, slug):
    feed_pages = query_api(language, 'feed_pages')
    page = None
    if 'pages' in feed_pages:
        for key in feed_pages['pages']:
            if feed_pages['pages'][key]:
                for p in feed_pages['pages'][key]:
                    if p['slug'] == slug:
                        page = p
    if settings.APP_NAME == 'happy-planet':
        try:
            endangered_species = query_api(language, 'pages',{'category_slug': 'endangered-species'})['pages']
            keystone_species = query_api(language, 'pages',{'category_slug': 'endangered-species'})['pages']
        except:
            logger.error('views/page_view')
            endangered_species = None
    if page:
        return render_to_response("pages/page_view.html", {"page": page,"endangered_species":endangered_species,"keystone_species":keystone_species},context_instance=RequestContext(request))
    else:
        language = get_request_language(request)["request_language"]
        galleries = query_api(language, 'galleries')
        images = query_api(language, 'images')
        pages = query_api(language, 'pages')
        categories = query_api(language, 'categories')
        feeds = query_api(language, 'feed_pages')
        return render_to_response("pages/sitemap.html", {"galleries":galleries,"images":images,"pages":pages,"categories":categories,"feeds":feeds},context_instance=RequestContext(request))

# ...
def page_api(request):
    return render_to_response("pages/page_api.html",context_instance=RequestContext(request))

# ...
def sitemap(request):
    media = 'text'
    response_format = 'json'
    if settings.APP_NAME == 'bible-love':
        languages = bible_languages(request,media,response_format)
        return render_to_response("pages/sitemap-bible.html", {'languages':languages},context_instance=RequestContext(request))
    else:
        language = get_request_language(request)["request_language"]
        pages = query_api(language, 'pages')
        categories = query_api(language, 'categories')
        feeds = query_api(language, 'feed_pages')
        galleries = query_api(language, 'galleries')
        images = query_api(language, 'images')
        return render_to_response("pages/sitemap.html", {"galleries":galleries,"images":images,"pages":pages,"categories":categories,"feeds":feeds},context_instance=RequestContext(request))

# ...
def sitemap_xml(request):
    media = 'text'
    response_format = 'json'
    if settings.APP_NAME == 'bible-love':
        languages = bible_languages(request,media,response_format)
        return render_to_response("pages/sitemap.xml", {'languages':languages},context_instance=RequestContext(request),content_type="application/xhtml+xml")
    else:
        return render_to_response("pages/sitemap.html", {},
                                  context_instance=RequestContext(request))

# ...
def sitemap_xml_language(request,language):
    media = 'text'
    response_format = 'json'
    # Get language_family_code
    language_family_code = 'eng'
    languages = bible_languages(request,media,response_format)
    language_item = search_dictionaries('language_family_iso', language, languages)
    if language_item:
        language_family_iso = language_item[0]['language_family_iso']
        language_family_code = language_item[0]['language_family_code']
        # Bible List
        bibles = bible_list(request,media,language_family_code.lower(),response_format)
    else:
        bibles = []
    return render_to_response("pages/sitemap-page.xml", {'language':language,'bibles': bibles},context_instance=RequestContext(request),content_type="application/xhtml+xml")

# ...
def category_view(request, language, slug):
    language = Language.objects.filter(code=language)[:1]
    category = get_object_or_404(Category, slug=slug, language_id=language[0].id)
    pages = Page.objects.filter(category=category)
    return render_to_response("pages/category_view.html", {"category": category, "pages": pages},context_instance=RequestContext(request))

# ...
def image_view(request, language, slug):
    image = get_object_or_404(Image, slug=slug)
    return render_to_response("pages/image_view.html", {"image": image,
                                                        },
                              context_instance=RequestContext(request))

# ...
def debug(key, value):
    import logging

    logging.getLogger().setLevel(logging.DEBUG)
    logging.info("*******************************")
    logging.info(key)
    logging.info(value)
    logging.info("*******************************")


def delete_all():
    category_array = Category.objects.all()
    page_array = Page.objects.all()
    ss_array = Spreadsheet.objects.all()
    for page in page_array:
        print page.title
        Page.objects.filter(id=page.id).delete()
    for category in category_array:
        print category.name
        Category.objects.filter(id=category.id).delete()
    for ss in ss_array:
        print ss.name
        Spreadsheet.objects.filter(id=ss.id).delete()


# Contact Form
def contact(request):
    from api import captcha_is_valid
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
        captcha_response =  request.POST.get('g-recaptcha-response', None)
        captcha_is_valid = captcha_is_valid(captcha_response,request)
        error_message = message_contains_url(request.POST['contact_comment'])
        if error_message:
            try:
                data = {'contact_email': request.POST['contact_email'], 'contact_name': request.POST['contact_name'], 'contact_message': request.POST['contact_comment']}
            except:
                logger.error('views/contact')
                data = {}
        elif captcha_is_valid == False:
            data = {'contact_email': request.POST['contact_email'], 'contact_name': request.POST['contact_name'], 'contact_message': request.POST['contact_comment']}
            error_message = 'Captcha Issue'
        else:
            if form.is_valid():
                contact_name = form.cleaned_data['contact_name']
                contact_email = form.cleaned_data['contact_email']
                contact_comment = form.cleaned_data['contact_comment']
                subject = 'Contact Form ' + Record.objects.filter(key='WEBSITE_NAME')[:1][0].value + ': \'' + contact_name + '\': \'' + contact_email + '\''
                recipients = settings.ADMIN_USERS_EMAILS
                sender = 'Contact Form ' + Record.objects.filter(key='WEBSITE_NAME')[:1][0].value + " <" + settings.SERVER_EMAIL + ">"
                from google.appengine.api import mail
                exit()
                mail.send_mail(sender=sender, to=recipients, subject=subject, body=contact_comment)
                return redirect('/thanks/',False)
    else:
        form = ContactForm()
        error_message = ''
    return render(request, 'users/contact.html', {'form': form, 'error_message': error_message, 'app_name': settings.APP_NAME})

def message_contains_url(message):
    from django.utils.html import urlize
    import re

    error_message = False
    # Strip Non Alpha Numeric
    message = re.sub(r'[^a-zA-Z0-9\.]',' ', message)
    if (urlize(message) != message) or message.find('buy') > 0 or message.find('shop') > 0:
        error_message = 'Please do not include links or emails in the message. Sorry for the inconvenience.'
    return error_message

def thanks(request):
    return render(request, 'users/thanks.html')

def front_page(request):
    from django.utils import translation
    thread_language = translation.get_language()
    if settings.APP_NAME == 'bible-love':
        if 'last_url' in request.session:
            if request.session['last_url']:
                return redirect(request.session['last_url'], False)
        languages = bible_languages(request,'text','json')
        for l in languages:
            if thread_language[0:3].lower() in l["language_family_iso"].lower():
                return redirect('/'+l["language_family_iso"].lower(), False)
        return redirect('/eng', False)
    else:
        languages = Language.objects.filter(is_enabled=True)
        for language in languages:
            if language.code in thread_language:
                if language.code != "":
                    return redirect('/'+language.code+'/', False)
        return redirect('/en/', False)

def front_page_language(request,language):
    if settings.APP_NAME == 'bible-love':
        return redirect('/eng', False)
    elif settings.APP_NAME == 'arturopegasus7':
        gallery = get_gallery()
        if gallery:
            image_list = get_image_list(gallery['id'])
        else:
            image_list = None
        return render_to_response('users/template.html', {'gallery':gallery,'image_list':image_list,'is_admin':is_admin(request)['is_admin']}, context_instance=RequestContext(request))
    elif settings.APP_NAME == 'arturoportfolio7':
        pages = get_page_list()
        return render_to_response('users/template.html', {'page_list':pages,'is_admin':is_admin(request)['is_admin']}, context_instance=RequestContext(request))
    elif settings.APP_NAME == 'happy-planet':
        language_code = 'en' if (language is None) else language
        try:
            feed_pages = query_api(language_code, 'feed_pages')['pages']
        except:
            logger.error('views/front_page_language')
            feed_pages = None
        try:
            endangered_species = query_api(language_code, 'pages',{'category_slug': 'endangered-species'})['pages']
        except:
            logger.error('views/front_page_language')
            endangered_species = None
        return render_to_response('users/template.html', {'feed_pages':feed_pages, 'endangered_species':endangered_species, 'is_admin':is_admin(request)['is_admin']}, context_instance=RequestContext(request))
    else:
        image_array = Image.objects.all()[:7]
        language_code = 'en' if (language is None) else language
        try:
            feed_pages = query_api(language_code, 'feed_pages')
            feed_pages = feed_pages['pages'] if feed_pages else None
        except:
            logger.error('views/front_page_language')
            feed_pages = None
    return render_to_response('users/template.html', {'feed_pages':feed_pages, 'image_array': image_array,'is_admin':is_admin(request)['is_admin']}, context_instance=RequestContext(request))

def get_gallery(gallery_id=None):
    gallery = None
    if gallery_id:
        gallery_item = Gallery.objects.filter(id=gallery_id)[:1]
    else:
        gallery_item = Gallery.objects.filter(is_enabled=True,is_default=True)[:1]
    if not gallery_item:
        gallery_item = Gallery.objects.filter(is_enabled=True)[:1]
    if gallery_item:
        gallery = {}
        gallery['id'] = gallery_item[0].id
        gallery['name'] = gallery_item[0].name
        gallery['slug'] = gallery_item[0].slug
        gallery['description'] = gallery_item[0].description
    return gallery

def get_page_list():
    page_list = []
    pages = Page.objects.filter(is_enabled=True).order_by('priority','title')
    for page in pages:
        page_dictionary = {}
        page_dictionary["title"] = page.title
        page_dictionary["content"] = page.content
        if page.image_url:
            page_dictionary["image_url"] = page.image_url
        else:
            image = Image.objects.filter(page=page.id,is_enabled=True).order_by('order','name')[:1]
            if image and image[0]:
                page_dictionary["image_url"] = image[0].picasa_thumb_url
            else:
                page_dictionary["image_url"] = None
        page_dictionary["link_url"] = page.link_url
        page_list.append(page_dictionary)
    return page_list

def get_image_list(gallery_id):
    images = Image.objects.filter(gallery=gallery_id,is_enabled=True).order_by('order','name')
    image_list=[]
    if images:
        for image_item in images:
            image = {}
            image['id'] = image_item.id
            image['name'] = image_item.name
            image['description'] = image_item.description
            image['slug'] = image_item.slug
            image['picasa_photo_url'] = image_item.picasa_photo_url
            image['picasa_medium_url'] = image_item.picasa_medium_url
            image['picasa_thumb_url'] = image_item.picasa_thumb_url
            image_list.append(image)
    return image_list

def front_page_language_family_iso(request,language,bible=None,book=None,chapter=None):
    if settings.APP_NAME != 'bible-love':
        return redirect('/', False)
    media = 'text'
    response_format = 'json'
    languages = bible_languages(request,media,response_format)
    language_item = search_dictionaries('language_family_iso', language, languages)
    if language_item:
        language_family_iso = language_item[0]['language_family_iso']
        language_family_code = language_item[0]['language_family_code']
        # Bible List
        bibles = bible_list(request,media,language_family_code.lower(),response_format)
        if bible:
            current_bible = search_dictionaries('dam_id', bible, bibles)[0]
        else:
            current_bible = bibles[0]
        # Get Book
        if language_family_iso == 'heb':
            current_bible['right_to_left'] = 'true'
        books = bible_books(request,current_bible['dam_id'],response_format)
        if books is None:
            return redirect('/eng', False)
        if book:
            current_book = search_dictionaries('book_id', book, books)[0]
        else:
            current_book = books[0]
        if chapter:
            chapter = bible_book_text(request,current_bible['dam_id'], current_book['book_id'], chapter.lower(), response_format)
        else:
            chapter = bible_book_text(request,current_bible['dam_id'], current_book['book_id'], current_book['chapters'].split(",")[0], response_format)
        reference = bible_copyright(request,current_bible['dam_id'],return_type=response_format)
        request.session['last_url'] = request.build_absolute_uri()
    else:
        return redirect('/eng', False)
    return render_to_response('users/template.html', {'current_url':request.session['last_url'],'languages_bible':languages, 'current_language':language_family_iso.lower(),'current_language_html':language_item[0]["language_family_iso_1"], 'bibles':bibles, 'current_bible':current_bible, 'books':books, 'current_book':current_book, 'current_chapter':chapter, 'references':reference,'is_admin':is_admin(request)['is_admin']}, context_instance=RequestContext(request))

#...
def search_dictionaries(key, value, list_of_dictionaries):
    return [element for element in list_of_dictionaries if element[key].lower() == value.lower()]

#...
@csrf_exempt
def upload_handler(request):
    if is_admin(request)['is_admin'] == False:
        return HttpResponse(json.dumps({'error':'Admin Permission Required'}), content_type="application/json",status=200)
    file_dictionary = {}
    files_array = []
    try:
        file = request.FILES["files[]"]
        filename = file.name
    except:
        file = None
        filename = None
        return HttpResponse(json.dumps(None), content_type="application/json",status=200)

    import sys
    print >>sys.stderr, 'HELLO'
    print >>sys.stderr, file
    print >>sys.stderr, filename
    print >>sys.stderr, file.size

    page_id = request.POST.get('page_id', None)
    gallery_id = request.POST.get('gallery_id', None)
    url_slug = ''
    if page_id:
        page = Page.objects.get(id=page_id)
        description = page.title
    elif gallery_id:
        gallery = Gallery.objects.get(id=gallery_id)
        description = gallery.name
        url_slug = '/en/gallery/' + gallery.slug
    else:
        description = None
    image = Image.create(filename)
    image.description = description if description else file.name
    image.image_file = file.name
    image.size = file.size
    try:
        photo = handle_image_picasa(file, image, description,url_slug)
        logger.debug("Image 1 uploaded successfully.")
        image_dictionary = {}
        image_dictionary["name"] = filename
        image_dictionary["size"] = image.size
        image_dictionary["url"] = image.picasa_photo_url
        image_dictionary["thumbnailUrl"] = image.picasa_thumb_url
        if page_id:
            image.page = page
        elif gallery_id:
            image.gallery = gallery
        image.save()
        image_dictionary["deleteUrl"] = str(request.build_absolute_uri()).replace('upload_handler/', '')  + 'image/delete/'+ str(image.id) +'/?json=true'
        image_dictionary["deleteType"] = "GET"
    except:
        logger.error('views/upload_handler')
        image_dictionary = {}
        image_dictionary["name"] = filename
        image_dictionary["size"] = image.size
        image_dictionary["error"] = 'Error Uploading Photo ' + filename
    files_array.append(image_dictionary)
    file_dictionary["files"] = files_array
    print >>sys.stderr, file_dictionary
    return HttpResponse(json.dumps(file_dictionary), content_type="application/json",status=200)

# ...
def image_upload(request):
    if is_admin(request)['is_admin']:
        page_id = request.GET.get('page_id', None)
        gallery_id = request.GET.get('gallery_id', None)
        if page_id:
            page = Page.objects.get(id=page_id)
            gallery = None
        elif gallery_id:
            gallery = Gallery.objects.get(id=gallery_id)
            page = None
        return render_to_response("pages/image_upload.html", {"page":page, "gallery":gallery }, context_instance=RequestContext(request))
    else:
        return redirect('/', False)



# Custom 404 and 500
def my_custom_404_view(request):
    return render_to_response('users/404.html',context_instance=RequestContext(request))

#...
def my_custom_500_view(request):
    return render_to_response('users/500.html',context_instance=RequestContext(request))

def humans(request):
    return render_to_response('txt/humans.txt',context_instance=RequestContext(request))

def robots(request):
    return render_to_response('txt/robots.txt',context_instance=RequestContext(request))
