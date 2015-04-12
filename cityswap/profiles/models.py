from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.db.models import permalink
from django.db.models.signals import post_save


class Profile(models.Model):
    """
    Profile model with friending, blocking, slug, and picture features
    """
    user = models.OneToOneField(User, related_name='profile')
    friends = models.ManyToManyField('Profile', symmetrical=True,
                                     related_name='friends', null=True,
                                     blank=True)
    blocking = models.ManyToManyField('Profile', symmetrical=False,
                                      related_name='blocked_by', null=True,
                                      blank=True)
    requested_friends = models.ManyToManyField('Profile',
                                               symmetrical=False,
                                               related_name='requesting_friend',
                                               null=True, blank=True)
    picture = models.ImageField(
        upload_to='photos/', null=True, blank=True, default='photos/frame.jpg')
    slug = models.CharField(max_length=32, unique=True, blank=True)

    def __str__(self):
        return self.user.username

    @permalink
    def get_absolute_url(self):
        return ('profile', None, {'slug': self.slug})

    def friending(self, other_profile):
        if other_profile in self.blocked_by.all():
            raise ValueError('You been BLOCKED!')
        return self.friends.add(other_profile)

    def unfriending(self, other_profile):
        return self.friends.remove(other_profile)

    def get_friends(self):
        return Profile.objects.filter(Q(friends=self) &
                                      ~Q(blocking=self) &
                                      ~Q(blocked_by=self))

    def block(self, other_profile):
        return self.blocking.add(other_profile)

    def unblock(self, other_profile):
        return self.blocking.remove(other_profile)


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)
