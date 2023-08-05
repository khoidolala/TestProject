from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
# router.register(r'staff', StaffViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain-pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]
