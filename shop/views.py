from django.shortcuts import render
from rest_framework import viewsets
from .models import Category, Product, Staff
from .serializers import CategorySerializers, ProductSerializers, StaffSerializers, MyTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated

class MyViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

# class StaffViewSet(viewsets.ModelViewSet):
    # queryset = Staff.objects.all()
    # serializer_class = StaffSerializers

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
