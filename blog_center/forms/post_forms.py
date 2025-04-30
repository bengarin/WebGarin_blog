from django import forms
from blog_center.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image', 'category']
        widgets = {
            'content': forms.Textarea(attrs={
                'id': 'ckeditor',
                'class': 'form-control',
                'rows': 60,
                'style': 'min-height:900px;',
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control input-default',
                'placeholder': 'Titre du post',
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-file-input form-control',
            }),
            'category': forms.Select(attrs={
                'class': 'default-select form-control wide mb-3',
            }),
        }
