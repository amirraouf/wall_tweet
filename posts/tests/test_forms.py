import pytest
from django.contrib.auth.models import AnonymousUser
from mixer.backend.django import mixer
from django.test import RequestFactory

from posts.forms import PostsForm

pytestmark = pytest.mark.django_db


class TestPostForm:
    def test_form(self):
        form = PostsForm(data={})
        assert form.is_valid() is False , 'Shouldn\'t be empty'

        user = AnonymousUser()
        form = PostsForm(data={'content': 'hello from test',
                               'user': user})
        assert form.is_valid() is False, 'Should be authorized'

        user = mixer.blend('users.User', is_verified=True)
        form = PostsForm(data={'content': 'hello from test',
                               'user': user})
        assert form.is_valid() is True, 'Should be authorized'