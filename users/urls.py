from django.urls import path
from users.views import sign_in, sign_up, logout, add_to_cart, add_to_likes, remove_from_cart, remove_from_likes, add_shipping_information, make_superuser

app_name = 'users'

urlpatterns = [
    path('sign-in/', sign_in, name='sign-in'),
    path('sign-up/', sign_up, name='sign-up'),
    path('logout/', logout, name='logout'),
    path('add-to-cart/', add_to_cart, name='add_to_cart'),
    path('add-to-likes/', add_to_likes, name = 'add_to_likes'),
    path('remove-from-cart/', remove_from_cart, name='remove_from_cart'),
    path('remove-from-likes/', remove_from_likes, name = 'remove_from_likes'),
    path('add-shipping-information/', add_shipping_information, name='add_shipping_information'),
    path('make-superuser/<int:id>/', make_superuser, name='make_superuser'),
]
