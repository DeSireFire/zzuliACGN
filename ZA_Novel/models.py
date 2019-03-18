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
    isDelete = models.BooleanField('是否删除', default=False)   #是否删除,默认不删
    def __str__(self):
        return self.Type_title
    class Meta:
        verbose_name = '小说所属分类'
        verbose_name_plural = '小说所属分类'


# 小說基本信息
class novel_info(models.Model):
    novel_id = models.AutoField('书id',primary_key=True,unique=True,) # 小说Id
    novel_name = models.CharField('书名',max_length=255,unique=True,default='',) # 小说名
    n_writer = models.CharField('作者名',max_length=100,unique=True,default='未知',) # 作者名
    n_illustrator = models.CharField('插画师名',max_length=100,unique=True,default='未知',) # 插画师名
    n_library = models.CharField('文库名',max_length=100,unique=True,default='未知',)  # 文库名
    n_intro = models.TextField('简介',default='',) # 小说简介
    n_headerImage = models.URLField("小说封面URL", unique=True) # 小说封面
    n_worksNum = models.CharField('小说字数',max_length=200,default='0',) # 小说字数
    n_types = models.ForeignKey(type, verbose_name='小说所属分类', on_delete=models.CASCADE) #小说所属类型
    n_saveTime = models.DateField('小说收录时间',default=date.today,) # 小说收录时间
    n_updateTime = models.DateField('小说更新时间',default=date.today,) # 小说更新时间
    n_action = models.CharField('小说文章状态',default='连载中..',) # 小说更新时间


    class Meta:
        verbose_name = '小说信息'
        verbose_name_plural = '小说信息'


# 小說正文信息
class novel_detail(models.Model):
    n_name = models.ForeignKey('novel_info', verbose_name='章节所属小说', on_delete=models.CASCADE)
    novel_title = models.CharField('小说册名',max_length=200,default='正文卷',) # 小说册名
    '''
    思路记录：
    由于小说主体内容过大，所以不适合保存在后端服务器；
    采取存储在第三方的方式，并保存相应的保存地址，通过后台发送请求获取文章正文；
    novel_container 预计存储格式如下：
    [[小说章节名1,保存地址1],[小说章节名2,保存地址2],[小说章节名3,保存地址3]..]
    小说章节数，则以该列表的下标+1的方式记录。
    '''
    container = models.TextField('小说章节名+正文',default='',) # 小说正文


    class Meta:
        verbose_name = '小說章节信息'
        verbose_name_plural = '小說章节信息'
