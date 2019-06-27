from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from .models import *
import json
# Create your views here.
# 网页渲染部分
def novelsIndex(request):
    '''
    响应小说页首页
    :param request:
    :return:
    '''
    context = {
        'title': '次元圣经',
        'novelTypes_html':[],
        'novelTypes':[],
    }
    NtypeAll = Ntype.objects.select_related().all().order_by("id").exclude(isdelete=1)
    context['novelTypes'] = list(NtypeAll.values_list('Type_title', flat=True))
    for a, b in zip(context['novelTypes'], [i for i in context['novelTypes'] if i not in context['novelTypes'][1::2]]):
        context['novelTypes_html'].append('<li><a href="?id=%s">%s</a><a href="?id=%s">%s</a></li>'%(context['novelTypes'].index(a),a,context['novelTypes'].index(b),b))
    if not context['novelTypes_html']:
        context['novelTypes_html'] = ['<li><a href="#">暂无</a></li>']
    return render(request,'ZA_Novel/ZA_Novel.html',context)


def bookInfo(request,bid):
    context = {
        'title': '次元圣经',
        'book':{},
        'index':{},
    }
    book = info.objects.select_related().all().order_by("novel_id").exclude(isdelete=1).filter(novel_id = bid)
    context['book'] = list(book.values())[0]
    context['index'] = list(book.values())[0]['contents']
    # todo 字段中目录contents中存储的数据格式存在问题，甚至是爬虫本身也存在问题
    return render(request, 'ZA_Novel/ZA_BookInfo.html', context)

def categoryIndex(request):
    '''
    首页分类获取
    :param request:
    :return:
    '''
    test = {'typeList':[{'name':'666','url':'6666'},{'name':'7777','url':'8888'},{'name':'7777','url':'8888'},{'name':'7777','url':'8888'},{'name':'7777','url':'8888'}]}
    return JsonResponse(test)

def category(request):
    '''
    首页各分类小说列表
    :param request:
    :return:
    '''
    context = {
        'title': '次元圣经',
        'List':[],
        'Ranking':[],
    }
    temp_category = request.GET.get('category')
    categoryAll = info.objects.select_related().all().order_by("novel_id").exclude(isdelete=1).filter(types__Type_title=temp_category)[:5]
    context['List'] = list(categoryAll.values('novel_id','novelName','writer','resWorksNum','headerImage','types','action','fromPress','illustrator'))
    # context['Ranking'] = categoryAll.query
    return JsonResponse(context)

def booksList(request):
    '''
    balabala
    :param request:
    :return:
    '''
    temp_data = {
                'hot':[
                    {'title':'我的姐姐有中二病','href':'https://www.iqing.com/book/34961','alt':'轻小说：我的姐姐有中二病','src':'http://rs.sfacg.com/web/novel/images/NovelCover/Big/2018/09/d36532df-2c23-4f5c-bebf-81fe948730fa.jpg','type':'轻小说','word':'58.1万字','state':'连载中','author':'嘎嘎'},
                    {'title':'我的子昂有中二病','href':'https://www.iqing.com/book/34961','alt':'轻小说：我的姐姐有中二病','src':'http://rs.sfacg.com/web/novel/images/NovelCover/Big/2018/09/d36532df-2c23-4f5c-bebf-81fe948730fa.jpg','type':'轻小说','word':'58.1万字','state':'连载中','author':'嘎嘎'},
                    ],
               'recommend':[
                {'title':'刀剑神域','href':'https://www.iqing.com/book/59609','src':'./次元圣经 郑州轻工大学 动漫协会！_files/5b9c39b1-3485-4cb2-b7e7-fb7ce1f88df5.jpg','num':'322.5','profile':'虽然是游戏，但可不是闹着玩的！'},
                {'title':'神话传说英雄的异世界奇谭','href':'https://www.iqing.com/book/70248','src':'./次元圣经 郑州轻工大学 动漫协会！_files/88d3c85c-e6cb-4af0-9afc-aa750342ae65.jpg','num':'11.6','profile':'我拿你当兄弟，你却要泡我重孙女？'},
                {'title':'Fate/Prototype 苍银的碎片','href':'https://www.iqing.com/book/35981','src':'./次元圣经 郑州轻工大学 动漫协会！_files/102fe928-efdf-4ec6-b26a-a7654f1ceb5b.jpg','num':'132.2','profile':'为了你，我愿意放弃一切！'},
                ],
                'zhanli':{
                    'list1':[
                    {'title':'精灵幻想记','href':'https://www.zzuliacgn.com/book/34962','alt':'轻小说：精灵幻想记','src':'./次元圣经 郑州轻工大学 动漫协会！_files/680ed4d9-0568-4113-944d-95ab025ae17e.jpg','author':'HJ文库','zhanli':'291.4'},
                    {'title':'百炼霸王与圣约女武神','href':'https://www.zzuliacgn.com/book/34925','alt':'轻小说：百炼霸王与圣约女武神','src':'./次元圣经 郑州轻工大学 动漫协会！_files/e69f9980-88a5-4395-bb95-587af47477cc.jpg','author':'HJ文库','zhanli':'252.8'},
                    {'title':'带着智能手机闯荡异世界','href':'https://www.zzuliacgn.com/book/39311','alt':'轻小说：带着智能手机闯荡异世界','src':'./次元圣经 郑州轻工大学 动漫协会！_files/f5f65df2-4791-4fb4-9b4d-1afbb9bd4daf.jpg','author':'HJ文库','zhanli':'907.9'}
                ],
                    'list2':[
                    {'title':'异世界料理道','href':'https://www.zzuliacgn.com/book/38406','zhanli':'137.0'},
                    {'title':'战斗面包师与机械看板娘','href':'https://www.zzuliacgn.com/book/39673','zhanli':'31.1'},
                ]
                }
               }
    # return JsonResponse(temp_data, safe=False)
    return JsonResponse(temp_data)