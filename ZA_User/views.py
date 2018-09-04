from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponseRedirect,JsonResponse
from hashlib import sha1
from django.core.paginator import Paginator,Page
from datetime import datetime
import re

# Create your views here.

# 用户注册跳转
def Register(request):
    context = {'title': '用户注册'}
    return render(request,'ZA_User/register.html',context)

def register_ajax(request):
    '''
        获取用户名
        验证用户名是否重复,
        返回json格式的数据(JsonResponse)
        {根据名字查到的用户对象的user_name}
        模板中接口为count
    '''
    ajaxdict = {"ZA_User_Name":request.GET.get('user_name'),"ZA_User_Email":request.GET.get('user_email'),"ZA_User_Phone":request.GET.get('user_phone'),}
    # user_name = request.GET.get('user_name')
    # user_email = request.GET.get('user_email')
    # user_phone = request.GET.get('user_phone')
    keyName = ''
    keyValue = ''
    theNum = {"count":1}

    # 分类ajax参数
    for key in ajaxdict:
        if ajaxdict.get(key,0) != None:
            keyName = key
            keyValue = ajaxdict[key]

    if Register_Re(keyName,keyValue):
        if keyName == 'ZA_User_Name':
            theNum["count"] = ZA_UserInfo.objects.filter(ZA_User_Name=keyValue).count()
        elif keyName == 'ZA_User_Email':
            theNum["count"] = ZA_UserInfo.objects.filter(ZA_User_Email=keyValue).count()
        elif keyName == "ZA_User_Phone":
            theNum["count"] = ZA_UserInfo.objects.filter(ZA_User_Phone=keyValue).count()
    else:
        context = {'title': '用户注册'}
        return render(request, 'ZA_User/register.html', context)

    print(theNum)
    return JsonResponse(theNum)


# 后端正则验证
def Register_Re(keyName,keyValue):
    ResDict = {
        "ZA_User_Name":r"^([\w]|[\u4e00-\u9fa5]|[ 。，、？￥“”‘’！：【】《》（）——.,?!$'\":+-]){4,16}$",
        "ZA_User_Email":r"^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$",
        "ZA_User_Phone":r"^1[34578]\d{9}$",
    }
    pattern = re.compile(ResDict.get(keyName))
    retemp = pattern.match(keyValue)
    print(retemp.group())
    if retemp:
        return True
    else:
        return False


 # 用户注册
def Register_handle(request):

    print(request.POST)
    if 'user_name' in request.GET and request.GET['user_name']:  # 获得用户输入值
        q = request.GET.get('user_name')
        print(q)
    # < QueryDict: {'csrfmiddlewaretoken': ['NRKioLR9Nz0wPXLK2HGnaZgvY53ihDJmQ8eBBq5NjS0uRHxsl42sCDjITCJJa3f4'],
    #               'pwdConfirm': ['RQganyongqi233?'], 'Email': ['1025212779@qq.com'], 'user_name': ['wocao'],
    #               'phone': [''], 'password': ['RQganyongqi233?']} >

    New_ZA_User_Email = request.POST.get('Email')
    #电子邮箱
    New_ZA_User_name = request.POST.get('user_name')
    #用户昵称
    New_ZA_User_Phone = request.POST.get('phone')
    #用户电话
    New_ZA_User_pwd = request.POST.get('password')
    #用户密码1
    New_ZA_User_pwd_again = request.POST.get('pwdConfirm')
    # 用户密码2
    # New_ZA_User_RegTime = datetime.now().strftime('%b-%d-%Y %H:%M:%S')
    # 用户注册时间

    # 后端再次确认密码是否一致
    if New_ZA_User_pwd != New_ZA_User_pwd_again and New_ZA_User_pwd != None and New_ZA_User_pwd_again != None:
        return redirect('/user/register/')
    else:
        #加密
        Encipherment = sha1()
        Encipherment.update(New_ZA_User_pwd.encode('utf-8'))
        Up_Password_Encipherment = Encipherment.hexdigest()

        #创建新的用户对象
        NewUser = ZA_UserInfo()
        # NewUser.ZA_User_RegTime = New_ZA_User_RegTime
        NewUser.ZA_User_Email = New_ZA_User_Email
        NewUser.ZA_User_Name = New_ZA_User_name
        NewUser.ZA_User_Phone = New_ZA_User_Phone
        NewUser.ZA_User_Password = Up_Password_Encipherment

        # print(New_ZA_User_RegTime)
        print(New_ZA_User_Email)
        print(New_ZA_User_name)
        print(New_ZA_User_Phone)
        print(Up_Password_Encipherment)
        print(NewUser)
        NewUser.save()
    return redirect('/user/login/')

# 用户登录页面
def Login(request):

    context = {'title': '用户登录'}
    return  render(request,'ZA_User/Login.html',context)

def Login_Handler(request):

    if 'Email' in request.GET and request.GET['Email']:  # 获得用户输入值
        New_ZA_User_Email = request.POST.get('Email')
        #电子邮箱
        New_ZA_User_pwd = request.POST.get('pwd')
        #用户密码
    context = {'title': '用户成功！'}
    return  render(request,'ZA_User/Login.html',context)