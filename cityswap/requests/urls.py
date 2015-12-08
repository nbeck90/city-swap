from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from requests.views import NewRequest
import views

urlpatterns = [
    url(r'^$', views.RequestListView.as_view(
        template_name="requests/requestspage.html",
    ),
        name='requests_page'),
    url(r'^accept/(?P<pk>\d+)$', 'requests.views.accept_request', name='accept_request'),
    url(r'^remove/(?P<pk>\d+)$', 'requests.views.remove_self', name='remove_self'),
    url(r'^detail/(?P<pk>\d+)$', 'requests.views.detail_request', name='detail_request'),
    url(r'^newrequest',
        login_required(NewRequest.as_view()),
        name='new_request',
        ),
]
