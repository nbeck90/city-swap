from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.db.models import permalink


class Profile(models.Model):
    """
    Profile model with friending, blocking, slug, and picture features
    """
    user = models.OneToOneField(User, related_name='profile')

    picture = models.ImageField(
        upload_to='photos', null=True, blank=True, default=None)

    slug = models.CharField(max_length=32, unique=True, blank=True)

    def __str__(self):
        return self.user.username

    def save(self):
        self.slug = slugify(self.user.username)
        super(Profile, self).save()

    @permalink
    def get_absolute_url(self):
        return ('profile', None, {'slug': self.slug})
