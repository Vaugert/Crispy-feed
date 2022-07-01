from django.shortcuts import render
from .models import Post


def home_screen(request):
    """Home Screen View"""
    posts = Post.objects.all()
    context = {
        'posts': posts
        }
    return render(request, 'index.html', context)