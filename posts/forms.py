from django import forms
from posts.models import Posts
from posts.validators import validate_content


class PostsForm(forms.ModelForm):
    """
    PostsForm model form for tweets and used allover the posts app
    """
    content = forms.CharField(label='', max_length=140, validators=[validate_content],
                              widget=forms.Textarea(
                                attrs={
                                    'placeholder': "Your Post text",
                                    'class': "form-control",
                                    'style': "height:50px"
                                }
                            ))
    image = forms.ImageField(label='', required=False)
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