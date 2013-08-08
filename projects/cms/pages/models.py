from django.db import models
from django.conf import settings
from users.models import *
from django.forms import ModelForm

from django.template.defaultfilters import slugify
from datetime import datetime

class Language(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, null=False, blank=False)
    code = models.CharField(max_length=7, null=False, blank=False, unique=True)
    created_at = models.DateTimeField(auto_now=True)
    # ...
    def __unicode__(self):
        return u'%s' % (self.name )

    # ...
    class Meta:
        unique_together = ("name", "code")


# Create your models here.
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    language = models.ForeignKey(Language, null=False, blank=False)
    name = models.CharField(max_length=256, null=False, blank=False)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children')
    slug = models.SlugField(unique=True,blank=False,null=False)
    allow_replies = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)

    # ...
    def __unicode__(self):
        return u'%s' % (self.name )

    # ...
    def save(self, *args, **kwargs):
        slug_1 = slugify(str(self.name))
        slug_2 = slugify(str(self.parent.name) + ' ' + str(self.name))

        exists_1 = Category.objects.filter(slug=slug_1).exclude(id=self.id).count()
        exists_2 = Category.objects.filter(slug=slug_2).exclude(id=self.id).count()

        if exists_1 == False:
            self.slug = slug_1
        elif exists_2 == False:
            self.slug = slug_2

        super(Category, self).save(*args, **kwargs)

    # ...
    class Meta:
        unique_together = ("parent", "name")

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
    slug = models.SlugField(unique=True,blank=False,null=False)
    content = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now=True)

    # ...
    def __unicode__(self):
        return u'%s' % (self.title )

    # ...
    def save(self, *args, **kwargs):
        slug_1 = slugify(str(self.name))
        slug_2 = slugify(str(self.category.name) + ' ' + str(self.name))

        exists_1 = Page.objects.filter(slug=slug_1).exclude(id=self.id).count()
        exists_2 = Page.objects.filter(slug=slug_2).exclude(id=self.id).count()

        if exists_1 == False:
            self.slug = slug_1
        elif exists_2 == False:
            self.slug = slug_2

        super(Category, self).save(*args, **kwargs)

        self.slug = slugify(str(self.category.name.encode('utf8')) + str(' ') + str(self.title.encode('utf8')))
        super(Page, self).save(*args, **kwargs)

    # ...
    class Meta:
        unique_together = ("category", "title")

# ...
class Record(models.Model):
    id = models.AutoField(primary_key=True)
    key = models.CharField(max_length=64, null=False, blank=False, unique=True)
    value = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now=True)
    # ...
    def __unicode__(self):
        return u'%s' % (self.key )


# ...
class Image(models.Model):
    id = models.AutoField(primary_key=True)
    page = models.ForeignKey(Page, null=True, blank=True)
    name = models.CharField(max_length=256, blank=False, null=False)
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
            self.name = self.page.title

        slug_1 = slugify(str(self.name))
        slug_2 = slugify(str(self.name) + datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))

        exists_1 = Image.objects.filter(slug=slug_1).exclude(id=self.id).count()
        exists_2 = Image.objects.filter(slug=slug_2).exclude(id=self.id).count()

        if exists_1 == False:
            self.slug = slug_1
        elif exists_2 == False:
            self.slug = slug_2

        super(Category, self).save(*args, **kwargs)

        self.slug = slugify(str(self.category.name.encode('utf8')) + str(' ') + str(self.title.encode('utf8')))
        super(Page, self).save(*args, **kwargs)


# ...
class Record(models.Model):
    id = models.AutoField(primary_key=True)
    key = models.CharField(max_length=64, null=False, blank=False, unique=True)
    value = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now=True)
    # ...
    def __unicode__(self):
        return u'%s' % (self.key )

# Forms
class RecordForm(ModelForm):
    class Meta:
        model = Record
        fields = ['key', 'value']

# Forms
class LanguageForm(ModelForm):
    class Meta:
        model = Language
        fields = ['name', 'code']

# Forms
class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['language', 'name', 'parent', 'allow_replies']

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