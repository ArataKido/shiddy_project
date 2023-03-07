from .views import *
from django.urls import path

app_name = 'index'

urlpatterns = [
    path('', Index.as_view(), name='index'),
]
