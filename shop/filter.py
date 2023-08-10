import django_filters
from shop.models import Product, Category


class ProductFilter(django_filters.FilterSet):

    name = django_filters.CharFilter(lookup_expr='contains')
    min_price = django_filters.NumberFilter(
        field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(
        field_name='price', lookup_expr='lte')

    class Meta:
        models = Product
        filds = ['name', 'min_price', 'max_price']


class CategoryFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='contains')

    class Meta:
        models = Category
        filds = ['name']
