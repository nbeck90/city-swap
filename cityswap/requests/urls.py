from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.RequestListView.as_view(
        template_name="requests/requestspage.html",
        ),
        name='requests_page'),
    url(r'^accept/(?P<pk>\d+)$', 'requests.views.accept_request', name='accept_request'),
    url(r'^detail/(?P<pk>\d+)$', 'requests.views.detail_request', name='detail_request'),
]
