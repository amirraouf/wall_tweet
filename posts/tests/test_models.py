import pytest
from mixer.backend.django import mixer

pytestmark = pytest.mark.django_db

class TestPost:
    def test_init(self):
        obj = mixer.blend('posts.Posts')
        assert obj.pk == 1, 'Should create a Post instance'