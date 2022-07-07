from django.urls import path, include
from . import views
from .models import Post

urlpatterns = [
    path('post_details/<int:pk>', views.post_details, name='post_details'),
    path('account/', include('allauth.urls')),
    path('delete_post/<int:pk>', views.delete_post, name='delete_post'),
    path('edit_post/<int:pk>', views.edit_post, name='edit_post'),
    path('create_post', views.create_post, name='create_post'),

]