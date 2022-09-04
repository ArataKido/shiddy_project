from .views import *
from django.urls import path

app_name = 'index'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('create/', create, name='create'),
    path('portfolio/id/<int:pk>', PortfolioDetail.as_view(), name='portfolio_detail'),
    path('blog/all', Blog.as_view(), name='blog'),
    path('blog/post/<int:pk>', BlogDetail.as_view(), name='blog-detail'),
]
