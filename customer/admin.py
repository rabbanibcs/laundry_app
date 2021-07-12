from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Customer
from django.conf import settings


class CustomUserAdmin(UserAdmin):
    model = settings.AUTH_USER_MODEL
    fieldsets = (
        (None, {'fields': ( 'email','password')}),
        ('Personal info', {'fields': ('name','phone','address')}),
        ('Permissions', {
            'fields': ('is_active','is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name','email','phone','password1', 'password2'),
        }),
    )
    list_display = ('id','name', 'email','phone', 'last_login','is_staff')
    search_fields = ('name', 'email','phone')
    ordering = ('name',)


admin.site.register(Customer, CustomUserAdmin)


