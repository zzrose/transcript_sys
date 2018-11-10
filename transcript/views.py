from django.shortcuts import render
from django.contrib.auth import authenticate,login   # 验证
from  django.contrib.auth.backends import ModelBackend
from django.http import HttpResponse
from django.db.models import Q
from .models import Course, UserProfile
from django.contrib.auth.hashers import make_password
from django.views.generic.base import View
from datetime import datetime
from .forms import LoginForm
# Create your views here.


# def index(request):
#     cou_list = Course.objects.all().order_by('id')[:10]
#     response = HttpResponse()
#     heading1 = '<p>' + 'List of courses: ' + '</p>'
#     response.write(heading1)
#     for course in cou_list:
#         para = '<p>'+ str(course.id) + ': ' + str(course) + '</p>'
#         response.write(para)
#     return response


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html', {})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get('username', '')
            pass_word = request.POST.get('password', '')
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'index.html')
                else:
                    return render(request, 'login.html', {'msg':'用户未激活'})
            else:
                return render(request, 'login.html', {'msg': '用户名或密码错误!'})

        else:
            return render(request, 'login.html', {'login_form': login_form})


class UserinfoView(View):
    def get(self, requset):
        return render(requset, 'usercenter-info.html', {})
