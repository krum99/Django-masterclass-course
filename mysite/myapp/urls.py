from django.urls import path
from . import views

from django.views.decorators.cache import cache_page

app_name='myapp'

urlpatterns = [
  path('',cache_page(15 * 60) (views.index), name='index'),
  path('<int:pk>/', views.FoodDetail.as_view(), name='detail'),
  path('add/', views.ItemCreateView.as_view(), name='create_item'),
  path('update/<int:pk>/', views.ItemUpdateView.as_view(), name='update'),
  path('delete/<int:pk>/', views.ItemDeleteView.as_view(), name='delete'),
]