from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from requests.models import Request
from profiles.models import Profile
from django.views.generic import UpdateView
from profiles.forms import UserProfileForm


class ProfileUpdateView(UpdateView):
    model = Profile
    template_name_suffix = '_edit'
    form_class = UserProfileForm
    context_object_name = 'profile'
    success_url = '/profile/'

    def get_queryset(self):
        qs = super(ProfileUpdateView, self).get_queryset()
        return qs.filter(user=self.request.user)

    def get_initial(self):
        initial = super(ProfileUpdateView, self).get_initial()
        initial['first_name'] = self.request.user.first_name
        initial['last_name'] = self.request.user.last_name
        initial['email'] = self.request.user.email
        return initial

    def form_valid(self, form):
        # import pdb; pdb.set_trace()
        user = form.instance.user
        user.first_name = form.cleaned_data.get('first_name')
        user.last_name = form.cleaned_data.get('last_name')
        user.email = form.cleaned_data.get('email')
        user.save()
        return super(ProfileUpdateView, self).form_valid(form)


@login_required
def profile(request):
    """
    View the user's own profile
    """
    profile = request.user.profile
    req = Request.objects.all()
    reqs = req.filter(courier=profile)
    return render(request, 'profiles/profile.html', {'object_list': reqs})
