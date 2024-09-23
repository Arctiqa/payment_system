from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    username = None
    email = models.EmailField(max_length=100, unique=True, verbose_name='email')
    is_subscribed = models.BooleanField(verbose_name='subscription')
    subscription_expiration = models.DateTimeField(verbose_name='time', null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'