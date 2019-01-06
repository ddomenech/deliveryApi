# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Customer, Address, Delivery

# Register your models here.
@admin.register(Customer, Delivery, Address)
class AuthorAdmin(admin.ModelAdmin):
    pass