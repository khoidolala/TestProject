from rest_framework import viewsets
from .models import Category, Product
from .serializers import CategorySerializers, ProductSerializers
from .serializers import MyTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from shop.filter import ProductFilter, CategoryFilter
from django_filters import rest_framework as filters
from .permissions import IsCreatorReadOnlyPermissions

class MyViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    filterset_class = CategoryFilter
    # permission_classes = IsCreatorReadOnlyPermissions
    # permission_classes = [IsCreatorReadOnlyPermissions]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = ProductFilter
    permission_classes = [IsCreatorReadOnlyPermissions]
    # permission_classes = [IsCreatorReadOnlyPermissions]

# class StaffViewSet(viewsets.ModelViewSet):
    # queryset = Staff.objects.all()
    # serializer_class = StaffSerializers


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
