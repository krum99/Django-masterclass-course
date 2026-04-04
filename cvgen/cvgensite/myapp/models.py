from django.db import models

# Create your models here.


class Profile(models.Model):
  name = models.CharField(max_length=60)
  email = models.CharField(max_length=100)
  phone = models.CharField(max_length=20)
  degree = models.CharField(max_length=100)
  school = models.CharField(max_length=50)
  university = models.CharField(max_length=100)
  summary = models.TextField(max_length=1000)
  previous_work = models.TextField(max_length=500)
  skills = models.CharField(max_length=200)