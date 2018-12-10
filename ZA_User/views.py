from django.shortcuts import render,redirect
from .models import *
# from django.http import HttpResponseRedirect,JsonResponse
from django.http import HttpResponse,JsonResponse
from hashlib import sha256
# from django.core.paginator import Paginator,Page
from . import loginCheck
import re,base64,json
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
    return render(request,'ZA_User/Login.html',context)

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
            request = UpdataHeaderURL(request,old_users[0].UserHeaderImg())
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

def UpdataHeaderURL(request,imgdata):
    '''
    更新session中HeaderURL字段中的值来达到头像图片同步的目的
    :param imgdata:字符串，直接从数据库获取字段内容
    :return:
    '''
    agent = request.META.get('HTTP_USER_AGENT', None)
    if 'default.jpg' not in imgdata:
        UserHeaderImg = json.loads(imgdata)
        print(UserHeaderImg)
        if UserHeaderImg['aurl'] and 'Chrome' in agent:
            request.session['HeaderURL'] = 'http://t1.aixinxi.net/{}-w.jpg'.format(UserHeaderImg['aurl'])
        elif UserHeaderImg['surl'] and 'Chrome' not in agent:
            request.session['HeaderURL'] = UserHeaderImg['surl']
        else:
            request.session['HeaderURL'] = '/static/ZA_User/img/HeaderImg/head.jpg'
    return request

@loginCheck.logining
def login_out(request):
    '''
    注销登录，并删除session
    '''

    request.session.flush()
    return redirect('/')

@loginCheck.logining
def userCenter(request):
    '''
        用户个人中心
        从session获取user_info的id
    '''
    # from django.http import HttpResponse
    context={
        'title':'用户中心',
    }
    return render(request,'ZA_User/usercenter.html',context)

@loginCheck.logining
def loadingBlacklist(request):
    '''
        用户个人中心黑名单
    '''
    blackList_json = {
        'data':{
            # "total": 18,
            # "size": 10,
            # "pages": 0,
            # "current": 1,
            'current': 0,# 当前页面
            'pages': 0,# 总页数
            'size': 0,# 每页所含条目
            'total': 0,# 总条目数
            "records": [
                # {"uid": 100, "head": "/static/ZA_User/img/HeaderImg/head.jpg", "userName": "来自后端的响应","time": "2018-06-30 02:44:21"},
            ]
        },
    }
    blacklist = list(ZA_UserInfo.objects.get(ZA_User_ID=request.session['user_id']).ZA_User_Blist)
    if blacklist:

        blackList_json = {
            'data':{
                'current': 1,# 当前页面
                'pages': 1+len(blacklist)//10,# 总页数
                'size': 10,# 每页所含条目
                'total': len(blacklist),# 总条目数
                "records": blacklist
            },
        }
    return JsonResponse(blackList_json)

@loginCheck.logining
def downloadperson(request):
    '''
        用户中心首页信息
        (尚未加入头像地址失效的检测)
    '''
    user_info = ZA_UserInfo.objects.get(ZA_User_ID=request.session['user_id'])
    f1 = lambda x:1 if x else 0
    f2 = lambda x:1 if x!='Unknow' else 0 # 实名认证函数
    f3 = lambda x:1 if json.loads(x)!={} else 0 # 密保函数
    agent = request.META.get('HTTP_USER_AGENT',None)
    if 'default.jpg' in user_info.UserHeaderImg():
        imgurl = user_info.UserHeaderImg()
    else:
        UserHeaderImg = json.loads(user_info.UserHeaderImg())
        print(UserHeaderImg)
        if UserHeaderImg['aurl'] and 'Chrome' in agent :
            imgurl = 'http://t1.aixinxi.net/{}-w.jpg'.format(UserHeaderImg['aurl'])
        elif UserHeaderImg['surl'] and 'Chrome' not in agent:
            imgurl = UserHeaderImg['surl']
        else:
            imgurl = '/static/ZA_User/img/HeaderImg/head.jpg'
    userdata={
            'username': user_info.ZA_User_Name,
            'userid': "{}".format(user_info.UserID()),
            'usermotto': "{}".format(user_info.ZA_User_motto),
            'userheadimg': "{}".format(imgurl),
            'emailif': f1(user_info.UserEmail()),# 是否设置邮箱
            'emailvalue': "{}".format(user_info.UserEmail()),
            'phoneif': f1(user_info.UserPhone()),# 是否设置手机号码
            'phonevalue': "{}".format(user_info.UserPhone()),
            'passwordif': f1(user_info.UserPassword()),# 是否设置密码
            'questionif': f3(user_info.ZA_User_questions),# 未设置密保问题
            'certificationif': f1(user_info.ZA_User_IDcard),# 已实名认证
            'birthday': "{}".format(user_info.UserBirthday()),
            'sex': int("{}".format(user_info.UserSex())),
            'sexselect': ['', '', ''],
            'ip': "{}".format(user_info.UserFromIP()),
            'identity': "{}".format(user_info.Useridentity()),
            'truename': f2("{}".format(user_info.ZA_User_TrueName)),
            'idcard': f2("{}".format(user_info.ZA_User_TrueName)),
        }
    return JsonResponse(userdata)

@loginCheck.logining
def header_Update(request):
    '''
        用于处理用户头像
        返回http状态码
    '''
    headerImgBase64 = request.POST.get('userheadimg')
    '''
    data:image/jpeg;base64,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
    '''
    imgdata = base64.b64decode(headerImgBase64[23:])
    user_info = ZA_UserInfo.objects.get(ZA_User_ID=request.session['user_id'])
    # 删除旧头像
    # 判断是否使用的是原始头像
    if 'default.jpg' in user_info.UserHeaderImg():
        upRec = imgUpdate(imgdata)
        if upRec:
            # ZA_UserInfo.objects.filter(ZA_User_ID=request.session['user_id']).update(ZA_User_HeaderImg=json.dumps(upRec))
            user_info.ZA_User_HeaderImg = json.dumps(upRec)
            user_info.save()
            UpdataHeaderURL(request,user_info.ZA_User_HeaderImg)
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=404)
    elif 'surl' in user_info.UserHeaderImg():
        upRec = imgUpdate(imgdata)
        if upRec:
            imgDelete(user_info.UserHeaderImg())
            print(json.dumps(upRec))
            # ZA_UserInfo.objects.filter(ZA_User_ID=request.session['user_id']).update(ZA_User_HeaderImg=json.dumps(upRec))
            user_info.ZA_User_HeaderImg = json.dumps(upRec)
            user_info.save()
            UpdataHeaderURL(request, user_info.ZA_User_HeaderImg)
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=404)
    else:
        return HttpResponse(status=404)

def imgUpdate(filesRB):
    """
    图片上传主函数，用于往图床上传图片
    :param filesRB: 已经读取的文件byte码
    # :param filename: 文件名
    # :param filename: 文件格式
    :return: 字典
    """
    from ZA_Tools.imgTools import sm_tools, aixinxi_tools
    imginfo = {
        'aurl':'',
        'hash':'',
        'surl':'',
        'key':'',
    }
    # 上传SM
    sm_temp = sm_tools.update(filesRB)['data']
    if sm_temp:
        imginfo['surl'] = sm_temp['url']
        imginfo['hash'] = sm_temp['hash']
    # 上传爱信息
    axx_header = aixinxi_tools.login()
    # 登陆状态检测
    if axx_header:
        # 上传
        filename = aixinxi_tools.fileNameadd()
        print('文件名预计为：%s'%filename)
        aixinxi_temp = aixinxi_tools.updata(axx_header,filename,{'file':filesRB})
        # 提交成功
        if aixinxi_temp:
            imginfo['aurl'] = filename
            imginfo['key'] = aixinxi_temp[0]
    else:
        print('爱信息图床上传失败')
    # 退出状态
    aixinxi_tools.loginOut(axx_header)
    if imginfo['aurl'] or imginfo['surl']:
        return imginfo
    else:
        return None

def imgDelete(imginfo_f):
    """
    图片删除主函数，用于删除图床上的图片
    :param imginfo: 字符串，存储在数据库字段里的字典
    :return:
    """
    from ZA_Tools.imgTools import sm_tools, aixinxi_tools
    imginfo = json.loads(imginfo_f)
    if imginfo['hash']:
        del_sm = sm_tools.delete(imginfo['hash'])
        if del_sm:
            print('sm图床删除成功！')
        else:
            print('sm图床删除失败！')
    if imginfo['key']:
        axx_header = aixinxi_tools.login()
        if axx_header:
            # 删除
            del_axx = aixinxi_tools.delete(axx_header,imginfo['key'])
            # 删除成功
            if del_axx:
                print('爱信息图床删除成功！')
            else:
                print('爱信息图床删除失败！')
        else:
            print('爱信息图床登陆失败')

def userCenter_special(request):
    context={
        'title':'特殊函数测试',
    }
    return render(request,'ZA_User/usercenter.html',context)