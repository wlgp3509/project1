from django.urls import path
from . import views

app_name = 'service'

urlpatterns = [
    # 서비스 소개 21.07.26
    path('adhd_test/', views.adhd_test, name='adhd_test'),
    path('mulpsy_test/', views.mulpsy_test, name='mulpsy_test'),
    path('artpsy_test/', views.artpsy_test, name='artpsy_test'),
]