from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from .models import *
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
    import json
    context = {
        'title': '次元圣经',
        'book':{},
        'index':{},
    }
    book = info.objects.select_related().all().order_by("novel_id").exclude(isdelete=1).filter(novel_id = bid)
    context['book'] = list(book.values())[0]
    context['index'] = list(book.values())[0]['contents']

    return render(request, 'ZA_Novel/ZA_BookInfo.html', context)

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
