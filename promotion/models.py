from django.db import models

# Create your models here.
class user(models.Model):
    nom = models.CharField(max_length = 50)
    prenom = models.CharField(max_length = 50)
