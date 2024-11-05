from django.db import models
from products.models import Dress
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    like = models.ManyToManyField(Dress, related_name='liked_by_users')
    cart = models.ManyToManyField(Dress, related_name='carted_by_users')
    fullname = models.CharField(max_length=100, default='')
    phone = models.CharField(max_length=20, default='')
    address = models.CharField(max_length=255, default='')
    postal_code = models.CharField(max_length=6, default='')


class Order(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, null=False)
    items = models.JSONField(null=False)
    order_sum = models.FloatField(null=False)
    shipping_info = models.JSONField(null=False)
    is_paid = models.BooleanField(null=False, default=False)
    status = models.CharField(max_length=100, null=False, default='In processing')

    def __str__(self):
        return f"Order: {self.id} from user: {self.user}"

    def calculate_order_sum(self):
        answer = 0
        for order_elem in self.items:
            dress = Dress.objects.get(id=int(order_elem['id']))
            answer += dress.cost * int(order_elem['quantity'])
        self.order_sum = answer
