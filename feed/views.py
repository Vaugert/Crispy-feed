from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment


def home_screen(request):
    """Home Screen View"""
    posts = Post.objects.all()
    context = {
        'posts': posts
        }
    return render(request, 'index.html', context)



def post_details(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post=post) 


def post_comment(request):
    
    if request.method == 'POST':

        name = request..get('author')

        return redirect ('home_screen')
    return render(request, 'templates/post_details.html' )

