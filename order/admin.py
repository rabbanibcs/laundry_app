from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.auth.models import Group

from laundry.models import Laundry, Category, Item
from order.models import Orders


class OrderAdmin(AdminSite):
    site_header = 'Dashboard'
    index_title = ''
    site_title = 'Admin'
    login_template = 'login.html'


@admin.action(description='Mark selected orders as processing')
def make_processing(modeladmin, request, queryset):
    queryset.update(order_status='processing')


@admin.action(description='Mark selected orders as delivered')
def make_delivered(modeladmin, request, queryset):
    queryset.update(order_status='delivered')


admin.site.index_title = ''
admin.site.site_header = 'Dashboard'
admin.site.site_title = 'Admin'


class CustomOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'customer_phone', 'last_activity', 'order_status', 'edit')
    # fields =  ( 'name', 'phone', 'status', )
    list_display_links = ('customer_name', 'customer_phone',)
    search_fields = ('customer_name', 'customer_phone',)
    save_on_top = True
    list_filter = ('order_date',)
    # list_editable = ()
    # readonly_fields = ('collection_address','delivery_address',)
    actions = [make_processing, make_delivered]


order_site = OrderAdmin(name='order_admin')
order_site.register(Orders, CustomOrderAdmin)

admin.site.register(Orders)
admin.site.register(Laundry)
admin.site.register(Category)
admin.site.register(Item)
admin.site.unregister(Group)
