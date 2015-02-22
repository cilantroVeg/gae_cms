from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.forms import ModelForm
from social.backends import google
from social.backends import facebook
from social.backends import twitter


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    profile_picture = models.URLField()

    def __str__(self):
        return "%s's profile" % self.user


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = UserProfile.objects.get_or_create(user=instance)


post_save.connect(create_user_profile, sender=User)


# Forms
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['email']


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['user', 'profile_picture']


def social_extra_values(sender, user, response, details, **kwargs):
    if "id" in response:
        from urllib2 import urlopen, HTTPError
        from django.template.defaultfilters import slugify
        from django.core.files.base import ContentFile

        try:
            url = None
            if sender == facebook:
                url = "http://graph.facebook.com/%s/picture?type=large" \
                            % response["id"]
            elif sender == google.GoogleOAuth2Backend and "picture" in response:
                url = response["picture"]

            elif sender == twitter:
                url = response["profile_image_url"]

            if url:
                avatar = urlopen(url)
                profile = UserProfile(user=user)

                profile.profile_picture.save(slugify(user.username + " social") + '.jpg',
                        ContentFile(avatar.read()))

                profile.save()

        except HTTPError:
            pass



    return False