from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter
from django.views.decorators.cache import cache_page

from rest_framework_simplejwt.views import (
  TokenObtainPairView,
  TokenRefreshView,
)

app_name='myapp'

router = DefaultRouter()
router.register(r"items", views.ItemViewSet, basename='item')
router.register(r"orders", views.OrderViewSet, basename='order')

urlpatterns = [
  path("api/token/", TokenObtainPairView.as_view(), name='token_obtain_pair'),
  path("api/token/refresh/", TokenRefreshView.as_view(), name='token_refresh'),
  path("api/", include(router.urls)),
  # URL api build with DRF
  # path('api/items', views.ItemListCreateAPI.as_view(), name='item_list_api' ),
  #URL pattern for single item
  # path('api/items/<int:pk>/', views.ItemRetrieveUpdateDestroyAPIView.as_view(), name='item_detail_api' ),
  #Django app urls
  path('', views.index, name='index'),
  path('<int:id>/', views.detail, name='detail'),
  path('add/', views.create_item, name='create_item'),
  path('update/<int:pk>/', views.ItemUpdateView.as_view(), name='update'),
  path('delete/<int:pk>/', views.ItemDeleteView.as_view(), name='delete'),
]