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
    Type_title = models.CharField('类型名称',max_length=20) #小说的分类（玄幻 奇幻 武侠 仙侠...）
    isDelete = models.BooleanField('是否删除', default=False)   #是否删除,默认不删
    def __str__(self):
        return self.ZA_Novel_Type_title
    class Meta:
        verbose_name = '小说所属分类'
        verbose_name_plural = '小说所属分类'

# 小说作者信息
class artist(models.Model):
    writer = models.CharField('作者名',max_length=50,unique=True,default='未知',) # 作者名
    illustrator = models.CharField('插画师名',max_length=50,unique=True,default='未知',) # 插画师名
    library = models.CharField('文库名',max_length=100,unique=True,default='未知',)  # 文库名
    Result = models.CharField('作者作品',max_length=100,unique=True,default='未知',)  # 作者作品
    Tags = models.CharField('作者自定义标签',max_length=100,default='',)  # 作者自定义标签

    class Meta:
        verbose_name = '作者信息'
        verbose_name_plural = '作者信息'


# 读者信息
class reader(models.Model):
    readerId = models.ForeignKey(to=ZA_UserInfo,to_field="ZA_User_ID",verbose_name='读者ID', on_delete=models.CASCADE)# 读者ID
    # ZA_Novel_Username = models.OneToOneField(ZA_UserInfo,to_field="ZA_User_Name",related_name="ZA_User_Name",verbose_name='读者信息', on_delete=models.CASCADE)# 读者信息
    history = models.CharField('读书历史',max_length=200,default='未知',) # 读书历史
    subscription = models.CharField('读者书架',max_length=50,unique=True,default='未知',) # 读者书架

    class Meta:
        verbose_name = '读者信息'
        verbose_name_plural = '读者信息'


# 小說基本信息
class novel_info(models.Model):
    # teacherAccount = models.OneToOneField('UserInfo')
    # teacherName = models.CharField(max_length=5)
    # teacherPhoto = models.ImageField(upload_to='pictures/')
    # teacherIntro = models.CharField(max_length=300)

    novel_id = models.AutoField('书d',primary_key=True,unique=True,) # 小说Id
    novel_name = models.CharField('书名',max_length=100,unique=True,default='',) # 小说名
    novel_writer = models.ForeignKey(artist,to_field="writer", verbose_name='该小说作者', on_delete=models.CASCADE)  # 作者名
    novel_intro = models.CharField('书名',max_length=200,default='',) # 小说简介
    novel_headerImage = models.URLField("小说封面URL", unique=True) # 小说封面
    novel_worksNum = models.CharField('小说字数',max_length=200,default='0',) # 小说字数
    novel_types = models.ForeignKey(type, verbose_name='小说所属分类', on_delete=models.CASCADE) #小说所属类型
    novel_saveTime = models.DateField('小说收录时间',default=date.today,) # 小说收录时间
    novel_updateTime = models.DateField('小说更新时间',default=date.today,) # 小说更新时间


    class Meta:
        verbose_name = '小说信息'
        verbose_name_plural = '小说信息'


# 小說章节信息
class Chapter(models.Model):
    novel_novel_name = models.ForeignKey(novel_info,to_field="novel_name", verbose_name='章节所属小说', on_delete=models.CASCADE)
    novel_title = models.CharField('小说册名',max_length=200,default='正文卷',) # 小说册名
    novel_secondaryId = models.CharField('小说章节id', unique=True ,max_length=200,default='',) # 小说章节id（用于网页）
    novel_chapter = models.CharField('小说章节名', unique=True ,max_length=200,default='',) # 小说章节名
    novel_chapterId = models.CharField('小说章节id', unique=True ,max_length=200,default='',) # 小说章节ID
    novel_chapterSecNum = models.CharField('小说章节数',max_length=100,default='',) # 小说章节数
    novel_chapterNum = models.CharField('小说总章节数',max_length=100,default='',) # 小说总章节数
    novel_container = models.TextField('小说正文',default='',) # 小说正文

    class Meta:
        verbose_name = '小說章节信息'
        verbose_name_plural = '小說章节信息'

# 小说人气信息
class Top(models.Model):
    novel_name = models.ForeignKey(novel_info,to_field="novel_name", verbose_name='小说的人气信息', on_delete=models.CASCADE)
    novel_top = models.CharField('小说人气',max_length=200,default='0',) # 小说人气
    novel_collections = models.CharField('小说收藏数',max_length=200,default='0',) # 小说收藏数
    novel_hop = models.CharField('人气',max_length=200,default='0',) # 人气（分为XX网站人气）