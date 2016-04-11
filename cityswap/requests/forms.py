from django import forms
from django.contrib.auth.models import User
from requests.models import Request
from django.db import models


class UserProfileForm(forms.ModelForm):
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
