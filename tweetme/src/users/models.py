from django.contrib.auth.models import AbstractUser
from django.db import models

from django.urls import reverse
from django.utils.text import slugify


class User(AbstractUser):
    slug = models.SlugField(default=None, blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    activation_key = models.TextField(default=None, null=True, max_length=40)
    expiry_date = models.DateTimeField(default=None, null=True)

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        self.slug = slugify(self.username)

    def get_absolute_url(self):
        return reverse("users:profile", kwargs={"username": slugify(self.username)})