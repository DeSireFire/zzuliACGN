from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponseRedirect,JsonResponse
from hashlib import sha256
from django.core.paginator import Paginator,Page
from . import loginCheck
import re
# from django.views.decorators.csrf import csrf_exempt

from django.utils.html import escape
# XSS防御组件

# todo :用户注册尚未加入敏感词过滤，由于user视图变量过多或考虑参数分离。
# Create your views here.

# 用户注册跳转
def register(request):
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

    if register_RE(keyName,keyValue):
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
def register_RE(keyName,keyValue):
    ResDict = {
        "ZA_User_Name":r"^([\w]|[\u4e00-\u9fa5]|[ 。，、？￥“”‘’！：【】《》（）——.,?!$'\":+-]){4,16}$",
        "ZA_User_Email":r"^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$",
        "ZA_User_Phone":r"^1[34578]\d{9}$",
    }
    pattern = re.compile(ResDict.get(keyName))
    retemp = pattern.match(keyValue)
    # print(retemp.group())
    if retemp:
        return True
    else:
        return False


 # 用户注册处理
def register_handle(request):


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
        Encipherment = sha256()
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


# 用户登录跳转
def login(request):

    context = {'warning': ''}
    return  render(request,'ZA_User/Login.html',context)

# 用户登录处理

# @csrf_exempt # 该视图无视跨域请求保护，有风险
def login_handler(request):

    # {'password': ['123qwe'], 'user_name': ['1025212779@qq.com'], 'rememberme': ['on'],
    #  'csrfmiddlewaretoken': ['O8nwHR9211S1Xw0jbWLtsr4YHu2kq7V4RpRPUwnGxkSZZgM1uj7yU57bC1ILjxrM']}
    print(request.POST)

    New_ZA_User_Temp = request.POST.get('user_name')

    # 判断使用邮箱登录还是用户名登录
    if register_RE("ZA_User_Email", New_ZA_User_Temp):
        New_ZA_User_Email = New_ZA_User_Temp
        old_users = ZA_UserInfo.objects.filter(ZA_User_Email=New_ZA_User_Email)  # 从后端获取用户名

    elif register_RE("ZA_User_Name", New_ZA_User_Temp):
        New_ZA_User_name = New_ZA_User_Temp
        old_users = ZA_UserInfo.objects.filter(ZA_User_Name=New_ZA_User_name)  # 从后端获取邮箱
    else:
        context = {'warning': '用户名或者密码错误啦！'}
        return render(request, 'ZA_User/Login.html', context)

    # 用户密码
    New_ZA_User_pwd = request.POST.get('password')


    # 登录状态记忆
    RememberMe = "off"
    if 'rememberme' in request.POST and request.POST['rememberme']:  # 获得用户输入值
        RememberMe = request.POST.get('rememberme')
        print("是否记住登陆状态：%s"%RememberMe)

    # print("Tmp:%s" % New_ZA_User_Temp)
    # print("pwd:%s" % New_ZA_User_pwd)
    # print("old_users:%s" % old_users[0])
    # print("old_users:%s" % old_users[0].ZA_User_ID)
    # print("old_users:%s" % old_users[0].ZA_User_Name)
    # print("old_users:%s" % old_users[0].ZA_User_Email)
    # print("CK_URL:%s" % request.COOKIES)
    # print("CK_URL:%s" % request.COOKIES.get("url"))

    login_json = {
        "login":"no", # 是否登录成功
        "url":"", # 删除转向地址，防止以后直接登录造成的转向
        "zzuliacgn_user_name":None, # 用户名信息
        "zzuliacgn_u":None, # 用户名信息

        # max_age:-1表示为cookies的max-age的默认值是-1(即max-age和expires的有效期为session)
        "max_age":-1, # 是否使用cookies的max-age,设置cookies还剩多少秒苟活，
        # expires为0表示为cookies的expires的默认值是为session,否则留存天数，单位（天）(即max-age和expires的有效期为session)
        "Expires":0, # 是否使用cookies的expires,设置cookies过期时间点,预留
    }
    if len(old_users) == 1:
        # 获取到用户名
        # 验证密码
        # 我就是要把变量名写得让你看起来头皮发麻！2333
        encipherment = sha256()
        encipherment.update(New_ZA_User_pwd.encode('utf-8'))
        ZA_User_Password_encipherment = encipherment.hexdigest()
        if ZA_User_Password_encipherment==old_users[0].ZA_User_Password:
            print("%s 登录成功！"%old_users[0].ZA_User_Name)
            login_json["login"] = "ok"
            # 记住用户名
            if RememberMe == "on" or RememberMe == "true":
                print("保持登录状态与默认sessions寿命一致!")
                # 用户名以utf8编码以保证cookies不报错，使用时用.decode("utf-8")解码
                login_json["zzuliacgn_user_name"] = old_users[0].ZA_User_Name.encode('utf-8').decode()
            else:
                print("未勾选登录状态记忆！关闭浏览器遍结束会话")
                login_json["zzuliacgn_user_name"] = ''


                # 用户关闭浏览器session就会失效
                request.session.set_expiry(0)
                # 你可以传递四种不同的值给它：
                # *如果value是个整数，session会在些秒数后失效。
                # *如果value是个datatime或timedelta，session就会在这个时间后失效。
                # *如果value是0, 用户关闭浏览器session就会失效。
                # *如果value是None, session会依赖全局session失效策略。

            # 登录成功保存session信息
            request.session['user_id']=old_users[0].ZA_User_ID
            request.session['zzuliacgn_user_name'] = old_users[0].ZA_User_Name
            print("session信息保存成功！")
            print("session——user_id:%s"%request.session['user_id'])
            print("session——user_name:%s"%request.session['zzuliacgn_user_name'])
            print("session——id:%s"%request.session.session_key)
            print("session——keys:%s"%request.session.keys())
            print("session——values:%s"%request.session.values())
            return JsonResponse(login_json)
        else:
            # 密码验证失败，返回json给js
            print("登陆失败！密码错误")
            return JsonResponse(login_json)
    else:
        # 密码验证失败，返回json给js
        print("登陆失败！用户名不存在")
        return JsonResponse(login_json)

@loginCheck.logining
def login_out(request):
    '''
    注销登录，并删除session
    '''

    request.session.flush()
    return redirect('/')

@loginCheck.logining
def info(request):
    '''
        用户个人中心
        从session获取user_info的id
    '''
    user_info = ZA_UserInfo.objects.get(ZA_User_ID=request.session['user_id'])
    context={
        # 'title':'用户中心',
        # 'user':user_info,
        # 'page_name': 1
    }
    return render(request,'ZA_User/usercenter.html',context)

@loginCheck.logining
def head_Update(request):
    '''
        用于处理用户头像
    :param request: request实例
    :return:
    '''
    print(request.POST)
    if 'user_name' in request.POST and request.POST['user_name']:  # 获得用户输入值
        q = request.GET.get('user_name')
        print(q)