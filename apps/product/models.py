from django.db import models
from unidecode import unidecode

from CustomUser.models import CustomUser
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=40)
    subcategories = models.ManyToManyField('SubCategory', blank=True, related_name='subcategories')
    slug = models.SlugField(max_length=40, unique=True, blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(unidecode(self.name))
        super().save(*args, **kwargs)


class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=40, unique=True, blank=True, null=True)
    products = models.ManyToManyField('Product',  blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(unidecode(self.name))
        super().save(*args, **kwargs)


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    characteristic = models.TextField(max_length=500)
    # image = models.ImageField(upload_to='')
    seller = models.ManyToManyField(CustomUser, blank=True)

    def __str__(self):
        return self.name


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.quantity} x {self.product.name}'
