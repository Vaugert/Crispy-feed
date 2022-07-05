from django.urls import path
from . import views

urlpatterns = [
    path('post_details', views.post_details, name='post_details'),

]