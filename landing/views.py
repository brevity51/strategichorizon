from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SubscriptionForm
from .models import Subscriber

def index(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = SubscriptionForm()
    
    return render(request, 'landing/index.html', {'form': form})

def success(request):
    return render(request, 'landing/success.html')