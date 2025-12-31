from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Item(models.Model):
  def __str__(self):
    return self.item_name
  
  def get_absolute_url(self):
    return reverse('myapp:index')

  user_name = models.ForeignKey(User, on_delete=models.CASCADE)
  item_name = models.CharField(max_length=200)
  item_desc = models.CharField()
  item_price = models.IntegerField()
  item_image = models.CharField(max_length=500, default='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRHCva-afP1vczYjMkGUFt4QQ51zwKM2q3GcQ&s')


class Category(models.Model):
  name = models.CharField(max_length=100)
  added_on = models.DateField(auto_now=True)

  def __str__(self):
    return self.name