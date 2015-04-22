from django.shortcuts import render
from django.views.generic.list import ListView

from models import Request


# Create your views here.
class RequestListView(ListView):
    model = Request