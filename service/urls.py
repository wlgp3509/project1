from django.urls import path
from . import views

app_name = 'service'

urlpatterns = [
    # 서비스 소개 21.07.26

    path('adhd_test/', views.adhd_test, name='adhd_test'),
    path('mulpsy_test/', views.mulpsy_test, name='mulpsy_test'),
    path('artpsy_test/', views.artpsy_test, name='artpsy_test'),
    # adhd 테스트 추가-최졔 21.10.05
    path('adhd_elementary/', views.adhd_elementary, name='adhd_elementary'),
    path('adhd_student/', views.adhd_student, name='adhd_student'),
    path('adhd_rearer/', views.adhd_rearer, name='adhd_rearer'),

]