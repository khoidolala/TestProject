from django.contrib import admin
from .models import Category, Product, Staff
from django.db.models import Count
from django.utils.html import format_html
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.db.models import Q
# Register your models here.
from django.utils.translation import gettext_lazy as _

class QuantityRangeFilter(admin.SimpleListFilter):
    title = _('Quantity Range')
    parameter_name = 'quantity_range'

    def lookups(self, request, model_admin):
        return (
            ('0-20', _('0-20')),
            ('21-50', _('21-50')),
            ('>50', _('>50')),
        )

    def queryset(self, request, queryset):
        if self.value() == '0-20':
            return queryset.filter(quantity__gte=0, quantity__lte=20)
        elif self.value() == '21-50':
            return queryset.filter(quantity__gt=20, quantity__lte=50)
        elif self.value() == '>50':
            return queryset.filter(quantity__gt=50)
        else:
            return queryset

class ProductAdmin(admin.ModelAdmin):
    '''list_display = ('id', 'name', 'category', 'price', 'quantity')
    list_filter = ('category', 'quantity')
    search_fields = ('name', 'category_name')

    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)
        if obj:
            fields.append('detail_link')
        return fields

    def category_name(self, obj):
        return obj.category.name
    category_name.admin_order_fiedl = 'id'
    
    list_display = ('id', 'name', 'category', 'category_name', 'price', 'quantity')'''
    list_display = ['name', 'price', 'quantity', 'image', 'category_name', 'detail_link']
    list_filter = ['category__name', QuantityRangeFilter]
    search_fields = ['name', 'category__name']

    def category_name(self, obj):
        return obj.category.name
    
    def display_image(self, obj):
        image_url = obj.image.url if obj.image else ''
        return mark_safe(f'<img src="{image_url}" alt="{obj.name}" height="100" width="100">')
    display_image.short_description = 'Image'

    def detail_link(self, obj):
        return format_html('<a href="/admin/shop/product/{}/change/">View</a>', obj.id)
    detail_link.short_description = 'Detail'
    detail_link.allow_tags = True

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent_category', 'products_count']
    readonly_fields = ['products_count']

    def products_count(self, obj):
        return obj.product_set.count()

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Staff)