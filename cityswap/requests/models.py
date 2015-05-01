from django.db import models
from profiles.models import Profile
from datetime import datetime


SEATTLE = 'se'
PORTLAND = 'pt'

LOCATION_CHOICES = (
    (SEATTLE, 'Seattle'),
    (PORTLAND, 'Portland')
)


class Request(models.Model):
    sender = models.ForeignKey(Profile, related_name='sent_from')
    courier = models.ManyToManyField(Profile, related_name='requests', blank=True,
                              null=True)

    description = models.TextField(default="Type your info here")

    origin = models.CharField(max_length=2,
                              choices=LOCATION_CHOICES,
                              default='se')

    destination = models.CharField(max_length=2,
                                   choices=LOCATION_CHOICES,
                                   default='se')
    date_created = models.DateTimeField(default=datetime.now, blank=True)

    def __unicode__(self):
        return self.description
