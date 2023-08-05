
from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from shop.models import Product, Category
from shop.serializers import ProductSerializers,CategorySerializers
from shop.views import ProductViewSet,CategoryViewSet
# Create your tests here.

class CategoryAPITestCase(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = CategoryViewSet.as_view({'get': 'list'})
        self.category_url = '/category/'  # URL của API danh sách sản phẩm
    def test_get_product_list(self):
        # Tạo một số sản phẩm giả để kiểm tra danh sách sản phẩm
        Category1 = Category.objects.create(name='Category 1', parent_category = 'a' )
        Category2 = Category.objects.create(name='Category 2', parent_category = 'b')

        request = self.factory.get(self.category_url)
        response = self.view(request)
        serializer = CategorySerializers([Category1, Category2], many=True)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)

class ProductAPITestCase(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = ProductViewSet.as_view({'get': 'list'})
        self.products_url = '/products/'  # URL của API danh sách sản phẩm
    def test_get_product_list(self):
        # Tạo một số sản phẩm giả để kiểm tra danh sách sản phẩm
        product1 = Product.objects.create(name='Product 1', category_id=1, price=10, quantity=5, image = None )
        product2 = Product.objects.create(name='Product 2', category_id=1, price=20, quantity=10, image =None)

        request = self.factory.get(self.products_url)
        response = self.view(request)
        serializer = ProductSerializers([product1, product2], many=True)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)

