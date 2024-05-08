from django.db import models


class Owner(models.Model):
    ROLES = (
        ('A', 'Administrator'),
        ('O', 'OWNER'),
        ('N', 'NoName')
    )
    role = models.CharField(max_length=1, choices=ROLES, default='N')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    telegram_id = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}: {self.telegram_id}: {self.role}'

