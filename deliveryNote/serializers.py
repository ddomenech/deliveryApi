from rest_framework import serializers
from .models import Customer, Delivery, Address

class CustomerSerializer(serializers.ModelSerializer):
    address=serializers.SlugRelatedField(many=True, read_only=True, slug_field='street')
    delivery=serializers.SlugRelatedField(many=True, read_only=True, slug_field='delivery')

    class Meta:
        model = Customer
        fields = '__all__'

class AdressSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Address
        fields = '__all__'

class DeliverySerializer(serializers.ModelSerializer):

    class Meta:
        model = Delivery
        fields = '__all__'
    