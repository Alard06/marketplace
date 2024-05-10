from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy

from CustomUser.models import CustomUser
from apps.seller.forms import SenderForm
from apps.seller.models import SellerApplication


def seller_index(request):
    return render(request, 'seller/seller_index.html')


def seller_register(request):
    if request.method == 'POST':
        form = SenderForm(request.POST)
        if form.is_valid():
            if not SellerApplication.objects.filter(inn=form.cleaned_data['inn'], email=form.cleaned_data[
                'email']).exists() and not CustomUser.objects.filter(inn=form.cleaned_data['inn'],
                                                                     email=form.cleaned_data['email']).exists():
                SellerApplication.objects.create(
                    last_name=form.cleaned_data['last_name'],
                    first_name=form.cleaned_data['first_name'],
                    patronymic=form.cleaned_data['patronymic'],
                    email=form.cleaned_data['email'],
                    name=form.cleaned_data['name'],
                    inn=form.cleaned_data['inn'],
                    description=form.cleaned_data['description'],
                    phone_number=form.cleaned_data['phone_number']
                )
                return HttpResponseRedirect(reverse_lazy('index'))
            else:
                return HttpResponseRedirect(reverse_lazy('seller_register'))
    else:
        form = SenderForm()
    return render(request, 'seller/seller_register.html', {'form': form})



