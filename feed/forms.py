from django import forms
from .models import Post, Comment

class CommentForm(forms.ModelForm):
    class Meta:
        fields = ('content',)
        labels = {
            'content': ('Leave a comment!')
        } 
        model = Comment
        widgets = {'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3})}
    

class PostForm(forms.ModelForm):
    """Create A Post"""
    class Meta:
        """Meta Class"""
        model = Post
        fields = ('title', 'content')

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'optional'})
        }