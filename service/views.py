
from django.shortcuts import render

#********************************************************************
# 21.07.26 서비스 소개
def adhd_test(request):
    return render(request, 'adhd_test.html')

def mulpsy_test(request):
    return render(request, 'mulpsy_test.html')

def artpsy_test(request):
    return render(request, 'artpsy_test.html')

