from .views import *
from django.urls import path

app_name = 'case'

urlpatterns = [
    path('', Cases.as_view(), name='index'),
    path('case/id/<int:pk>', CaseDetail.as_view(), name='detail')
]
