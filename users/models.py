from django.db import models
from products.models import Dress
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    like = models.ManyToManyField(Dress, related_name='liked_by_users')
    cart = models.ManyToManyField(Dress, related_name='carted_by_users')
    # full_name = models.CharField(max_length=100, default='')
    # phone_number = models.CharField(max_length=15, default='')
    # address = models.CharField(max_length=255, default='')
    # postal_code = models.CharField(max_length=6, default='')