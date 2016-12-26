import datetime
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm as AbstractUserCreationForm


from .utils import generate_activation_key
User = get_user_model()


class UserCreationForm(AbstractUserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.is_verified = False
        user.expiry_date = datetime.datetime.strftime(datetime.datetime.now() + datetime.timedelta(days=2),
                                                      "%Y-%m-%d %H:%M:%S")
        user.activation_key = generate_activation_key(user.username)

        if commit:
            user.save()

        return user
