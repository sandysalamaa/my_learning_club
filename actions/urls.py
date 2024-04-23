from django.conf.urls import include
from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

# for modelviewsets only
# router = DefaultRouter()
# router.register('products',ProductViewSet,basename = 'products')


urlpatterns = [
    # path('',include(router.urls))
    # path('product/<int:pk>/', ProductApiView.as_view(),name='get-product'),
    # path('product/', ProductApiView.as_view(),name='create-product'),
    path('products/', get_all_products ,name='all-products'),
    path('products/<int:pk>/', product_detail ,name='all-products'),
]
