from .views import *
from django.urls import path

app_name = 'social'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('create/', create, name='create'),
]
