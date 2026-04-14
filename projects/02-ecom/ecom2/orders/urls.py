from django.urls import path
from .import views

urlpatterns = [
  path('add-address', views.add_address, name='add_address'),
  path('checkout/',views.checkout,name='checkout'),
  path('place-order',views.place_order,name='place-order'),
]