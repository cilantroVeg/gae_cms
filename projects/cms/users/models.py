from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    profile_picture = models.URLField()

    def __str__(self):
        return "%s's profile" % self.user


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = UserProfile.objects.get_or_create(user=instance)


post_save.connect(create_user_profile, sender=User)


class ContactForm(forms.Form):
    your_email = forms.EmailField()
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea(attrs={'cols': 80, 'rows': 20}))


# Forms
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['email']


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['user', 'profile_picture']