# views.py

import gdata.photos.service
import gdata.media
import gdata.geo

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

# ...
def delete_cache(request):
    memcache.delete('category_array')
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
def page_form(request, id=None):
    if is_admin(request)['is_admin']:
        instance = get_object_or_404(Page, id=id) if id is not None else None
        if instance:
            image_array = Image.objects.filter(page=instance)
        else:
            image_array = None
        page_form = PageForm(request.POST or None, instance=instance)
        ImageFormSet = formset_factory(ImageForm, extra=7)
        if page_form.is_valid():
            page = page_form.save(commit=False)
            page.user = request.user
            page.save()
            formset = ImageFormSet(request.POST or None, request.FILES or None)
            for form in formset.forms:
                try:
                    image = form.save(commit=False)
                    image.page = page
                    image.name = form.cleaned_data['name']
                    image.image_file = form.cleaned_data['image_file'].name
                    image.size = form.cleaned_data['image_file'].size
                    image.save()
                    handle_image_picasa(form.cleaned_data['image_file'], image)
                except:
                    continue

            return redirect('/pages/')
        return render_to_response("pages/page_form.html", {"page_form": page_form, "image_formset": ImageFormSet, "id": id, "user": request.user.id, 'image_array': image_array}, context_instance=RequestContext(request))
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
        return False

# ...
def handle_image_picasa(file, image):
    gd_client = connect_picasa()

    try:
        albums = gd_client.GetUserFeed()
        album = albums.entry[0]
    except:
        album = gd_client.InsertAlbum(title=Record.objects.get(key='WEBSITE_NAME').value, summary=Record.objects.get(key='WEBSITE_DESCRIPTION').value)

    album_url = '/data/feed/api/user/%s/albumid/%s' % ('default', album.gphoto_id.text)
    photo = gd_client.InsertPhotoSimple(album_url, file.name, Record.objects.get(key='WEBSITE_DESCRIPTION').value, file, content_type='image/jpeg')

    image.picasa_album_id = album.gphoto_id.text
    image.picasa_photo_id = photo.gphoto_id.text
    image.picasa_thumb_url = photo.media.thumbnail[0].url
    image.picasa_photo_url = photo.content.src
    image.save()
    # pic = StringIO.StringIO(pic)
    debug('PHOTO', photo)
    return photo

# ...
def image_list(request):
    if is_admin(request)['is_admin']:
        return render_to_response("pages/image_list.html", {"image_list": Image.objects.all(),
                                                            },
                                  context_instance=RequestContext(request))
    else:
        return redirect('/', False)

# ...
def image_delete(request, id=None):
    if is_admin(request)['is_admin']:
        instance = get_object_or_404(Image, id=id) if id is not None else None
        delete_picasa_photo(instance)
        instance.delete()
        return redirect('/images/')
    else:
        return redirect('/', False)


# ...
def page_view(request, language, slug):
    page = get_object_or_404(Page, slug=slug)
    image_array = Image.objects.filter(page=page)
    return render_to_response("pages/page_view.html", {"page": page,"image_array":image_array},context_instance=RequestContext(request))

# ...
def page_feed_view(request, language, slug):
    feed_pages = query_api(language, 'feed_pages')
    page = None
    for key in feed_pages['pages']:
        if feed_pages['pages'][key]:
            for p in feed_pages['pages'][key]:
                if p['slug'] == slug:
                    page = p
    if page:
        return render_to_response("pages/page_view.html", {"page": page},context_instance=RequestContext(request))
    else:
        return redirect('/', False)

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
        return render_to_response("pages/sitemap.html", {},context_instance=RequestContext(request))

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
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
        error_message = message_contains_url(request.POST['contact_comment'])
        if error_message:
            try:
                data = {'contact_email': request.POST['contact_email'], 'contact_name': request.POST['contact_name'], 'contact_message': request.POST['contact_message']}
            except:
                data = {}
        else:
            if form.is_valid():
                contact_name = form.cleaned_data['contact_name']
                contact_email = form.cleaned_data['contact_email']
                contact_comment = form.cleaned_data['contact_comment']
                subject = 'Contact Form ' + Record.objects.filter(key='WEBSITE_NAME')[:1][0].value + ': \'' + contact_name + '\': \'' + contact_email + '\''
                recipients = settings.ADMIN_USERS_EMAILS
                sender = 'Contact Form ' + Record.objects.filter(key='WEBSITE_NAME')[:1][0].value + " <" + settings.SERVER_EMAIL + ">"
                from google.appengine.api import mail
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
                return redirect('/'+language.code, False)
        return redirect('/en', False)

def front_page_language(request,language):
    if settings.APP_NAME == 'bible-love':
        return redirect('/eng', False)
    image_array = Image.objects.all()[:7]
    language_code = 'en' if (language is None) else language
    try:
        feed_pages = query_api(language_code, 'feed_pages')
        feed_pages = feed_pages['pages'] if feed_pages else None
    except:
        feed_pages = None
    return render_to_response('users/template.html', {'feed_pages':feed_pages, 'image_array': image_array,'is_admin':is_admin(request)['is_admin']}, context_instance=RequestContext(request))

def front_page_language_family_iso(request,language,bible=None,book=None,chapter=None):
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

def search_dictionaries(key, value, list_of_dictionaries):
    return [element for element in list_of_dictionaries if element[key].lower() == value.lower()]

# Custom 404 and 500
def my_custom_404_view(request):
    return render_to_response('users/404.html',context_instance=RequestContext(request))

def my_custom_500_view(request):
    return render_to_response('users/500.html',context_instance=RequestContext(request))