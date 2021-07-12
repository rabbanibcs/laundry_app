from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import OrderForm


def place_order(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order=form.save(commit=False)
            # print(request.user.name)
            order.customer = request.user
            order.save()
            messages.success(request, 'Your order has been placed.')
            return redirect('home')
    else:
        form = OrderForm()
    return render(request, 'order_form.html',{'form' : form})
