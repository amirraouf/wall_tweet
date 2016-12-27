import pytest
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from mixer.backend.django import mixer
from django.test import RequestFactory, Client

from posts.views import PostListView, PostCreateView, PostUpdateView

User = get_user_model()
pytestmark = pytest.mark.django_db

class TestPostListView:
    def test_anonymous(self):
        req = RequestFactory().get('/')
        resp = PostListView.as_view()(req)
        assert resp.status_code == 200, 'Should be called by anyone'


class TestPostCreateView:
    def test_anonymous(self):
        req = RequestFactory().get('/')
        req.user = AnonymousUser()
        resp = PostCreateView.as_view()(req)
        assert resp.status_code == 302, 'Shouldn\'t be called by anyone'
        assert 'login' in resp.url

    @pytest.mark.django_db(transaction=True)
    def test_authenticated(self):
        req = RequestFactory().get('/')
        req.user = mixer.blend('users.User')
        resp = PostCreateView.as_view()(req)
        assert resp.status_code == 200, 'Should be called by authenticated'


class TestPostUpdateView:
    @pytest.mark.django_db(transaction=True)
    def test_post(self):
        """
        Test post http method
        :return:
        """
        post = mixer.blend('posts.Posts', content='hello')
        data = {'content': 'hello test'}
        req = RequestFactory().post('/', data=data)
        req.user = post.user
        resp = PostUpdateView.as_view()(req, pk=post.pk)
        assert resp.status_code == 302, 'Should redirect to listview'
        post.refresh_from_db()
        assert post.content == 'hello test', 'Should update the post'
