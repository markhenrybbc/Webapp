from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('videos/', views.video_list, name='video_list'),
  path('video/<int:pk>/', views.video_detail, name='video_detail'),
  path('signup/', views.signup, name='signup'),
]