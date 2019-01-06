# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Customer, Address, Delivery
from .serializers import CustomerSerializer, DeliverySerializer, AdressSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# Create your views here.
class DeliveryListView(ListCreateAPIView):
    queryset=Delivery.objects.all()
    serializer_class=DeliverySerializer
    
class DeliveryDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Delivery.objects.all()
    serializer_class=DeliverySerializer

class CustomerListView(ListCreateAPIView):
    queryset=Customer.objects.all()
    serializer_class=CustomerSerializer

class CustomerDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Customer.objects.all()
    serializer_class=CustomerSerializer

class AddressListView(ListCreateAPIView):
    queryset=Address.objects.all()
    serializer_class=AdressSerializer

class AddressDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Address.objects.all()
    serializer_class=AdressSerializer
