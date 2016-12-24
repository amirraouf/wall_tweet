from django.contrib.auth.models import AbstractUser
from django.db import models

from django.urls import reverse
from django.utils.text import slugify


class User(AbstractUser):
    slug = models.SlugField(default=None, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super(User, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("users:profile", kwargs={"username": slugify(self.username)})