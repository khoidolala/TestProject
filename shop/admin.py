from django.contrib import admin
from .models import Category, Product, Staff
from django.utils.html import format_html
from django.utils.safestring import mark_safe
# from .permissions import IsCreatorReadOnlyPermissions
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


class PriceRangeFilter(admin.SimpleListFilter):
    title = ('Price Range')
    parameter_name = 'price_range'

    def lookups(self, request, model_admin):
        return (
            ('0-20', _('0-20')),
            ('21-50', _('21-50')),
            ('>50', _('>50')),
        )

    def queryset(self, request, queryset):
        if self.value() == '0-20':
            return queryset.filter(price__gte=0, price__lte=20)
        elif self.value() == '21-50':
            return queryset.filter(price__gt=20, price__lte=50)
        elif self.value() == '>50':
            return queryset.filter(price__gt=50)
        else:
            return queryset


class ProductAdmin(admin.ModelAdmin):

    list_display = ['name', 'price', 'quantity', 'image', 'category_name',
                    'detail_link']
    list_filter = ['category__name', QuantityRangeFilter, PriceRangeFilter]
    search_fields = ['name', 'category__name']

    def has_change_permission(self, request, obj=None):
        if obj is not None and obj.created_by == request.user:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if obj is not None and obj.created_by == request.user:
            return True
        return False
    # permission_classes = [IsCreatorReadOnlyPermissions]

    def category_name(self, obj):
        return obj.category.name

    def display_image(self, obj):
        image_url = obj.image.url if obj.image else ''
        return mark_safe(
            f'<img src="{image_url}" alt="{obj.name}" height="100" width="100">')
    display_image.short_description = 'Image'

    def detail_link(self, obj):
        return format_html('<a href="/admin/shop/product/{}/change/">View</a>',
                           obj.id)
    detail_link.short_description = 'Detail'
    detail_link.allow_tags = True


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent_category', 'products_count']
    readonly_fields = ['products_count']
    search_fields = ['name']

    def products_count(self, obj):
        return obj.product_set.count()

    def has_change_permission(self, request, obj=None):
        if obj is not None and obj.created_by == request.user:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if obj is not None and obj.created_by == request.user:
            return True
        return False


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Staff)
