from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from .forms import CommentForm, PostForm


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
    form = CommentForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()

    context = {
        'post': post,
        'comments': comments,
        'form': form
    }

    return render(request, 'posts/post_details.html', context)


def delete_post(request, pk):
    """Delete Post"""
    post = get_object_or_404(Post, pk=pk)
    if request.user == post.author:
        post.delete()

    return redirect('home')


def create_post(request):
    form = PostForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')

    context = {
        'form': form
    }

    return render(request, 'posts/create_post.html', context)


def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user == post.author:
      if request.method == 'POST':
        form = PostForm(request.POST, instance=post)

    








