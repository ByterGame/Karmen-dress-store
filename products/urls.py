from django.urls import path
from products.views import (index, about, cart, checkout,
                            single_product, search, likes,
                            admin_panel, admin_dresses,
                            update_dress, add_dress, orders,
                            make_available, admin_orders,
                            update_order_status)

app_name = 'products'

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('cart/', cart, name='cart'),
    path('likes/', likes, name = 'likes'),
    path('checkout/', checkout, name='checkout'),
    path('single_product/<int:id>/', single_product, name='single_product'),
    path('search/', search, name='search'),
    path('admin-panel/', admin_panel, name='admin-panel'),
    path('admin-dresses/', admin_dresses, name='admin-dresses'),
    path('update-dress/<int:id>/', update_dress, name='update_dress'),
    path('add-dress/', add_dress, name='add-dress'),
    path('orders/', orders, name='orders'),
    path('make-available/<int:id>/', make_available, name='make-available'),
    path('admin-orders/', admin_orders, name='admin-orders'),
    path('update_order_status/<int:id>/', update_order_status, name='update_order_status'),
]
