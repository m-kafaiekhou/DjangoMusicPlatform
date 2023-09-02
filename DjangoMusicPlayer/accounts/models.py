from django.db import models
from django.contrib.auth.models import AbstractUser

# Local Imports

# Models


class CustomUser(AbstractUser):
    STATUS_CHOICES = (
        ('f', 'Free'),
        ('b', 'Base'),
        ('p', 'Premium'),
    )
    status = models.CharField(choices=STATUS_CHOICES, max_length=1)
    email = models.EmailField(verbose_name="email address", blank=False, null=False, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


