from django.conf.urls import include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'cityswap.views.home_page', name='home'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^profile/', include('profiles.urls'), name='profile'),
    url(r'^accounts/profile/', 'profiles.views.profile', name='profile'),
    url(r'^requests/', include('requests.urls'), name='requests'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]

urlpatterns += staticfiles_urlpatterns()
