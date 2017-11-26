from django.contrib import admin
from .models import *
# Register your models here.


# Register your models here.
class UserinfoAdmin(admin.ModelAdmin):
    '''
    用户查询在admin界面中的显示
    '''
    list_per_page = 15
    list_display = [
        'id',
        #SQLID
        'ZA_User_Email',
        # 电子邮箱
        'ZA_User_Phone',
        # 联系电话
        'ZA_User_Name',
        # 用户名
        'ZA_User_Password',
        # 密码，二次确认
        'ZA_User_motto',
        # 个性签名
        'ZA_User_Specialty',
        # 专业
        'ZA_User_StudentID',
        # 学号
        'ZA_User_Class',
        # 班级
        'ZA_User_Faculty',
        # 院系
        'ZA_User_Campus',
        # 校区
        'ZA_User_Birthday',
        # 生日
        'ZA_User_Age',
        # 年龄
        'ZA_User_Sex',
        # 性别
        'ZA_User_Constellation',
        # 星座
        'ZA_User_HomeTown',
        # 故乡
        'ZA_User_Medal',
        # 成就勋章
        'ZA_User_Department',
        # 协会部门
        'ZA_User_identity',
        # 用户身份
        'ZA_User_Permission',
        # 用户权限
        'ZA_User_FromIP',
        # 用户登录IP
        'ZA_User_HeaderImg',
        # 用户头像
        'ZA_User_Action',
        # 用户状态：0：正常 1:删除 2:黑名单 3：冻结
    ]
# # 在admin页面里面注册model中的类和admin.py中对应的类
admin.site.register(ZA_UserInfo,UserinfoAdmin)