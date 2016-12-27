from django.db import models
from django.conf import settings
from django.urls import reverse

from posts.utils import generate_image_name
from posts.validators import validate_content


class Posts(models.Model):
    """
    Tweets model class
    """
    PRIVACY = (
        ('pb', 'Public'),
        ('pr', 'Private'),
    )

    content     = models.CharField(max_length=140, null=False, validators=[validate_content])
    user        = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1, related_name='posts')
    image       = models.ImageField(upload_to=generate_image_name, null=True, blank=True)
    privacy     = models.CharField(max_length=2, choices=PRIVACY, default='pb')
    timestamp   = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-timestamp"]
        verbose_name_plural = "Posts"

    def __str__(self):
        return str(self.content)

    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"pk": self.pk})
