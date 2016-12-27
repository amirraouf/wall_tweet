from django.utils import timezone
from django.http import (
    HttpResponseRedirect,
    HttpResponsePermanentRedirect,
    HttpResponseGone,
    )

from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, RedirectView
import logging

from .forms import UserCreationForm
from .models import User
from .utils import send_activation_code_email
from wall.settings import LOGIN_REDIRECT_URL


class ProfileView(DetailView):
    template_name = 'users/detail.html'
    slug_url_kwarg = 'username'
    model = User

    # def get


class RegisterFormView(CreateView):
    form_class = UserCreationForm
    template_name = 'users/register.html'
    model = User

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(LOGIN_REDIRECT_URL)
        return super(RegisterFormView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        super(RegisterFormView, self).form_valid(form)
        send_activation_code_email(form, form.instance.activation_key)
        return HttpResponseRedirect(reverse_lazy("users:login"))


class UserActivationView(RedirectView):
    model = User
    template_name = 'users/activation_user.html'

    def get(self, request, **kwargs):
        user = get_object_or_404(User, activation_key=kwargs['key'])
        if not user.is_verified:
            if timezone.now() <= user.expiry_date:
                user.is_verified = True
                user.save()

        url = user.get_absolute_url()
        if url:
            if self.permanent:
                return HttpResponsePermanentRedirect(url)
            else:
                return HttpResponseRedirect(url)
        else:
            logging.getLogger('django.request').warning(
                'Gone: %s', request.path,
                extra={'status_code': 410, 'request': request}
            )
            return HttpResponseGone()
