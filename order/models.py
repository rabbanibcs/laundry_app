from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings
from laundry.models import Laundry, Item

options = (('pending', 'pending'), ('processing', 'processing'), ('delivered', 'delivered'))
pay_methods = (('cash_on_delivery', 'cash_on_delivery'), ('bkash', 'bkash'),
               ('nagad', 'nagad'), ('rocket', 'rocket'), ('visa', 'visa'),
               ('mastercard', 'mastercard'),)


class Orders(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    laundry = models.ForeignKey(Laundry, on_delete=models.DO_NOTHING)
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    collection_address = models.TextField(max_length=500, null=True, blank=True)
    delivery_address = models.TextField(max_length=500, null=True, blank=True)

    customer_name = models.CharField(max_length=100, null=True, blank=True)
    customer_phone = models.PositiveBigIntegerField(validators=[MaxValueValidator(9999999999, 'Incorrect Phone number.'),MinValueValidator(1111111111, 'Incorrect Phone number.')])
    order_status = models.CharField(choices=options, default='pending', max_length=20)
    instructions = models.CharField(max_length=200, null=True, blank=True)
    expected_delivery_date = models.DateField(null=True, blank=True)

    subtotal = models.DecimalField(max_digits=6, decimal_places=2,default=0)
    discount = models.DecimalField(max_digits=6, decimal_places=2,default=0)
    total = models.DecimalField(max_digits=6, decimal_places=2,default=0)
    payment_method = models.CharField(choices=pay_methods, default='pending', max_length=20)

    processing_date = models.DateField(null=True, blank=True)
    cancel_date = models.DateField(null=True, blank=True)
    shipping_date = models.DateField(null=True, blank=True)
    received_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    order_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    @admin.display
    def edit(self):
        return format_html('<a href="{}/change/">Edit</a>', self.id)

    @admin.display
    def last_activity(self):
        return self.updated_at


class OrderItems(models.Model):
    order = models.ForeignKey(Orders,on_delete=models.CASCADE)
    item = models.ForeignKey(Item,on_delete=models.CASCADE)
    ld = models.DecimalField(max_digits=6, decimal_places=2,default=0)
    dc = models.DecimalField(max_digits=6, decimal_places=2,default=0)
    pr = models.DecimalField(max_digits=6, decimal_places=2,default=0)
    service_type = models.CharField(max_length=50)