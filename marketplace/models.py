from django.db import models

from user.models import CustomUser


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='название')
    price = models.PositiveIntegerField(verbose_name='цена')
    seller = models.ManyToManyField(CustomUser, verbose_name='продавец')
    description = models.TextField(verbose_name='описание')
    characteristics = models.ForeignKey('Characteristics',
                                        on_delete=models.CASCADE,
                                        verbose_name='характеристики')
    reviews = models.ForeignKey('Review',
                                on_delete=models.CASCADE,
                                verbose_name='отзывы')
    number_of_purchases = models.PositiveIntegerField()


class Characteristics(models.Model):
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=100)


class Review(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.TextField()
    like = models.PositiveIntegerField()
    dislike = models.PositiveIntegerField()

