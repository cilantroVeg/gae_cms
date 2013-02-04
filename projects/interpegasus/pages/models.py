from django.db import models

# Create your models here.

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200,unique=False)
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
    title = models.TextField()
    content = models.CharField(max_length=200,unique=False)
    created_at = models.DateTimeField(auto_now=True)
    # ...
    def __unicode__(self):
        return u'%s' % (self.token )
        # ...
    class Meta:
        unique_together = ("title", "category")
