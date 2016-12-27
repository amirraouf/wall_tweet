from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.http import HttpRequest
from django.test import TestCase
import unittest

from django.urls import reverse
from posts.models import Posts
from posts.forms import PostsForm
from posts.views import PostCreateView

# Tests are dummy here -- To be continued


class PostsTestCase(TestCase):
    def setUp(self):
        Posts.objects.create(content="", user="1", privacy="pb")
        Posts.objects.create(content="new tweet from test", user="1", privacy='pr')

    def test_posts_valid(self):
        """Posts that has validation are correctly identified"""
        first = Posts.objects.get(id=1)
        second = Posts.objects.get(name="cat")
        self.assertEqual(first.__str__(), ValidationError)
        self.assertEqual(second.__str__(), 'new tweet from test')


class PostDetailViewTests(TestCase):
    def test_detail_view_with_invalid_id(self):
        """
        The detail view of a question with a pk in the future should
        return a 404 not found.
        """
        post = Posts(content='Future tweet.', privacy="pb")
        url = reverse('posts:detail', args=(22,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_detail_view_with_valid_id(self):
        """
        The detail view of a question with a pk that exist should
        display the post's content.
        """
        post = Posts(content='Future tweet.', privacy="pb")
        url = reverse('posts:detail', args=(post.id,))
        response = self.client.get(url)
        self.assertContains(response, post.content)
        self.assertEqual(response.status_code, 200)


# Test with Unit Test


class PostCreateViewTest(unittest.TestCase):
    def setUp(self):
        self.view = PostCreateView.as_view({self.template_name:'posts/create.html',
                                            self.form_class:PostsForm,
                                            self.request:HttpRequest(),
                                            self.request.user: get_user_model().objects.get(id=1)
                                            })

    def test_form_dot_save_called_with_user(self):
        """
        The create view of a post with user that exist should
        save the instance user.
        """
        self.view.form_valid(self.form_class)
        self.form.save.assert_called_once_with(user=self.request.user)


    @patch('lists.views.redirect')
    def test_redirect(self, form_redirect):
        """
        The create view of a post with user that exist should
        display the post's list view.
        """
        self.view.form_valid(self.form_class)
        form_redirect.assert_called_once_with(reverse('posts:list'))
