from django.urls import path
from users.views import logout, add_to_cart, add_to_likes, remove_from_cart, remove_from_likes

app_name = 'users'

urlpatterns = [
    path('logout/', logout, name='logout'),
    path('add-to-cart/', add_to_cart, name='add_to_cart'),
    path('add-to-likes/', add_to_likes, name = 'add_to_likes'),
    path('remove-from-cart/', remove_from_cart, name='remove_from_cart'),
    path('remove-from-likes/', remove_from_likes, name = 'remove_from_likes'),
]
