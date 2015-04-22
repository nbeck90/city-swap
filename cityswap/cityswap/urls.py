from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'cityswap.views.home_page', name='home'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
