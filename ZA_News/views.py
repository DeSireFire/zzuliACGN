from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from django.core import serializers
# Create your views here.
# 网站模块临时展示页
def ZA_News(request):
    context = {'title': '宅新闻'}
    return render(request,'ZA_News/index.html',context)


def typeList(request):
    '''
    宅新闻种类
    '''
    typeList = [
        '动画情报',
        '漫画情报',
        '轻小说情报',
        '动漫周边',
        '声优情报',
        '音乐资讯',
        '游戏资讯',
        '美图欣赏',
        '乱七八糟',
                ]
    context = {'title': '宅新闻'}
    return JsonResponse(typeList)

def type_news(request):
    '''
    按分类新闻
    '''
    typeList = [
        '动画情报',
        '漫画情报',
        '轻小说情报',
        '动漫周边',
        '声优情报',
        '音乐资讯',
        '游戏资讯',
        '美图欣赏',
        '乱七八糟',
                ]
    try:

        typeName = request.GET.get('typeName')  # 新闻类别
        idStart = request.GET.get('idStart')  # 从第几个新闻开始返回数据

    except:

        typeName = '全部'
        idStart = 1

    if typeName not in typeList: # 不存在则全排列
        newsList = news.objects.select_related().all.order_by("-news_upTime").exclude(isdelete=1)
    else:
        newsList = news.objects.select_related().all.order_by("-news_upTime").exclude(isdelete=1).filter(news_category=typeList.index(typeName)+1)

    # dataLen = newsList.count()
    # if int(idStart)-1 <= dataLen:
    #     newsInfo = serializers("json",newsList[int(idStart):int(idStart)+20])
