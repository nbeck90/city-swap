from django import forms
from profiles.models import Profile


class UserProfileForm(forms.ModelForm):
    first_name = forms.CharField(label='First Name', max_length=30)
    last_name = forms.CharField(label='Last Name', max_length=30)
    email = forms.EmailField(label='Email', max_length=30)

    class Meta:
        model = Profile
        fields = [
            'first_name',
            'last_name',
            'email',
            'picture',
        ]
