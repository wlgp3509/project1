
from django.shortcuts import render
from service.forms import AdhdForm

from service.models import Choice


from django.http import HttpResponseRedirect

#******************** 21.07.26 서비스 소개
# 21.10.05 adhd 서비스 추가
def adhd_test(request):
    return render(request, 'ADHD/adhd_test.html')
# 21.10.05 adhd 초/중고/양육자 추가
# form 처리 21.10.21

def adhd_elementary(request):
    if request.method == "POST":
        # content = request.POST.get('content')
        form = AdhdForm(request.POST)
        if form.is_valid():
            # 데이터를 모델에 저장하기 전에 작성자 정보를 추가하고 저장해야 하므로 commit=False 사용
            form.cleaned_data['choices', 'contents']
            form.save()
            return HttpResponseRedirect('service:adhd_result')
    else:
        form = AdhdForm()
    context = {'form': form}
    return render(request, 'ADHD/adhd_elementary.html', context)
  #  return render(request, 'ADHD/adhd_elementary.html')













#21.10.22 선택 결과창
def adhd_result(request):  #요청, id값 파라미터

    adhd_form = request.POST.get('adhd_form')
    context = {'adhd_form' : adhd_form }
    return render(request, 'ADHD/adhd_result.html', context)
    # return render(request, 'ADHD/adhd_result.html')


def adhd_student(request):
    return render(request, 'ADHD/adhd_student.html')
def adhd_rearer(request):
    return render(request, 'ADHD/adhd_rearer.html')
def TEST(request):
    return render(request, 'ADHD/TEST.html')




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


