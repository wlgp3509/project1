from django.shortcuts import render, redirect
from common.forms import UserForm
from django.contrib.auth import authenticate, login

# Create your views here.
def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            # 회원가입 후 바로 로그인 되게 하는 기능
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return render(request, 'index.html')

    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})