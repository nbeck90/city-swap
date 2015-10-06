from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from profiles.views import ProfileUpdateView

urlpatterns = patterns(
    'profiles.views',
    url(r'^$', 'profile', name='profile'),
    url(r'^/edit/(?P<pk>\d+)$',
        login_required(ProfileUpdateView.as_view()),
        name='profile_edit'),
)

urlpatterns += staticfiles_urlpatterns()
