from django.urls import path, include
from . import views
from .models import Post

urlpatterns = [
    path('post_details/<int:pk>', views.post_details, name='post'),
    path('accounts/', include('allauth.urls')),

]