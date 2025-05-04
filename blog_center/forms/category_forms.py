from django import forms
from blog_center.models import Category

class CategoryForm(forms.ModelForm):    
    class Meta:
        model = Category
        fields = ['name', 'slug', 'status', 'icons']
        
    