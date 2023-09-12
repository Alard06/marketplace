from django.contrib.auth.models import User
from django.db import models


class BuyerUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bonus = models.PositiveIntegerField(default=0)
    phone_number = models.CharField(max_length=30)
    # buy =


class SellerUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=30)