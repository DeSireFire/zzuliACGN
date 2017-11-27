from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponseRedirect,JsonResponse
from hashlib import sha1
from django.core.paginator import Paginator,Page

# Create your views here.
def Test(request):
    return render(request,'ZA_users/test.html')

# 用户注册跳转
def Register(request):

    context = {'title': '用户注册'}
    return  render(request,'ZA_users/RegEmail.html',context)
    pass

# 用户注册：电子邮箱
def Register_handle_Email(request):
    New_ZA_User_Email = request.POST.get('Email')
    New_ZA_User_name = request.POST.get('user_name')
    New_ZA_User_pwd = request.POST.get('pwd')
    New_ZA_User_pwd_again = request.POST.get('pwdagain')

    #
    if New_ZA_User_pwd != New_ZA_User_pwd_again:
        return redirect('/user/Register')
    pass

# 用户注册：手机电话
def Register_handle_Phone(request):
    # New_ZA_User_Phone =
    pass