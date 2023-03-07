from .views import BlogAll, BlogDetail, BlogCategory
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('', BlogAll.as_view(), name='blog'),
    path('blog/post/<str:slug>', BlogDetail.as_view(), name='blog-detail'),
    path('category/<int:pk>', BlogCategory.as_view(), name='blog-category'),
]
