from django.db import models
from django.conf import settings
from pages.models import Page


# Create your models here.
class Photo(models.Model):
    id = models.AutoField(primary_key=True)
    page = models.ForeignKey(Page, null=True)
    title = models.CharField(max_length=256, null=True, blank=True)
    url_small = models.URLField()
    url_medium = models.URLField()
    url_large = models.URLField()
    created_at = models.DateTimeField(auto_now=True)

    # ...
    def __unicode__(self):
        return u'%s' % (self.title)