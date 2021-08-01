from django.urls import path
from . import views

app_name = 'app1'

urlpatterns =[
    path('', views.question_list, name='index'),

    # ---- 게시판(질문 리스트) 21.07.26(최졔)
    path('question/list/', views.question_list, name='question_list'),

    # --------- 상세보기 페이지 추가 21.07.12(최졔)
    path('<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),

    # ---------- 질문등록 url 생성 21.07.13(최졔)
    path('question/create/', views.question_create, name='question_create'),

    # ---------- 질문 수정 url 등록 21.07.21
    path('question/modify/<int:question_id>/', views.question_modify, name='question_modify'),

    # --------- 질문 삭제 url 등록 21.07.22
    path('question/delete/<int:question_id>/', views.question_delete, name='question_delete'),

    # --------- 답변 수정 url 등록 21.07.23
    path('answer/modify/<int:answer_id>/', views.answer_modify, name='answer_modify'),

    # --------- 답변 삭제 url 등록 21.07.22
    path('answer/delete/<int:answer_id>/', views.answer_delete, name='answer_delete'),



]


