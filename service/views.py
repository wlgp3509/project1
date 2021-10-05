
from django.shortcuts import render

#******************** 21.07.26 서비스 소개
def adhd_test(request):
    return render(request, 'adhd_test.html')

# 21.10.05 adhd 1,2,3 세부 검사 페이지 추가
def adhd1(request):
    return render(request, 'adhd1.html')
def adhd2(request):
    return render(request, 'adhd2.html')
def adhd3(request):
    return render(request, 'adhd3.html')


def mulpsy_test(request):
    return render(request, 'mulpsy_test.html')

def artpsy_test(request):
    return render(request, 'artpsy_test.html')

