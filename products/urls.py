from django.urls import path
from products.views import index, about, cart, checkout, single_product, checkout2

app_name = 'products'

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('cart/', cart, name='cart'),
    path('sign-in/', checkout, name='checkout'),
    path('sign-up/', checkout2, name='checkout2'),
    path('single-product/', single_product, name='single_product'),
]
