from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('<slug:slug>', views.detail, name='detail')
]