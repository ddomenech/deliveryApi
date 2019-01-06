# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Customer(models.Model):
    code=models.CharField(verbose_name='Código Cliente', max_length=256)
    name=models.CharField(verbose_name='Nombre Cliente', max_length=1400)
    description=models.CharField(verbose_name='Descripción Cliente', max_length=2400)
    created=models.DateTimeField(verbose_name='Fecha Creación', auto_now_add=True)
    shipped=models.DateTimeField(verbose_name='Fecha Envio')

    def __str__(self):
        return '%s %s'%(self.name, self.description)
    
class Address(models.Model):
    street=models.CharField(max_length=1400)
    zipcode=models.IntegerField(null=True, default=0)
    countrycode=models.CharField(max_length=2)
    created=models.DateTimeField(verbose_name='Fecha Creación', auto_now_add=True)
    customer=models.ForeignKey(Customer, related_name='address', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.street

class Delivery(models.Model):
    description=models.CharField(verbose_name='Descripción',max_length=1800)
    created=models.DateTimeField(verbose_name='Fecha Creación',auto_now_add=True)
    shipped=models.DateTimeField(verbose_name='Fecha Envio')
    customer=models.ForeignKey(Customer, related_name='delivery')
    address=models.ForeignKey(Address, related_name='delivery_address')
    
    def __str__(self):
        return self.description
