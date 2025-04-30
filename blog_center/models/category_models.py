from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(unique=True,max_length=255)
    slug = models.CharField(unique=True,max_length=30)
    status = models.BooleanField(default=True)
    icons = models.CharField(max_length=255,default='fas fa-th')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name}"
     
    @classmethod
    def get_status_number(cls):
        status_active = cls.objects.filter(status=True).count()
        status_inactive = cls.objects.filter(status=False).count()
        return {
            'status_active': status_active,
            'status_inactive': status_inactive
        }