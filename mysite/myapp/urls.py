from django.urls import path
from . import views

app_name='myapp'

urlpatterns = [
  path('',views.IndexClassView.as_view(), name='index'),
  path('<int:id>/', views.detail, name='detail'),
  path('add/', views.create_item, name='create_item'),
  path('update/<int:id>/', views.update_item, name='update'),
  path('delete/<int:id>/', views.delete_item, name='delete'),

]