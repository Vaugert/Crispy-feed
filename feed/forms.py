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
    