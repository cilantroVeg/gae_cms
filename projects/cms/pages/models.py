from django.db import models
from users.models import *
from django.template.defaultfilters import slugify


# Create your models here.
class Category(models.Model):
    id = models.AutoField(primary_key=True)
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