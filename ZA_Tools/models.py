from django.db import models

# Create your models here.

# 图库整合
class Gallerys(models.Model):
    imgName = models.CharField('图片文件名',unique=True,max_length=255)
    axxUrl = models.URLField('爱信息图片地质',default='')
    smUrl = models.URLField('sm图片地质',default='')
    axxKey = models.CharField('爱信息图Key',default='',max_length=255)
    smhash = models.CharField('sm图hash',default='',max_length=255)
    imgfrom = models.CharField('所属应用',max_length=255,default='图库')# 按照django应用名来划分，例如：user（代表头像）、new(代表咨询图片)、Gallery(代表图库)、novel(代表小说封面或者插图)
