from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponseRedirect,JsonResponse
from hashlib import sha1
from django.core.paginator import Paginator,Page
from datetime import datetime

# Create your views here.
def Test(request):
    return render(request,'ZA_users/test.html')

def Testindex(request):
    return render(request,'ZA_index/Base.html')

# 用户注册跳转
def Register(request):

    context = {'title': '用户注册'}
    return  render(request,'ZA_users/RegEmail.html',context)


def register_skip(request):
    '''
        获取用户名
        验证用户名是否重复,
        返回json格式的数据(JsonResponse)
        {根据名字查到的用户对象的num_id}
        模板中接口为count
    '''
    uname = request.GET.get('user_name')
    print(request.GET)
    print(uname)
    # num_id = ZA_UserInfo.objects.filter(uname = uname).count()
    # return JsonResponse({'count':2})
    return JsonResponse({'Judgement':'false'})

# 用户注册：电子邮箱
def Register_handle(request):

    if 'user_name' in request.GET and request.GET['user_name']:  # 获得用户输入值
        q = request.GET.get('user_name')
        print(q)

    New_ZA_User_Email = request.POST.get('Email')
    #电子邮箱
    New_ZA_User_name = request.POST.get('user_name')
    #用户昵称
    New_ZA_User_Phone = request.POST.get('user_Phone')
    #用户电话
    New_ZA_User_pwd = request.POST.get('pwd')
    #用户密码1
    New_ZA_User_pwd_again = request.POST.get('pwdagain')
    # 用户密码2
    New_ZA_User_RegTime = datetime.now().strftime('%b-%d-%Y %H:%M:%S')
    # 用户注册时间


    #后端再次确认密码是否一致
    if New_ZA_User_pwd != New_ZA_User_pwd_again and New_ZA_User_pwd != None and New_ZA_User_pwd_again != None:
        return redirect('/user/Register')
    else:
        #加密
        Encipherment = sha1()
        print(New_ZA_User_pwd)
        print(type(New_ZA_User_pwd))
        Encipherment.update(New_ZA_User_pwd.encode('utf-8'))
        Up_Password_Encipherment = Encipherment.hexdigest()

        #创建新的用户对象
        NewUser = ZA_UserInfo()
        NewUser.ZA_User_RegTime = New_ZA_User_RegTime
        NewUser.ZA_User_Email = New_ZA_User_Email
        NewUser.ZA_User_Name = New_ZA_User_name
        NewUser.ZA_User_Phone = New_ZA_User_Phone
        NewUser.ZA_User_Password = Up_Password_Encipherment

        print(New_ZA_User_RegTime)
        print(New_ZA_User_Email)
        print(New_ZA_User_name)
        print(New_ZA_User_Phone)
        print(Up_Password_Encipherment)

        print(NewUser)
        return  redirect('/user/login/')