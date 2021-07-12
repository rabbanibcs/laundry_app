from django.db import models
from django.contrib import admin
from django.utils import timezone
from django.utils.html import format_html
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings

options = (('pending', 'pending'), ('processing', 'processing'), ('delivered', 'delivered'))
pay_methods = (('cash_on_delivery', 'cash_on_delivery'), ('bkash', 'bkash'),
                ('nagad', 'nagad'), ('rocket', 'rocket'), ('visa', 'visa'),
                ('mastercard', 'mastercard'),)


class Laundry(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=500, null=True, blank=True)
    phone = models.PositiveBigIntegerField(validators=[MaxValueValidator(9999999999, 'Incorrect Phone number.'),
                                                       MinValueValidator(1111111111, 'Incorrect Phone number.')])
    profile_photo = models.ImageField(upload_to='laundries')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Laundry'
        verbose_name_plural = 'Laundries'

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    laundry = models.ForeignKey(Laundry, on_delete=models.SET_NULL,null=True)
    profile_photo = models.ImageField(upload_to='categories')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title


class Item(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    laundry = models.ForeignKey(Laundry, on_delete=models.SET_NULL,null=True)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)

    ld = models.DecimalField(max_digits=6, decimal_places=2,default=0)
    dc = models.DecimalField(max_digits=6, decimal_places=2,default=0)
    pr = models.DecimalField(max_digits=6, decimal_places=2,default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
