from django.http import HttpResponseRedirect
from django.views.generic import DetailView, CreateView

from .forms import UserCreationForm
from .models import User
from .utils import send_activation_code_email
from wall.settings import LOGIN_REDIRECT_URL


class ProfileView(DetailView):
    template_name = 'users/detail.html'
    slug_url_kwarg = 'username'
    model = User


class RegisterFormView(CreateView):
    form_class = UserCreationForm
    template_name = 'users/register.html'
    model = User

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(LOGIN_REDIRECT_URL)
        super(RegisterFormView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        send_activation_code_email(form)
        super(RegisterFormView, self).form_valid(form)
