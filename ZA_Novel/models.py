from django.db import models
from ZA_User.models import ZA_UserInfo
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
class ZA_NovelType(models.Model):
    ZA_Novel_Type_title = models.CharField('类型名称',max_length=20) #小说的分类（玄幻 奇幻 武侠 仙侠...）
    isDelete = models.BooleanField('是否删除', default=False)   #是否删除,默认不删
    def __str__(self):
        return self.ZA_Novel_Type_title
    class Meta:
        verbose_name = '小说所属分类'
        verbose_name_plural = '小说所属分类'

# 小说作者信息
class ZA_NovelArtistInfo(models.Model):
    ZA_Novel_writer = # 作者名
    ZA_Novel_illustrator = # 插画师名
    ZA_Novel_library = # 文库名
    ZA_Novel_Result = # 作者作品
    ZA_Novel_Tags = # 作者自定义标签


# 读者信息
class ZA_NovelUserInfo(models.Model):

    ZA_Novel_UserId = # 读者id
    ZA_Novel_UserName = # 读者名
    ZA_Novel_history = # 读书历史
    ZA_Novel_subscription = # 读者书架

# 小說基本信息
class ZA_NovelInfo(models.Model):
    # teacherAccount = models.OneToOneField('UserInfo')
    # teacherName = models.CharField(max_length=5)
    # teacherPhoto = models.ImageField(upload_to='pictures/')
    # teacherIntro = models.CharField(max_length=300)

    ZA_Novel_id = # 小说Id
    ZA_Novel_name = # 小说名
    ZA_Novel_intro = # 小说简介
    ZA_Novel_headerImage = # 小说封面
    ZA_Novel_worksNum = # 小说字数
    ZA_Novel_types = models.ForeignKey(ZA_NovelType, verbose_name='小说所属分类', on_delete=models.CASCADE)     #小说所属类型
    ZA_Novel_saveTime = # 小说收录时间
    ZA_Novel_updateTime = # 小说更新时间
    ZA_Novel_top = # 小说人气
    ZA_Novel_collections = # 小说收藏数
    ZA_Novel_hop = # 人气（分为XX网站人气）
    ZA_Novel_title = # 小说册名
    ZA_Novel_secondaryId = #小说章节id（用于网页）
    ZA_Novel_chapter = # 小说章节名
    ZA_Novel_chapterId = # 小说章节ID
    ZA_Novel_chapterSecNum = # 小说章节数
    ZA_Novel_chapterNum = # 小说总章节数
    ZA_Novel_container = # 小说正文


    class Meta:
        verbose_name = '小说信息'
        verbose_name_plural = '小说信息'