from django.db import models

# Create your models here.
class Seed(models.Model):
  # fake_data = models.TextField()
  name=models.TextField()
  age=models.TextField()
 