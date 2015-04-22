from django.db import models
from profiles.models import Profile


SEATTLE = 'se'
PORTLAND = 'pt'

LOCATION_CHOICES = (
    (SEATTLE, 'Seattle'),
    (PORTLAND, 'Portland')
)


class Request(models.Model):
    sender = models.ForeignKey(Profile, related_name='sent_from')
    currier = models.ManyToManyField(Profile, related_name='requests')

    description = models.TextField(default="Type your info here")

    origin = models.CharField(max_length=2,
                              choices=LOCATION_CHOICES,
                              default='se')

    destination = models.CharField(max_length=2,
                                   choices=LOCATION_CHOICES,
                                   default='se')
