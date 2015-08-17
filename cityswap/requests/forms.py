from django import forms
from requests.models import Request


class UserProfileForm(forms.ModelForm):

    SEATTLE = 'Seattle'
    PORTLAND = 'Portland'

    LOCATION_CHOICES = (
        (SEATTLE, 'Seattle'),
        (PORTLAND, 'Portland')
    )

    title = forms.TextField(default="Type your title here")

    description = forms.TextField(default="Type your description here")

    origin = forms.CharField(max_length=25,
                             choices=LOCATION_CHOICES,
                             default='Seattle')

    destination = forms.CharField(max_length=25,
                                  choices=LOCATION_CHOICES,
                                  default='Seattle')

    class Meta:
        model = Request
        fields = [
            'title',
            'description',
            'origin',
            'destination',
            'sender',
            'courier',
            'date_created',
        ]
