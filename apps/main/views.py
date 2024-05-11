from django.shortcuts import render

from CustomUser.models import CustomUser
from django.db.models import Q

from apps.product.models import Product


def index(request):
    seller = True if CustomUser.objects.filter(Q(pk=request.user.pk) & Q(seller=True)).exists() else False

    products = Product.objects.all()[:10]

    return render(request, 'main/index.html', context={'seller': seller, 'products': products})
