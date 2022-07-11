from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    summernote_fields = ('content')
    list_filter = ('title', 'created_date', 'updated_date', )
    list_display = ('author', 'title', 'created_date' )
    search_fields = ('title', 'created_date')
    


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created_date', 'content')


