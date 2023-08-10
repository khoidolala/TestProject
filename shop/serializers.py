from rest_framework import serializers
from .models import Category, Product, Staff
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CategorySerializers(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializers(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source='category.name')
    
    class Meta:
        model = Product
        fields = '__all__'


class StaffSerializers(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        return token
