from django.shortcuts import render


def seller_index(request):
    return render(request, 'seller/seller_index.html')


def seller_register(request):
    return render(request, 'seller/seller_register.html')