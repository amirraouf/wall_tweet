from django import forms
from .models import Posts


class PostsForm(forms.ModelForm):
    content = forms.CharField(label='', max_length=140, widget=forms.Textarea(
        attrs={
            'placeholder': "Your Post text",
            'class': "form-control",
            'style': "height:50px"
        }
    ))
    image = forms.ImageField(label='')
    privacy = forms.ChoiceField(label='', choices=Posts.PRIVACY, widget=forms.Select(
        attrs={
            'class': "form-control Selector col-sm-offset-10",
            'style': "width:130px"

        }))

    class Meta:
        model = Posts
        fields = [
            'content',
            'image',
            'privacy',
        ]
        exclude = [
            'timestamp',
            'updated',
            'user',
        ]