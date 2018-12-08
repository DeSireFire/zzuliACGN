from django.shortcuts import render
from django.core.paginator import Paginator
from .models import *
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.views import View
# Create your views here.
def BTIndex(request):
    aiueo_list = Items.objects.all()
    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1

    akasatana = Paginator(aiueo_list, per_page=1, request=request)
    aiueo_list = akasatana.page(page)
    ctx = {
        'title': '资源下载',
        'hamayarawa_list': aiueo_list
    }
    return render(request, 'ZA_ResourceDownload/Resourcedownload.html', ctx)
# 网页渲染部分
# def BTIndex(request):
#     context = {'title': '资源下载'}
#     messages = models.Message.objects.all()  #获取全部数据
#     limit = 10
#     paginator = Paginator(messages, limit)  #按每页10条分页
#     page = request.GET.get('page','1')  #默认跳转到第一页
#
#     result = paginator.page(page)
#     return render(request,'ZA_ResourceDownload/Resourcedownload.html',context)