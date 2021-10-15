from django.urls import path
from . import views

app_name = 'service'

urlpatterns = [
    # 서비스 소개 21.07.26
    # 우울증, 다중지능 테스트 추가- 최졔 21.10.12
    path('adhd_test/', views.adhd_test, name='adhd_test'),
    path('multiiq_test/', views.multiiq_test, name='multiiq_test'),
    path('depression_test/', views.depression_test, name='depression_test'),
    # adhd 초/중등/양육자 추가_최졔 21.10.05
    path('adhd_elementary/', views.adhd_elementary, name='adhd_elementary'),
    path('adhd_student/', views.adhd_student, name='adhd_student'),
    path('adhd_rearer/', views.adhd_rearer, name='adhd_rearer'),
    path('TEST/', views.TEST, name='TEST'),

    # 우울증 청소년/양육자 추가_최졔 21.10.12
    path('dep_adolescent/', views.dep_adolescent, name='dep_adolescent'),
    path('dep_rearer/', views.dep_rearer, name='dep_rearer'),

    # 다중지능 청소년/양육자 추가_최졔 21.10.12
    path('mul_adolescent/', views.mul_adolescent, name='mul_adolescent'),
    path('mul_rearer/', views.mul_rearer, name='mul_rearer'),

]