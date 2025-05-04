from django import forms
from blog_center.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image', 'category', 'meta_title', 'meta_description', 'slug']
        