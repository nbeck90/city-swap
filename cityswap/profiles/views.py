from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def profile(request):
    """
    View the user's own profile
    """
    profile = request.user.profile
    context = {
        'profile': profile,
    }
    return render(request, 'profiles/profile.html', context)
