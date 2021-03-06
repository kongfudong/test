from django.shortcuts import render
from django.shortcuts import redirect
from  . import models
from djnago import forms
# Create your views here.


def index(request):
    pass
    return render(request,'login/index.html')


def login(request):
    if request.method == "POST":
        login_form = forms.UserForm(request.POST)
        message = "请填写检查内容"
        if login_form.is_valid：
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
        message = "所有字段必须填写！"
        if username and password:
            username = username.strip()
            try:
                user = models.User.objects.get(name=username)
                if user.password == password:
                    return redirect('/index/')
                else:
                    message = "密码不正确！"
            except:
                message = "用户名不存在！"
        return render(request,'login/login.html',{'message':message})
    return render(request, 'login/login.html')


def register(request):
    pass
    return render(request, 'login/register.html')


def logout(request):
    pass
    return redirect(request, 'index.html')
