
from django.shortcuts import render

#******************** 21.07.26 서비스 소개
def adhd_test(request):
    return render(request, 'ADHD/adhd_test.html')

# 21.10.05 adhd 1,2,3 세부 검사 페이지 추가
def adhd_elementary(request):
    return render(request, 'ADHD/adhd_elementary.html')
def adhd_student(request):
    return render(request, 'ADHD/adhd_student.html')
def adhd_rearer(request):
    return render(request, 'ADHD/adhd_rearer.html')


def mulpsy_test(request):
    return render(request, 'mulpsy_test.html')

def artpsy_test(request):
    return render(request, 'artpsy_test.html')

