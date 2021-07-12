from django import forms
from django.conf import settings
from customer.models import Customer
from django.contrib.auth.forms import UserCreationForm


class CustomerCreationForm(UserCreationForm):
    name = forms.CharField(max_length=200)

    class Meta:
        model = Customer
        fields = ['name','email', 'password1', 'password2']
