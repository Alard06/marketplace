from django.contrib.auth.models import User
from django.db import models


class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, default='', null=True, blank=True)
    email = models.EmailField(null=True, blank=True, unique=True)
    bonus = models.IntegerField(default=0)
    telephone = models.CharField(max_length=11)
    seller = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name

