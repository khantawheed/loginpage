from django.db import models
from django.contrib.auth.models import User 
# Create your models here.
class Destination(models.Model):
    email = models.EmailField(max_length=200)
    username = models.CharField(max_length=100)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
   