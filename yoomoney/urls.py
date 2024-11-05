from django.urls import path
from yoomoney.views import create_payment_view, create_payment_acceptance

app_name = 'yoomoney'

urlpatterns = [
    path('create_payment/<int:total>/<str:str_dresses>/<str:count>/<str:sizes>', create_payment_view, name='create_payment'),
    path('payment-acceptance/', create_payment_acceptance, name='acceptance'),
]
