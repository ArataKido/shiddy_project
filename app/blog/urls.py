from .views import BlogAll, BlogDetail
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('', BlogAll.as_view(), name='blog'),
    path('blog/post/<int:pk>', BlogDetail.as_view(), name='blog-detail'),
]
