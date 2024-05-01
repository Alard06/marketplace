from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=40)
    subcategories = models.ForeignKey('SubCategory', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    characteristic = models.TextField(max_length=500)
    #image = models.ImageField(upload_to='')
    subcategory = models.ManyToManyField(SubCategory)

    def __str__(self):
        return self.name

