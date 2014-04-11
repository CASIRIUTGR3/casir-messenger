from django.db import models
from test.test_imageop import MAX_LEN

# Create your models here.
class user(models.Model):
    nom = models.CharField(max_length = 50)
    prenom = models.CharField(max_length = 50)
    email = models.EmailField
    password = models.CharField(max_length = 20)
    
