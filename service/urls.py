from django.urls import path
from . import views

app_name = 'service'

urlpatterns = [
    # 서비스 소개 21.07.26
    path('adhd_test/', views.adhd_test, name='adhd_test'),
    path('mulpsy_test/', views.mulpsy_test, name='mulpsy_test'),
    path('artpsy_test/', views.artpsy_test, name='artpsy_test'),
    # adhd 테스트 추가-최졔 21.10.05
    path('adhd_test/adhd1/', views.adhd1, name='adhd1'),
    path('adhd_test/adhd2/', views.adhd2, name='adhd2'),
    path('adhd_test/adhd3/', views.adhd3, name='adhd3'),

]