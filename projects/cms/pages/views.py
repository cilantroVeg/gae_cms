# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.conf import settings
from django.utils.html import *
import gdata.photos.service
import gdata.media
import gdata.geo
from django.forms.formsets import formset_factory
from django.forms.models import modelformset_factory

from pages.models import *

# ...
def category_form(request, id=None):
    if is_admin(request):
        instance = get_object_or_404(Category, id=id) if id is not None else None
        form = CategoryForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/categories/')
        return render_to_response("pages/category_form.html",
                                  {"form": form, "id": id},
                                  context_instance=RequestContext(request))
    else:
        return redirect('/', False)


# ...
def category_formset(request):
    if is_admin(request):
        CategoryFormSet = modelformset_factory(Category, exclude="slug", extra=0)

        if request.POST:
            formset = CategoryFormSet(request.POST)
            if formset.is_valid():
                formset.save()
                return redirect('/categories/')
        else:
            formset = CategoryFormSet(initial=Category.objects.values())
        return render_to_response("pages/category_formset.html",
                                  {"formset": formset},
                                  context_instance=RequestContext(request))
    else:
        return redirect('/', False)


# ...
def category_list(request):
    if is_admin(request):
        return render_to_response("pages/category_list.html",
                                  {"category_list": Category.objects.all()},
                                  context_instance=RequestContext(request))
    else:
        return redirect('/', False)

# ...
def category_delete(request, id=None):
    if is_admin(request):
        instance = get_object_or_404(Category, id=id) if id is not None else None
        instance.delete()
        return redirect('/categories/')
    else:
        return redirect('/', False)

# ...
def language_form(request, id=None):
    if is_admin(request):
        instance = get_object_or_404(Language, id=id) if id is not None else None
        form = LanguageForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/languages/')
        return render_to_response("pages/language_form.html",
                                  {"form": form, "id": id},
                                  context_instance=RequestContext(request))
    else:
        return redirect('/', False)

# ...
def language_list(request):
    if is_admin(request):
        return render_to_response("pages/language_list.html",
                                  {"language_list": Language.objects.all()},
                                  context_instance=RequestContext(request))
    else:
        return redirect('/', False)

# ...
def language_delete(request, id=None):
    if is_admin(request):
        instance = get_object_or_404(Language, id=id) if id is not None else None
        instance.delete()
        return redirect('/languages/')
    else:
        return redirect('/', False)

# ...
def page_form(request, id=None):
    if is_admin(request):
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
        return render_to_response("pages/page_form.html", {"page_form": page_form, "image_formset": ImageFormSet, "id": id, "user": request.user.id,
                                                           'image_array': image_array},
                                  context_instance=RequestContext(request))
    else:
        return redirect('/', False)

# ...
def page_list(request):
    if is_admin(request):
        return render_to_response("pages/page_list.html",
                                  {"page_list": Page.objects.all()},
                                  context_instance=RequestContext(request))
    else:
        return redirect('/', False)

# ...
def page_delete(request, id=None):
    if is_admin(request):
        instance = get_object_or_404(Page, id=id) if id is not None else None
        instance.delete()
        return redirect('/pages/')
    else:
        return redirect('/', False)

# ...
def record_form(request, id=None):
    if is_admin(request):
        instance = get_object_or_404(Record, id=id) if id is not None else None
        form = RecordForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/records/')
        return render_to_response("pages/record_form.html",
                                  {"form": form, "id": id},
                                  context_instance=RequestContext(request))
    else:
        return redirect('/', False)

# ...
def record_list(request):
    if is_admin(request):
        return render_to_response("pages/record_list.html",
                                  {"record_list": Record.objects.all()},
                                  context_instance=RequestContext(request))
    else:
        return redirect('/', False)

# ...
def record_delete(request, id=None):
    if is_admin(request):
        instance = get_object_or_404(Record, id=id) if id is not None else None
        instance.delete()
        return redirect('/records/')
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
    if is_admin(request):
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
        return render_to_response("pages/spreadsheet_form.html",
                                  {"form": form, "id": id},
                                  context_instance=RequestContext(request))
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
                # Language
                language, language_created = Language.objects.get_or_create(code=language_code,
                                                                            defaults={'name': language_code})
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
    if is_admin(request):
        return render_to_response("pages/spreadsheet_list.html", {"spreadsheet_list": Spreadsheet.objects.all(),
        },
                                  context_instance=RequestContext(request))
    else:
        return redirect('/', False)

# ...
def spreadsheet_delete(request, id=None):
    if is_admin(request):
        instance = get_object_or_404(Spreadsheet, id=id) if id is not None else None
        instance.delete()
        return redirect('/spreadsheets/')
    else:
        return redirect('/', False)


# # ...
# def handle_flickr_image(file, user, image):
#     # Check for Token
#     api_token = Record.objects.get(key='FLICKR_TOKEN').value
#     flickr = flickrapi.FlickrAPI(settings.FLICKR_API_KEY, settings.FLICKR_API_SECRET, token=api_token)
#     keywords = {'title': image.name, 'description': 'MAF', 'tags': 'MAF', 'is_public':1, 'format':'xmlnode'}
#     response = flickr.upload(filename=file.read(), callback=None, **keywords)
#     return False


# # ...
# def flickr_callback(request):
#     debug('FROB', request.GET['frob'])
#     flickr = flickrapi.FlickrAPI(settings.FLICKR_API_KEY, settings.FLICKR_API_SECRET, store_token=False)
#     token = flickr.get_token(request.GET['frob'])
#     if token:
#         Record(key='FLICKR_TOKEN', value=token).save()
#     debug('FLICKR_TOKEN',token)
#     return redirect('/', False)




# def require_flickr_auth(view):
#     '''View decorator, redirects users to Flickr when no valid
#     authentication token is available.
#     '''
# 
#     def protected_view(request, *args, **kwargs):
#         try:
#             token = Record.objects.get(key='FLICKR_TOKEN').value
#         except:
#             token = None
# 
#         f = flickrapi.FlickrAPI(settings.FLICKR_API_KEY,
#                settings.FLICKR_API_SECRET, token=token,
#                store_token=False)
# 
#         if token:
#             # We have a token, but it might not be valid
#             try:
#                 f.auth_checkToken()
#             except flickrapi.FlickrError:
#                 token = None
# 
#         if not token:
#             url = f.web_login_url(perms='write')
#             return HttpResponseRedirect(url)
# 
#         # If the token is valid, we can call the decorated view.
# 
#         return view(request, *args, **kwargs)
# 
#     return protected_view
# 
# 
# 

def image_form(request, id=None):
    if is_admin(request):
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
    if is_admin(request):
        return render_to_response("pages/image_list.html", {"image_list": Image.objects.all(),
        },
                                  context_instance=RequestContext(request))
    else:
        return redirect('/', False)

# ...
def image_delete(request, id=None):
    if is_admin(request):
        instance = get_object_or_404(Image, id=id) if id is not None else None
        delete_picasa_photo(instance)
        instance.delete()
        return redirect('/images/')
    else:
        return redirect('/', False)


# ...
def page_view(request, language, slug):
    page = get_object_or_404(Page, slug=slug)
    return render_to_response("pages/page_view.html", {"page": page,
    },
                              context_instance=RequestContext(request))

# ...
def sitemap(request):
    return render_to_response("pages/sitemap.html",
                              context_instance=RequestContext(request))


# ...
def category_view(request, language, slug):
    language = get_object_or_404(Language, code=language)
    category = get_object_or_404(Category, slug=slug, language_id=language.id)
    pages = Page.objects.filter(category=category)
    return render_to_response("pages/category_view.html", {"category": category, "pages": pages,
    },
                              context_instance=RequestContext(request))

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


def is_admin(request):
    try:
        if request.user.email in settings.ADMIN_USERS:
            return True
        else:
            return False
    except:
        return False