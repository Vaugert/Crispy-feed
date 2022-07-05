from django.urls import path
from . import views
from .models import Post

urlpatterns = [
    path('post_details/<pk>', views.post_details, name='post_details'),

]