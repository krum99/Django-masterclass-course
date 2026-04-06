from django.urls import path
from . import views

from django.views.decorators.cache import cache_page

app_name='myapp'

urlpatterns = [
  # URL api build with DRF
  path('items-api/', views.item_list_api, name='item_list_api' ),
  #URL pattern for single item
  path('api/items/<int:pk>/', views.item_detail_api, name='item_detail_api' ),
  # URL api
  path('items-json/', views.item_list_json, name='item_list_json' ),
  #Django app urls
  path('', views.index, name='index'),
  path('<int:id>/', views.detail, name='detail'),
  path('add/', views.create_item, name='create_item'),
  path('update/<int:pk>/', views.ItemUpdateView.as_view(), name='update'),
  path('delete/<int:pk>/', views.ItemDeleteView.as_view(), name='delete'),
]