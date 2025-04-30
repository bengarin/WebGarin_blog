from django.db import models

# Create your models here.
class Ctaegory(models.Model):
    name = models.CharField(unique=True,max_length=255)
    slug = models.CharField(unique=True,max_length=30)
    
    def __str__(self):
        return f"{self.name}"