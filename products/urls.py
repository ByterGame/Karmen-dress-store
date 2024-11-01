from django.urls import path
from products.views import index, about, cart, checkout, single_product, search, likes

app_name = 'products'

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('cart/', cart, name='cart'),
    path('likes/', likes, name = 'likes'),
    path('checkout/', checkout, name='checkout'),
    path('single_product/<int:id>/', single_product, name='single_product'),
    path('search/', search, name='search')
]
