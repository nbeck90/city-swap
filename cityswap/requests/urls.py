from django.conf.urls import include, url
from django.contrib import admin
import views

urlpatterns = [
    url(r'^$', views.RequestListView.as_view(
        template_name="requests/requestspage.html",
        ),
        name='requests_page'),
    url(r'^accept/(?P<pk>\d+)$', views.accept_request, name='accept_request')
]
