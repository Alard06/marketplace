from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    last_name = models.CharField(max_length=50, blank=True, null=True)
    bonus = models.IntegerField(default=0)
    telephone_number = models.CharField(max_length=11)
    inn = models.CharField(max_length=40, null=True, blank=True)
    seller = models.BooleanField(default=False)
    permission_to_sell = models.BooleanField(default=False)
    age = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} : {self.username}'