from django.db import models
from datetime import date
# todo 可能需要加入敏感词库
# Create your models here.
class ZA_UserInfo(models.Model):
    '''
    用户注册时间
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
    出生日期
    性别
    星座
    故乡
    成就
    协会部门
    用户身份： 0：校外人士 1：普通学生 2：老师
    用户权限: 0：校外人士 1：普通学生 2：社团干部 3:老师 4：网站管理员 5：超级管理员 6:站长
    用户来源：IP
    用户头像
    用户状态：   0：正常 1:删除 2:黑名单 3：冻结
    '''




    ZA_User_ID = models.AutoField('用户ID',primary_key=True,unique=True,)
    # 用户ID(自增)
    ZA_User_RegTime = models.DateField('用户注册时间',default=date.today,)
    # 用户注册时间
    ZA_User_Email = models.CharField('电子邮箱',max_length=100,unique=True,default='',)
    #电子邮箱
    ZA_User_Phone = models.CharField('联系电话',max_length=11,default='',blank=True,)
    #联系电话
    ZA_User_Name = models.CharField('用户名',max_length=20,unique=True,)
    #用户名
    ZA_User_Password = models.CharField('密码',max_length=65,default='',)
    #密码，二次确认
    ZA_User_motto = models.CharField('个性签名',max_length=60,default='',blank=True,)
    #个性签名
    ZA_User_StudentID = models.CharField('学号',max_length=12,default='',blank=True,)
    #学号
    ZA_User_Faculty = models.CharField('院系',max_length=60,default='校外人士',blank=True,)
    #院系
    ZA_User_Campus = models.CharField('校区',max_length=60,default='校外人士',blank=True,)
    #校区
    ZA_User_Birthday = models.CharField('出生日期',max_length=60,default='',blank=True,)
    #出生日期
    ZA_User_Sex = models.CharField('性别',max_length=2,default='2',blank=True,)
    #性别
    ZA_User_identity = models.CharField('用户身份',max_length=2,default='0',)
    #用户身份
    ZA_User_FromIP = models.CharField('用户登录IP',max_length=20,default='IPUnknow',blank=True,)
    #用户登录IP
    # ZA_User_HeaderImg = models.ImageField('用户头像',upload_to="ZA_User/img/HeaderImg", default='/ZA_User/img/HeaderImg/default.jpg',blank=True,)
    ZA_User_HeaderImg = models.CharField('用户头像',max_length=200, default='/ZA_User/img/HeaderImg/default.jpg',blank=True,)
    # 用户头像
    ZA_User_Action = models.CharField('用户状态',max_length=6, default='0',)
    # 用户状态：0：正常 1:删除 2:黑名单 3：冻结
    ZA_User_TrueName = models.CharField('真实姓名', max_length=50, default='Unknow', )
    # 用户实名姓名
    ZA_User_IDcard = models.CharField('实名身份证', max_length=50, default='Unknow', )
    # 用户实名身份证号码
    ZA_User_Blist = models.TextField('用户黑名单', default='[{}]', )
    # 用户黑名单
    ZA_User_questions = models.TextField('用户密保问题', default="[]", )
    # 用户密保问题
    ZA_User_level = models.TextField('用户等级', max_length=50, default='0', )

    # def __str__(self):
    #     str_ZA_User_ID = str(self.ZA_User_ID)
    #     return str_ZA_User_ID

    # class Meta:
    #     verbose_name = '用户信息'


    def UserAction(self):
        actionDirct = {0:"正常",1: "删除",2:"黑名单",3:"冻结"}
        return actionDirct[self.ZA_User_Action]

    def UserID(self):
        return self.ZA_User_ID
    def UserRegTime(self):
        return self.ZA_User_RegTime
    def UserEmail(self):
        return self.ZA_User_Email
    def UserPhone(self):
        return self.ZA_User_Phone
    def UserName(self):
        return self.ZA_User_Name
    def UserPassword(self):
        return self.ZA_User_Password
    def UseMotto(self):
        return self.ZA_User_motto
    def UserStudentID(self):
        return self.ZA_User_StudentID
    def UserFaculty(self):
        return self.ZA_User_Faculty
    def UserCampus(self):
        return self.ZA_User_Campus
    def UserBirthday(self):
        return self.ZA_User_Birthday
    def UserSex(self):
        return self.ZA_User_Sex
    def Useridentity(self):
        return self.ZA_User_identity
    def UserFromIP(self):
        return self.ZA_User_FromIP
    def UserHeaderImg(self):
        return self.ZA_User_HeaderImg

    UserAction.short_description = '用户状态'
    UserID.short_description = '用户ID'
    UserRegTime.short_description = '用户注册时间'
    UserEmail.short_description = '电子邮箱'
    UserPhone.short_description = '联系电话'
    UserName.short_description = '用户名'
    UserPassword.short_description = '密码'
    UseMotto.short_description = '个性签名'
    UserStudentID.short_description = '学号'
    UserFaculty.short_description = '院系'
    UserCampus.short_description = '校区'
    UserBirthday.short_description = '出生日期'
    UserSex.short_description = '性别'
    Useridentity.short_description = '用户身份'
    UserFromIP.short_description = '用户登录IP'
    UserHeaderImg.short_description = '用户头像'