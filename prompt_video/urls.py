from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('handle_video_edit/', views.handle_video_edit, name='handle_video_edit'),
    path('generate-audio/', views.generate_audio, name='generate_audio'),

]
