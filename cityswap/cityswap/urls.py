from django.conf.urls import include, url, patterns
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'cityswap.views.home_page', name='home'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^profile/', include('profiles.urls'), name='profile'),
    url(r'^requests/', include('requests.urls'), name='requests_page'),
    url(r'^accounts/profile/', 'profiles.views.profile', name='profile'),
    url(r'^requests/', include('requests.urls'), name='requests'),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
