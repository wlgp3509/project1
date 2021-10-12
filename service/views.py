
from django.shortcuts import render

#******************** 21.07.26 서비스 소개
# 21.10.05 adhd 서비스 추가
def adhd_test(request):
    return render(request, 'ADHD/adhd_test.html')
# 21.10.05 adhd 초/중고/양육자 추가
def adhd_elementary(request):
    return render(request, 'ADHD/adhd_elementary.html')
def adhd_student(request):
    return render(request, 'ADHD/adhd_student.html')
def adhd_rearer(request):
    return render(request, 'ADHD/adhd_rearer.html')

# 21.10.12 우울증 (청소년, 양육자) 서비스 추가
def depression_test(request):
    return render(request, 'Depression/depression_test.html')
def dep_adolescent(request):
    return render(request, 'Depression/dep_adolescent.html')
def dep_rearer(request):
    return render(request, 'Depression/dep_rearer.html')

# 21.10.12 다중지능 (청소년, 양육자) 서비스 추가
def multiiq_test(request):
    return render(request, 'Multi_Iq/multiiq_test.html')

def mul_adolescent(request):
    return render(request, 'Multi_Iq/mul_adolescent.html')
def mul_rearer(request):
    return render(request, 'Multi_Iq/mul_rearer.html')


