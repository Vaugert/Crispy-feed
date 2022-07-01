from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    """ Post model """
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=300)
    content = models.TextField(blank=True)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)


class Comment(models.Model):
    """ Comment model """
    post = models.ForeignKey(Post, null=True, on_delete=models.CASCADE, related_name='post_comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comments')
    content = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='comment_likes')

