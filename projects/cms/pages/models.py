import time

from google.appengine.api import memcache
from django import forms
from django.template.defaultfilters import slugify
from django.core.exceptions import ValidationError
from users.models import *


class Language(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, null=False, blank=False)
    code = models.CharField(max_length=7, null=False, blank=False, unique=True)
    is_enabled = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)
    # ...
    def __unicode__(self):
        return u'%s' % (self.name )

    # ...
    class Meta:
        unique_together = ("name", "code")


# Create your models here.
class Category(models.Model):
    ORDER = ((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'),(10, '10'), (11, '11'), (12, '12'), (13, '13'), (14, '14'), (15, '15'), (16, '16'), (17, '17'), (18, '18'), (19, '19'),(20, '20'), (21, '21'), (22, '22'), (23, '23'), (24, '24'), (25, '25'), (26, '26'), (27, '27'), (28, '28'), (29, '29'),(30, '30'), (31, '31'), (32, '32'), (33, '33'), (34, '34'), (35, '35'), (36, '36'), (37, '37'), (38, '38'), (39, '39'))
    MAX_COUNT = ((1, '1'), (2, '2'), (3, '3'), (4, '4'))
    id = models.AutoField(primary_key=True)
    language = models.ForeignKey(Language, null=True, blank=True)
    name = models.CharField(max_length=256, null=False, blank=False)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children')
    slug = models.SlugField(unique=True, blank=False, null=False)
    order = models.SmallIntegerField(null=True, blank=True,default=1, choices=ORDER)
    allow_replies = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)

    # ...
    def __unicode__(self):
        return u'%s' % (self.name )

    # ...
    def save(self, *args, **kwargs):
        memcache.delete('categories')

        import re

        name = re.sub(r'\W+', ' ', self.name)
        slug_1 = slugify(str(name))
        slug_2 = slugify(str(name) + ' ' + str(int(time.time())))

        if self.id is not None:
            category_exists_1 = Category.objects.filter(slug=slug_1, language=self.language).exclude(id=self.id).count()
            category_exists_2 = Category.objects.filter(slug=slug_2, language=self.language).exclude(id=self.id).count()
        else:
            category_exists_1 = Category.objects.filter(slug=slug_1, language=self.language).count()
            category_exists_2 = Category.objects.filter(slug=slug_2, language=self.language).count()

        if category_exists_1 == False:
            self.slug = slug_1
        elif category_exists_2 == False:
            self.slug = slug_2
        else:
            raise ValidationError("Another Category with same slug already exists. Please use different name.")

        super(Category, self).save(*args, **kwargs)

    # ...
    def clean(self):
        if self.parent is None and self.id is None and Category.objects.filter(name=self.name).exists():
            raise ValidationError("Another Category with name " + self.name + " and no parent already exists")


    # ...
    class Meta:
        unique_together = (("language", "parent", "name"))

# ...
class Spreadsheet(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)
    spreadsheet_file = models.FileField(upload_to='spreadsheets/')
    size = models.CharField(max_length=32)
    created_at = models.DateTimeField(auto_now=True)
    # ...
    def __unicode__(self):
        return u'%s' % (self.name )

# ...
class Feed(models.Model):
    id = models.AutoField(primary_key=True)
    source_type = models.CharField(max_length=64, null=False, blank=False, unique=False)
    feed_url = models.CharField(max_length=128, null=False, blank=False, unique=False)
    logo_url = models.CharField(max_length=128, null=False, blank=False, unique=False)
    language = models.ForeignKey(Language, null=True, blank=True)
    save_to_db = models.BooleanField(default=False)
    is_enabled = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)

    # ...
    def __unicode__(self):
        return u'%s' % (self.source_type )

    # ...
    class Meta:
        unique_together = ("source_type", "language")

# ...
class Page(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, null=False, blank=False)
    user = models.ForeignKey(User, null=False, blank=False)
    spreadsheet = models.ForeignKey(Spreadsheet, null=True, blank=True)
    title = models.CharField(max_length=256, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    headline = models.CharField(max_length=256, null=False, blank=False)
    slug = models.SlugField(unique=True, blank=False, null=False)
    twitter_hashtags = models.CharField(max_length=256, null=False, blank=False)
    feed_source = models.ForeignKey(Feed, null=True, blank=True)
    image_url = models.CharField(max_length=64, null=True, blank=True, unique=False)
    video_url = models.CharField(max_length=64, null=True, blank=True, unique=False)
    audio_url = models.CharField(max_length=64, null=True, blank=True, unique=False)
    link_url = models.CharField(max_length=64, null=True, blank=True, unique=False)
    priority = models.IntegerField(default=1, null=False, blank=False, unique=False)
    is_enabled = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)

    # ...
    def __unicode__(self):
        return u'%s' % (self.title )

    # ...
    def save(self, *args, **kwargs):
        memcache.delete('pages')
        import re

        title = re.sub(r'\W+', ' ', self.title)
        slug_1 = slugify(str(title))
        slug_2 = slugify(str(self.category.name) + ' ' + str(title))

        if self.id is not None:
            page_exists_1 = Page.objects.filter(slug=slug_1).exclude(id=self.id).count()
            page_exists_2 = Page.objects.filter(slug=slug_2).exclude(id=self.id).count()
        else:
            page_exists_1 = Page.objects.filter(slug=slug_1).count()
            page_exists_2 = Page.objects.filter(slug=slug_2).count()

        if page_exists_1 == False:
            self.slug = slug_1
        elif page_exists_2 == False:
            self.slug = slug_2
        else:
            raise ValidationError("Another page with same slug already exists. Please use different name.")

        # Headline
        self.headline = self.content[0:70] + '...'

        super(Page, self).save(*args, **kwargs)

    # ...
    class Meta:
        unique_together = ("category", "title")


# ...
class Gallery(models.Model):
    ORDER = ((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'),(10, '10'), (11, '11'), (12, '12'), (13, '13'), (14, '14'), (15, '15'), (16, '16'), (17, '17'), (18, '18'), (19, '19'),(20, '20'), (21, '21'), (22, '22'), (23, '23'), (24, '24'), (25, '25'), (26, '26'), (27, '27'), (28, '28'), (29, '29'),(30, '30'), (31, '31'), (32, '32'), (33, '33'), (34, '34'), (35, '35'), (36, '36'), (37, '37'), (38, '38'), (39, '39'))
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256, blank=True, null=True, unique=True)
    slug = models.SlugField(unique=True, blank=False, null=False)
    description = models.TextField(null=True, blank=True)
    is_enabled = models.BooleanField(default=True)
    is_default = models.BooleanField(default=False)
    order = models.SmallIntegerField(null=True, blank=True, choices=ORDER)
    created_at = models.DateTimeField(auto_now=True)

    # ...
    def __unicode__(self):
        return u'%s' % (self.name )

    # ...
    def save(self, *args, **kwargs):
        memcache.delete('galleries')
        import re
        name = re.sub(r'\W+', ' ', self.name)
        slug_1 = slugify(str(name))        

        if self.id is not None:
            gallery_exists_1 = Gallery.objects.filter(slug=slug_1).exclude(id=self.id).count()            
        else:
            gallery_exists_1 = Gallery.objects.filter(slug=slug_1).count()
        if gallery_exists_1 == False:
            self.slug = slug_1
        else:
            raise ValidationError("Another gallery with same slug already exists. Please use different name.")
        super(Gallery, self).save(*args, **kwargs)

# ...
class Image(models.Model):
    ORDER = ((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'),(10, '10'), (11, '11'), (12, '12'), (13, '13'), (14, '14'), (15, '15'), (16, '16'), (17, '17'), (18, '18'), (19, '19'),(20, '20'), (21, '21'), (22, '22'), (23, '23'), (24, '24'), (25, '25'), (26, '26'), (27, '27'), (28, '28'), (29, '29'),(30, '30'), (31, '31'), (32, '32'), (33, '33'), (34, '34'), (35, '35'), (36, '36'), (37, '37'), (38, '38'), (39, '39'))
    id = models.AutoField(primary_key=True)
    page = models.ForeignKey(Page, null=True, blank=True)
    gallery = models.ForeignKey(Gallery, null=True, blank=True)
    name = models.CharField(max_length=256, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField(unique=True, blank=False, null=False)
    image_file = models.FileField(upload_to='images/')
    size = models.CharField(max_length=32)
    picasa_album_id = models.CharField(max_length=256)
    picasa_photo_id = models.CharField(max_length=256)
    picasa_photo_url = models.URLField()
    picasa_medium_url = models.URLField()
    picasa_thumb_url = models.URLField()
    height = models.CharField(max_length=7)
    width = models.CharField(max_length=7)
    order = models.SmallIntegerField(null=True, blank=True,default=1, choices=ORDER)
    is_enabled = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)

    # ...
    @classmethod
    def create(cls, name):
        image = cls(name=name)
        return image

    # ...
    def __unicode__(self):
        return u'%s' % (self.name )

    # ...
    def save(self, *args, **kwargs):

        if self.name is None:
            if self.page is None:
                self.name = self.image_file
            else:
                self.name = self.page.title

        slug_1 = slugify(str(self.name))
        slug_2 = slugify(str(self.name) + str(int(time.time())))

        if self.id is not None:
            image_exists_1 = Image.objects.filter(slug=slug_1).exclude(id=self.id).count()
            image_exists_2 = Image.objects.filter(slug=slug_2).exclude(id=self.id).count()
        else:
            image_exists_1 = Image.objects.filter(slug=slug_1).count()
            image_exists_2 = Image.objects.filter(slug=slug_2).count()

        if image_exists_1 == False:
            self.slug = slug_1
        elif image_exists_2 == False:
            self.slug = slug_2

        self.order = int(self.order)

        super(Image, self).save(*args, **kwargs)


# ...
class Record(models.Model):
    id = models.AutoField(primary_key=True)
    key = models.CharField(max_length=64, null=False, blank=False, unique=False)
    value = models.TextField(null=False, blank=False)
    language = models.ForeignKey(Language, null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    # ...
    def __unicode__(self):
        return u'%s' % (self.key )

    # ...
    class Meta:
        unique_together = ("key", "language")

# ...
class Advertisement(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, null=False, blank=False, unique=True)
    advertisement_url = models.CharField(max_length=128, null=False, blank=False, unique=True)
    image_url = models.CharField(max_length=128, null=False, blank=False, unique=True)
    is_enabled = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)

    # ...
    def __unicode__(self):
        return u'%s' % (self.name )

# ...
class ContactForm(forms.Form):
    contact_email = forms.EmailField()
    contact_name = forms.CharField(max_length=100)
    contact_comment = forms.CharField(widget=forms.Textarea(attrs={'cols': 80, 'rows': 20}))


# Forms
class RecordForm(ModelForm):
    class Meta:
        model = Record
        fields = ['key', 'value','language']

# Forms
class LanguageForm(ModelForm):
    class Meta:
        model = Language
        fields = ['name', 'code']

# Forms
class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['language', 'name', 'parent', 'allow_replies', 'order']

# Forms
class PageForm(ModelForm):
    class Meta:
        model = Page
        fields = ['category', 'title', 'content','image_url','video_url','link_url','is_enabled']

# Forms
class FeedForm(ModelForm):
    class Meta:
        model = Feed
        fields = ['source_type', 'feed_url', 'logo_url', 'language', 'save_to_db', 'is_enabled']

# Forms
class SpreadsheetForm(ModelForm):
    class Meta:
        model = Spreadsheet
        fields = ['name', 'spreadsheet_file']

# Forms
class GalleryForm(ModelForm):
    class Meta:
        model = Gallery
        fields = ['name', 'description','is_default','is_enabled']


# Forms
class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = ['name', 'description', 'image_file']

# Forms
class AdvertisementForm(ModelForm):
    class Meta:
        model = Advertisement
        fields = ['name', 'advertisement_url', 'image_url', 'is_enabled']