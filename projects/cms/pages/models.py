from django.db import models
from django.conf import settings
from users.models import *
from photos.models import *
from django.forms import ModelForm

from django.template.defaultfilters import slugify

class Language(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, null=False, blank=False)
    code = models.CharField(max_length=7, null=False, blank=False)
    created_at = models.DateTimeField(auto_now=True)
    # ...
    def __unicode__(self):
        return u'%s' % (self.name )

# Create your models here.
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    language = models.ForeignKey(Language, null=False, blank=False)
    name = models.CharField(max_length=256, null=False, blank=False)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children')
    slug = models.SlugField()
    allow_replies = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)

    # ...
    def __unicode__(self):
        return u'%s' % (self.name )

    # ...
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(str(self.parent) +str(' ') + str(self.name))
        super(Category, self).save(*args, **kwargs)

    # ...
    class Meta:
        unique_together = ("parent", "name")


class Page(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, null=False, blank=False)
    user = models.ForeignKey(User, null=False, blank=False)
    title = models.CharField(max_length=256, null=False, blank=False)
    slug = models.SlugField()
    content = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now=True)

    # ...
    def __unicode__(self):
        return u'%s' % (self.title )

    # ...
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(str(self.category) +str(' ') + str(self.title))
        super(Page, self).save(*args, **kwargs)

    # ...
    class Meta:
        unique_together = ("category", "title")


# Forms
class LanguageForm(ModelForm):
    class Meta:
        model = Language
        fields = ['name', 'code']

# Forms
class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['language', 'name','parent','allow_replies']

# Forms
class PageForm(ModelForm):
    class Meta:
        model = Page
        fields = ['category','user', 'title','content']
