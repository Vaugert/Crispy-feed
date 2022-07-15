from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.core.paginator import Paginator
from .models import Post, Comment
from .forms import CommentForm, PostForm


def home_screen(request):
    """Home Screen View"""
    posts = Post.objects.all()
    paginateby = Paginator(posts, 6)
    context = {
        'posts': posts

        }
    return render(request, 'index.html', context)


def post_details(request, pk):

    post = get_object_or_404(Post, pk=pk)
    comments = post.post_comments.all()
    form = CommentForm(request.POST)
    author = request.user
    if request.method == 'POST':
        if form.is_valid():
            form.instance.author = author
            form.instance.post = post
            form.save()
            return redirect('post_details', post.pk)
    
    print(comments)

    context = {
        'post': post,
        'author': author,
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
        form = PostForm(instance=post)
        author = request.user
        if request.method == 'POST':
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                form.instance.author = author
                form.instance.post = post
                form.save()
            return redirect('post_details', post.pk)

    context = {
        'form': form
    }

    return render(request, 'posts/edit_post.html', context)
    

    








