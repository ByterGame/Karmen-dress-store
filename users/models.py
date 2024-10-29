from django.db import models
from products.models import Dress
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    like = models.ManyToManyField(Dress)
