from django.urls import path
from .import views 


urlpatterns = [
  path('', views.save_profile, name='save_profile'),
  path('<int:id>/', views.resume, name='resume'),
]