from django.db import models

# Create your models here.
# 新闻分类
class newsType(models.Model):
    Type_title = models.CharField('类型名称',max_length=50,unique=True) #小说的分类（玄幻 奇幻 武侠 仙侠...）
    isdelete = models.BooleanField('是否删除', default=False)   #是否删除,默认不删
    def __str__(self):
        return self.Type_title
    class Meta:
        verbose_name = '新闻分类'
        verbose_name_plural = '新闻分类'
# 宅新闻
class news(models.Model):
    news_title = models.CharField('标题', default='', max_length=255, unique=True)
    news_category = models.ForeignKey('newsType',on_delete=models.CASCADE)
    news_tags = models.URLField('标签',default='')
    news_writer = models.URLField('作者',default='')
    news_origin = models.CharField('来源',default='',max_length=255)
    news_upTime = models.CharField('发布时间',default='',max_length=255)
    news_content = models.TextField('正文',default='',)# 按照django应用名来划分，例如：user（代表头像）、new(代表咨询图片)、Gallery(代表图库)、novel(代表小说封面或者插图)
