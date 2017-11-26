from django.db import models

# Create your models here.

class ZA_UserInfo(models.Model):
    '''
    联系电话
    电子邮箱
    用户名
    个性签名
    密码，二次确认
    学号
    专业
    班级
    院系
    校区
    生日
    年龄
    性别
    星座
    故乡
    成就
    协会部门
    用户身份：是否非学生
    用户权限
    用户来源：IP
    用户头像
    用户状态：0：正常 1:删除 2:黑名单 3：冻结
    '''
    ZA_User_Email = models.CharField(max_length=100)
    #电子邮箱
    ZA_User_Phone = models.CharField(max_length=11,default='')
    #联系电话
    ZA_User_Name = models.CharField(max_length=20,unique=True)
    #用户名
    ZA_User_Password = models.CharField(max_length=60,default='')
    #密码，二次确认
    ZA_User_motto = models.CharField(max_length=60,default='')
    #个性签名
    ZA_User_Specialty = models.CharField(max_length=40,default='')
    #专业
    ZA_User_StudentID = models.CharField(max_length=12,default='')
    #学号
    ZA_User_Class = models.CharField(max_length=60,default='')
    #班级
    ZA_User_Faculty = models.CharField(max_length=60,default='')
    #院系
    ZA_User_Campus = models.CharField(max_length=60,default='')
    #校区
    ZA_User_Birthday = models.CharField(max_length=60,default='')
    #生日
    ZA_User_Age = models.CharField(max_length=60,default='')
    #年龄
    ZA_User_Sex = models.CharField(max_length=60,default='')
    #性别
    ZA_User_Constellation = models.CharField(max_length=20,default='')
    #星座
    ZA_User_HomeTown = models.CharField(max_length=20,default='')
    #故乡
    ZA_User_Medal = models.CharField(max_length=20,default='')
    #成就勋章
    ZA_User_Department = models.CharField(max_length=20,default='')
    #协会部门
    ZA_User_identity = models.CharField(max_length=20,default='')
    #用户身份
    ZA_User_Permission = models.CharField(max_length=20,default='')
    #用户权限
    ZA_User_FromIP = models.CharField(max_length=20,default='')
    #用户登录IP
    ZA_User_HeaderImg = models.CharField(max_length=200, default='default.img')
    # 用户头像
    ZA_User_Action = models.CharField(max_length=2, default='0')
    # 用户状态：0：正常 1:删除 2:黑名单 3：冻结

