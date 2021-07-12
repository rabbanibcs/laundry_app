from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from order.models import Orders
from .managers import CustomUserManager


class Customer(AbstractUser):
    first_name = None
    last_name = None
    username = None

    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.PositiveBigIntegerField(null=True, blank=True)
    address = models.TextField(max_length=1000, null=True, blank=True)
    is_staff = models.BooleanField(default=False)

    is_active = models.BooleanField(default=False)
    device_id = models.PositiveBigIntegerField(null=True, blank=True)
    email_verification_code = models.PositiveBigIntegerField( null=True, blank=True)
    is_email_verified = models.BooleanField(default=False)
    email_verified_at = models.DateTimeField(null=True,blank=True)

    jwt_token = models.PositiveBigIntegerField( null=True, blank=True)
    status_message = models.CharField(max_length=200,null=True,blank=True)
    profile_photo = models.ImageField(upload_to='profile', null=True, blank=True)
    online_status = models.BooleanField(default=False)
    password_reset_code = models.PositiveIntegerField(null=True, blank=True)

    last_password_change_at = models.DateTimeField(default=timezone.now)
    deleted_by = models.CharField(max_length=200,null=True,blank=True)
    updated_at =  models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', ]
    objects = CustomUserManager()

    def __str__(self):
        return self.name or ''


class Review(models.Model):
    order = models.OneToOneField(Orders,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True)
    review_status = models.CharField(max_length=20)
    comments = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)


class Promotions(models.Model):
    order = models.OneToOneField(Orders,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    promotion_id = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)