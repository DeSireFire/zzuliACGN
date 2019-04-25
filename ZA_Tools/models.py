from django.db import models

# Create your models here.

# 图库整合
class Gallerys(models.Model):
    imgName = models.CharField('图片文件名',unique=True,max_length=255)
    imgType = models.CharField('文件格式',max_length=255)
    url = models.URLField('图片地址',default='')
    origin = models.URLField('原图片地址',default='',unique=True)
    hash = models.CharField('图hash或者key',default='',max_length=255,unique=True)
    imgMd5 = models.CharField('通过hash字段加密的md5字符串，用于其他表调用',default='',max_length=255)
    bedName = models.CharField('托管的图床名',default='',max_length=255)
    imgfrom = models.CharField('所属应用',max_length=255,default='图库')# 按照django应用名来划分，例如：user（代表头像）、new(代表咨询图片)、Gallery(代表图库)、novel(代表小说封面或者插图)
