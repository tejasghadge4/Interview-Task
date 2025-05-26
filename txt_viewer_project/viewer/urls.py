from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('check_file/', views.check_file, name='check_file'),
]
