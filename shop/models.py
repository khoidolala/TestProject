from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    parent_category = models.CharField(max_length=100)
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True,
        related_name='category_created')


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    image = models.ImageField(upload_to="")
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True,
        related_name='products_created')


class Staff(User):
    position = models.CharField(max_length=100)
    department = models.CharField(max_length=100)

    class Meta:
        # Thiết lập bảng database tương ứng với Staff model
        db_table = 'staff'
