from django.db import models
from blog_center.models.posts_models import Post
from django.contrib.auth.models import User
class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    name = models.OneToOneField(User,on_delete=models.SET_NULL,null=True,blank=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.post} - {self.created_at}"
    
    
    