from django.urls import path
from yoomoney.views import create_payment_view, payment_accept

app_name = 'yoomoney'

urlpatterns = [
    path('create_payment/', create_payment_view, name='create_payment'),
    path('payment-accept/<int:id>', payment_accept, name='payment-accept'),
]
