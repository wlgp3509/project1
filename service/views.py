
from django.shortcuts import render

#********************************************************************
# 21.07.26 서비스 소개
def service(request):
    return render(request, 'service.html')

