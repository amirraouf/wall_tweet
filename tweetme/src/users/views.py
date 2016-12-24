from django.views.generic import DetailView, FormView
from django.contrib.auth.admin import UserCreationForm

from .models import User


class ProfileView(DetailView):
    template_name = 'users/detail.html'
    slug_url_kwarg = 'username'
    model = User


class Register(FormView):
    form_class = UserCreationForm
