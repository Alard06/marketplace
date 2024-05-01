from http.client import HTTPResponse

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from apps.seller.forms import SenderForm


def seller_index(request):
    return render(request, 'seller/seller_index.html')


def seller_register(request):
    if request.method == 'POST':
        form = SenderForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = SenderForm()
    return render(request, 'seller/seller_register.html', {'form': form})
