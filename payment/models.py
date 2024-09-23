from django.db import models


class Payment(models.Model):
    name = models.CharField(max_length=100, verbose_name='name')
    amount = models.CharField(max_length=100, verbose_name='amount')
    email = models.CharField(max_length=100, verbose_name='email')

    class Meta:
        verbose_name = 'payment'
        verbose_name_plural = 'payments'

