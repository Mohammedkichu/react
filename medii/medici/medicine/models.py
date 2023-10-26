from django.db import models

# Create your models here.
class Medicine(models.Model):
    
    mname=models.CharField(max_length=50)
    description = models.TextField(max_length=255, blank=True)
    Price=models.CharField(max_length=10)
    expiry_date=models.DateField(null=True, blank=True)
    side_effect=models.TextField(max_length=50)

    
