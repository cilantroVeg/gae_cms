from django.db import models
from django.conf import settings
from pages.models import Page


# Create your models here.
class Photo(models.Model):
    id = models.AutoField(primary_key=True)
    page = models.ForeignKey(Page, null=False, blank=False)
    title = models.CharField(max_length=256, null=True, blank=True)
    url_small = models.URLField()
    url_medium = models.URLField()
    url_large = models.URLField()
    created_at = models.DateTimeField(auto_now=True)

    # ...
    def __unicode__(self):
        return u'%s' % (self.title)


class PhotoProvider(models.Model):
    id = models.AutoField(primary_key=True)
    name = title = models.CharField(max_length=64, null=False, blank=False)  # Flickr, Photobucket, Picassa
    key = models.CharField(max_length=64, null=False, blank=False)
    secret = models.CharField(max_length=64, null=False, blank=False)