from django.db import models
from ZA_User.models import ZA_UserInfo
from datetime import date
'''
小说文库数据库设计：

小说-id
小说-书名 
小说-简介
小说-作者
小说-插画师
小说-封面
小说-字数
小说-分类
小说-收录时间
小说-更新时间
小说-人气（分为XX网站人气）
小说-收藏数
小说-热度（点击数）

小说-册名
小说-册名id
小说-章节名
小说-章节id
小说-章节数
小说-总章节数
小说-正文

小说-订阅
'''
# Create your models here.

# 小说分类信息
class type(models.Model):
    Type_title = models.CharField('类型名称',max_length=20,unique=True) #小说的分类（玄幻 奇幻 武侠 仙侠...）
    isdelete = models.BooleanField('是否删除', default=False)   #是否删除,默认不删
    def __str__(self):
        return self.Type_title
    class Meta:
        verbose_name = '小说所属分类'
        verbose_name_plural = '小说所属分类'


# 小說基本信息
class info(models.Model):
    novel_id = models.AutoField('书id',primary_key=True,unique=True,) # 小说Id
    novelName = models.CharField('书名',max_length=255,unique=True,default='',) # 小说名
    writer = models.CharField('作者名',max_length=50,default='未知',) # 作者名
    illustrator = models.CharField('插画师名',max_length=50,default='未知',) # 插画师名
    fromPress = models.CharField('文库名',max_length=100,default='未知',)  # 文库名
    intro = models.TextField('简介',default='',) # 小说简介
    headerImage = models.URLField("小说封面URL") # 小说封面
    resWorksNum = models.IntegerField('小说字数',default='0',) # 小说字数
    index = models.TextField('小说目录',default='0',) # 小说目录
    types = models.ForeignKey(type, verbose_name='小说所属分类', on_delete=models.CASCADE) #小说所属类型
    action = models.CharField('小说文章状态',max_length=200,default='连载中..',) # 小说更新状态
    isdelete = models.BooleanField('是否删除', default=False)


    class Meta:
        verbose_name = '小说信息'
        verbose_name_plural = '小说信息'


# 小說正文信息
class detail(models.Model):
    name = models.TextField('章节所属小说',default='暂无')# 书名
    title = models.CharField('册名',max_length=255,default='正文卷') # 小说册名
    chapter = models.CharField('章节名',max_length=255,default='正文卷') # 小说章节名
    fullName = models.CharField('章节全称',max_length=255,unique=True) # 小说章节名
    worksNum = models.IntegerField('章节字数')  # 章节更新时间
    updateTime = models.DateField('章节更新时间', max_length=50)  # 章节更新时间
    chapterImgurls = models.TextField('章节插画',default='暂无')  # 章节插画
    container = models.TextField(default='',) # 小说正文
    isDelete = models.BooleanField('是否删除', default=False)

    class Meta:
        verbose_name = '小說章节信息'
        verbose_name_plural = '小說章节信息'
