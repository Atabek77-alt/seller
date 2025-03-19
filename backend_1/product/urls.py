from django.urls import path,include
from .views import *
# from rest_framework.routers import DefaultRouter
#
# router = DefaultRouter()
# router.register('product', ProductViewSets,basename='product')
# router.register('blog', BlogViewSets, basename='blog')





urlpatterns= [
    # path('', include(router.urls)),
    path('chat/',ChatView.as_view(), name='chat')

    # path('get-products/<int:pk>/',ProductByCategoryListApiView.as_view(),name='products'),
    # path('get-product/<int:pk>/', ProductDetailApiView.as_view(), name='product-detail'),
    # path('create-product/<int:pk>/', ProductUpdateDestroyApiView.as_view(), name='product-create'),
    # path('update-product/<int:pk>/', ProductUpdateApiView.as_view(), name='product-update'),
    # path('delete-product/<int:pk>/', ProductDestroyApiView.as_view(), name='product-delete'),
    # path('category',CategoryListApiView.as_view(),name='categories'),
    # path('get-products/',ProductViewSets.as_view({''}),name='products'),
]





