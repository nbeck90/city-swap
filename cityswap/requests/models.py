from django.db import models
from profiles.models import Profile
from datetime import datetime


SEATTLE = 'Seattle'
PORTLAND = 'Portland'

LOCATION_CHOICES = (
    (SEATTLE, 'Seattle'),
    (PORTLAND, 'Portland')
)


class Request(models.Model):
    sender = models.ForeignKey(Profile, related_name='sent_from')
    courier = models.ForeignKey(Profile, related_name='requests', blank=True,
                              null=True)

    title = models.TextField(default="Type your title here")

    description = models.TextField(default="Type your description here")

    origin = models.CharField(max_length=25,
                              choices=LOCATION_CHOICES,
                              default='Seattle')

    destination = models.CharField(max_length=25,
                                   choices=LOCATION_CHOICES,
                                   default='Seattle')
    date_created = models.DateTimeField(default=datetime.now, blank=True)

    def __unicode__(self):
        return self.description
