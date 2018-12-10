from django.db import models

# Create your models here.

# 全部资源分类
class Rtypes(models.Model):
    BTtitle = models.CharField(max_length=15,unique=True)
    isdelete = models.BooleanField(default=False)
    def __str__(self):
        return self.BTtitle

#资源信息
class Items(models.Model):
    rdName = models.TextField(default='未知')#资源名称
    rdUpTime = models.CharField(max_length=50,unique=True)  # 资源发布时间
    rdSize = models.CharField(max_length=30,default='-')#资源大小
    rdUpNum = models.CharField(max_length=50,default='-')#资源上传数
    rdDownloadNum = models.CharField(max_length=50,default='-')#资源下载数
    rdInfo = models.TextField(default='暂无')#资源介绍
    rdOK = models.CharField(max_length=50,default='-')#资源完成数
    rdURLS = models.TextField(default='暂无')    #资源下载链接
    rdType = models.ForeignKey('Rtypes',on_delete=models.CASCADE)#资源种类
    rdView = models.TextField(default='')#资源详细页地址
    isdelete = models.BooleanField(default=False)#是否删除
    def __str__(self):
        return self.rdName