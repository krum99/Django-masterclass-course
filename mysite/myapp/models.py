from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from .managers import ItemManager

class Item(models.Model):
  
  class Meta:
    indexes = [
      models.Index(fields=['user_name', 'item_price']),
    ]

  def __str__(self):
    return self.item_name + ": " + str(self.item_price)
  
  def get_absolute_url(self):
    return reverse('myapp:index')

  user_name = models.ForeignKey(User, on_delete=models.CASCADE)
  item_name = models.CharField(max_length=200, db_index=True)
  item_desc = models.CharField()
  item_price = models.DecimalField(max_digits=4, decimal_places=2, db_index=True)
  item_image = models.URLField(max_length=500, default='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRHCva-afP1vczYjMkGUFt4QQ51zwKM2q3GcQ&s')
  is_available = models.BooleanField(default=True)
  created_at = models.DateTimeField(auto_now_add=True)

  is_deleted = models.BooleanField(default=False) # soft delete  flag

  deleted_at = models.DateTimeField(null=True, blank=True)

  objects = ItemManager()

class Category(models.Model):
  name = models.CharField(max_length=100)
  added_on = models.DateField(auto_now=True)

  def __str__(self):
    return self.name