from django.db import models

# Create your models here.

# 全部资源分类
class Rtypes(models.Model):
    BTtitle = models.CharField(max_length=15,unique=True)
    isdelete = models.BooleanField(default=False)
    def __str__(self):
        return self.BTtitle

#资源信息
# unique唯一约束，适用于CharField，不适用TextField
class Items(models.Model):
    rdName = models.TextField(default='未知')#资源名称
    rdUpTime = models.DateTimeField(max_length=50)  # 资源发布时间
    rdSize = models.CharField(max_length=30,default='-')#资源大小
    rdUpNum = models.CharField(max_length=50,default='-')#资源上传数
    rdDownloadNum = models.CharField(max_length=50,default='-')#资源下载数
    rdInfo = models.TextField(default='暂无')#资源介绍
    rdOK = models.CharField(max_length=50,default='-')#资源完成数
    rdMagnet = models.CharField(default='暂无',max_length=255,unique=True,)    #资源下载链接
    rdMagnet2 = models.CharField(default='暂无',max_length=255)    #资源下载链接
    rdTracker = models.TextField(default='暂无')    #资源下tracker服务器
    rdFileList = models.TextField(default='暂无')    #资源文件列表
    rdType = models.ForeignKey('Rtypes',on_delete=models.CASCADE)#资源种类
    rdView = models.CharField(default='',max_length=255,unique=True,)#资源详细页地址
    rdUper = models.CharField(default='未知',max_length=100)#资源发布者
    isdelete = models.BooleanField(default=False)#是否删除
    def __str__(self):
        return self.rdName