from django import forms
from django.forms.utils import ErrorList
from django.http import HttpResponse
from django.views import View


class InstanceOwnerMixin(object):
    """
    InstanceOwnerMixin is to check if the user
    is the owner of the tweet or not
    """
    def form_valid(self, form):
        if form.instance.user == self.request.user:
            return super(InstanceOwnerMixin, self).form_valid(form)
        else:
            form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["You can't change or update this"])
            return self.form_invalid(form)

    def delete(self, request, *args, **kwargs):
        if request.user == self.get_object().user:
            return super(InstanceOwnerMixin, self).delete(request, *args, **kwargs)

        else:
            return HttpResponse("<h3>You don't have permission to delete this</h3>")


class VerifiedUserMixin(object):
    """
    VerifiedUserMixin is to check if the user
    is the owner is verified or not
    """
    def form_valid(self, form):
        if form.instance.user.is_verified:
            return super(VerifiedUserMixin, self).form_valid(form)
        else:
            form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["You have to verify your email"])
            return self.form_invalid(form)
