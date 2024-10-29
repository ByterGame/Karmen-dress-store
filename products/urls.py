from django.urls import path
from products.views import index, about, cart, checkout,single_product

app_name = 'products'

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('single_product/<int:id>/', single_product, name='single_product')
]
