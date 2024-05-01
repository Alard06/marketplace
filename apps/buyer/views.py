from django.contrib.auth import logout
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from apps.buyer.forms import RegisterBuyerForm


class BuyerRegisterView(CreateView):
    form_class = RegisterBuyerForm
    template_name = 'buyer/register.html'
    success_url = reverse_lazy('index')


class BuyerLoginView(LoginView):
    template_name = 'buyer/login.html'

    def get_success_url(self):
        return reverse_lazy('index')



def logout_view(request):
    logout(request)
    return redirect('/')