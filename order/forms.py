from django import forms
from .models import Orders


class OrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        # fields = '__all__'
        exclude = ['order_status','customer','expected_delivery_date','subtotal',
                   'discount','total','processing_date','cancel_date','shipping_date',
                   'received_date','created_at','updated_at','order_date']
