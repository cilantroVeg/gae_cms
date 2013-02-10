from django.db import models

# Create your models here.

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200,unique=False)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children')
    slug = models.SlugField(unique=True)
    allow_replies = models.Boolean
    created_at = models.DateTimeField(auto_now=True)
    # ...
    def __unicode__(self):
        return u'%s' % (self.token )
        # ...
    class Meta:
        unique_together = ("title", "token")

class Page(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, blank=False, null=False)
    title = models.TextField(max_length=256,unique=False)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    # ...
    def __unicode__(self):
        return u'%s' % (self.token )
        # ...
    class Meta:
        unique_together = ("title", "category")

class Photo(models.Model):
    id = models.AutoField(primary_key=True)
    page = models.ForeignKey(Page, blank=False, null=False)
    title = models.TextField()
    url = models.URLField(max_length=200,blank=False,null=False)
    created_at = models.DateTimeField(auto_now=True)
    # ...
    def __unicode__(self):
        return u'%s' % (self.token )
        # ...
    class Meta:
        unique_together = ("title", "category")
