from django.db import models

# Create your models here.
class Medicine(models.Model):
    
    name=models.CharField(max_length=50)
    description = models.TextField(max_length=255)
    Price=models.IntegerField(max_length=10)
    availability=models.IntegerField(max_length=10)
