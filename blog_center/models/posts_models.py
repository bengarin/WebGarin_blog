from django.db import models
from django.contrib.auth.models import User
from blog_center.models.category_models import Ctaegory

class Post(models.Model):
    title = models.CharField(max_length=255)
    image = models.FileField(upload_to="pots/%Y/%m/%d",null=True,blank=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(Ctaegory,on_delete=models.SET_NULL,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        
        return f'{self.title} - ({self.pk})'
    