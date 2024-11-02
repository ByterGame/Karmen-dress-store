from django.urls import path
from yoomoney.views import create_payment_view

app_name = 'yoomoney'

urlpatterns = [
    path('create_payment/', create_payment_view, name='create_payment'),
    # path('payment-acceptance/', create_payment_acceptance, name='acceptance'), url для получение результата оплаты (на локал хосте его нет)
]
