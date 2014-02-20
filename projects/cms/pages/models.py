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
    ORDER = ((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'))
    MAX_COUNT = ((1, '1'), (2, '2'), (3, '3'), (4, '4'))
    id = models.AutoField(primary_key=True)
    language = models.ForeignKey(Language, null=True, blank=True)
    name = models.CharField(max_length=256, null=False, blank=False)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children')
    slug = models.SlugField(unique=True, blank=False, null=False)
    order = models.SmallIntegerField(null=True, blank=True, choices=ORDER)
    allow_replies = models.BooleanField(default=False)
    frontpage_page_limit = models.SmallIntegerField(null=True, blank=True, default=1, choices=MAX_COUNT)
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
class Page(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, null=False, blank=False)
    user = models.ForeignKey(User, null=False, blank=False)
    spreadsheet = models.ForeignKey(Spreadsheet, null=True, blank=True)
    title = models.CharField(max_length=256, null=False, blank=False)
    headline = models.CharField(max_length=256, null=False, blank=False)
    slug = models.SlugField(unique=True, blank=False, null=False)
    content = models.TextField(null=False, blank=False)
    twitter_hashtags = models.CharField(max_length=256, null=False, blank=False)
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
class Image(models.Model):
    id = models.AutoField(primary_key=True)
    page = models.ForeignKey(Page, null=True, blank=True)
    name = models.CharField(max_length=256, blank=True, null=True)
    slug = models.SlugField(unique=True, blank=False, null=False)
    image_file = models.FileField(upload_to='images/')
    size = models.CharField(max_length=32)
    picasa_album_id = models.CharField(max_length=256)
    picasa_photo_id = models.CharField(max_length=256)
    picasa_photo_url = models.URLField()
    picasa_thumb_url = models.URLField()
    height = models.CharField(max_length=7)
    width = models.CharField(max_length=7)
    created_at = models.DateTimeField(auto_now=True)

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

        super(Image, self).save(*args, **kwargs)


# ...
class Ingredients(models.Model):
    id = models.AutoField(primary_key=True)
    page = models.ForeignKey(Page, null=False, blank=False)
    list = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now=True)
    # ...
    def __unicode__(self):
        return u'%s' % (self.key )


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
        fields = ['category', 'title', 'content']

# Forms
class SpreadsheetForm(ModelForm):
    class Meta:
        model = Spreadsheet
        fields = ['name', 'spreadsheet_file']

# Forms
class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = ['name', 'image_file']
