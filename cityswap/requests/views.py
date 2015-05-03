from django.shortcuts import render, redirect
from django.views.generic.list import ListView

from models import Request
from profiles.models import Profile


# Create your views here.
class RequestListView(ListView):
    model = Request


def request_list(request):
    reqs = Request.objects.orderby('date_created')
    return render(request, 'requestspage.html', {'object_list': reqs})


def accept_request(request, pk):
    #import pdb; pdb.set_trace()
    req = Request.objects.get(pk=pk)
    profile = Profile.objects.get(user=request.user)
    req.courier.add(profile)
    req.save()
    return redirect('/requests')

# def my_requests(request, pk):
#     reqs = Request.courier.get(pk=pk)

