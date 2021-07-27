from django.urls import path

from . import views

app_name = 'service'

urlpatterns = [
    # 서비스 소개 21.07.26
    path('service/', views.service, name='service'),
]