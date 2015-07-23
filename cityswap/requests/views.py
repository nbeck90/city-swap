from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic import CreateView

from models import Request
from profiles.models import Profile


# Create your views here.
class RequestListView(ListView):
    model = Request


def request_list(request):
    reqs = Request.objects.orderby('date_created')
    return render(request, 'requestspage.html', {'object_list': reqs})


def accept_request(request, pk):
    # import pdb; pdb.set_trace()
    req = Request.objects.get(pk=pk)
    profile = Profile.objects.get(user=request.user)
    req.courier = profile
    req.save()
    return redirect('/requests')


def detail_request(request, pk):
    req = Request.objects.filter(pk=pk)
    return render(request, 'requests/requestdetail.html', {'object_list': req})


class NewRequest(CreateView):
    model = Request
    context_object_name = 'request'
    success_url = '/profile'
    fields = [
        'title',
        'description',
        'origin',
        'destination',
        'sender'
    ]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(NewRequest, self).form_valid(form)

    def get_form(self, form_class):
        form = super(NewRequest, self).get_form(form_class)
        return form
