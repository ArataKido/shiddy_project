from .views import *
from django.urls import path

app_name = 'portfolio'

urlpatterns = [
    path('', Portfolio.as_view(), name='index'),
    path('portfolio/id/<int:pk>', PortfolioDetail.as_view(), name='portfolio_detail'),
]