from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class CustSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customers
        fields=["username","password"]
        # fields="__all__"

class ProductSerializer(serializers.ModelSerializer):
    br_name = serializers.CharField(read_only=True, source='br_id.br_name')    
    ct_name = serializers.CharField(read_only=True, source='ct_id.ct_name')    
    class Meta:
        model=Products
        fields="__all__"
        


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields="__all__"

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model=Brand
        fields="__all__"

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Banner
        fields="__all__"