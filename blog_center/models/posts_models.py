from django.db import models
from django.contrib.auth.models import User
from blog_center.models.category_models import Category

class Post(models.Model):
    title = models.CharField(max_length=255)
    meta_title = models.CharField(max_length=255 ,default="")
    meta_description = models.TextField(default="")
    slug = models.CharField(max_length=255,unique=True ,default="")
    image = models.FileField(upload_to="pots/%Y/%m/%d",null=True,blank=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=True)
    number_views = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        
        return f'{self.title} - ({self.pk})'
    