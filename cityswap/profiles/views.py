from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from requests.models import Request


@login_required
def profile(request):
    """
    View the user's own profile
    """
    profile = request.user.profile
    req = Request.objects.all()
    reqs = req.filter(courier=profile)
    return render(request, 'profiles/profile.html', {'object_list': reqs})
