from django.urls import path
from .views import index, check_file

urlpatterns = [
    path('', index, name='index'),
    path('check_file/', check_file, name='check_file'),
]
