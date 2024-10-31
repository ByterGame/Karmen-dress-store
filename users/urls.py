from django.urls import path
from users.views import sign_in, sign_up, logout, add_to_cart

app_name = 'users'

urlpatterns = [
    path('sign-in/', sign_in, name='sign-in'),
    path('sign-up/', sign_up, name='sign-up'),
    path('logout/', logout, name='logout'),
    path('add-to-cart/', add_to_cart, name='add_to_cart'),
]
