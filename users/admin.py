from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import User, Order

admin.site.register(User, UserAdmin)
admin.site.register(Order)