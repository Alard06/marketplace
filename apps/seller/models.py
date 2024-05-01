from django.contrib.auth.models import User
from django.db import models


"""
class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    products = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    seller = models.BooleanField(default=True)
    telephone = models.CharField(max_length=11)

    def __str__(self):
        return self.name
"""