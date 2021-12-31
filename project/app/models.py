from django.db import models
from django.contrib.auth.models import User

class Aphorism(models.Model):
  aphorism_text = models.CharField(max_length=100)

class UserInfo(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  address = models.CharField(max_length=100)
  sec_number = models.CharField(max_length=100)