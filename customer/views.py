from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import CustomerCreationForm
from verify_email.email_handler import send_verification_email


def create_customer(request):
    if request.method == 'POST':
        form = CustomerCreationForm(request.POST)
        if form.is_valid():
            inactive_user = send_verification_email(request, form)
            messages.success(request, ' We’ve emailed you with instructions. Please verify your email account. ')
            return redirect('login')
    else:
        form = CustomerCreationForm()
    return render(request,'registration.html',{'form':form})
