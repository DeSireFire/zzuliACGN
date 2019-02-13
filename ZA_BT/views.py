from django.shortcuts import render
from django.core.paginator import Paginator
from .models import *
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
# 网页渲染部分以及分页
def BTIndex(request):
    try:
        # 跳转到第1页
        sashisuseso = request.GET.get('page', 1)
        tachitsuteto = request.GET.get('category', 0)
    except PageNotAnInteger:
        # 若发现无页码，跳转会第一页
        sashisuseso = 1
        tachitsuteto = 0

    # 读取全部索引
    aiueo_list = Items.objects.all()
    print(type(aiueo_list))
    # 默认首页为1，如果最后一页的数据少于5条，合并到上一页，request为必传
    akasatana = Paginator(aiueo_list, per_page=80, orphans=5, request=request)

    aiueo_list = akasatana.page(sashisuseso)
    print(type(aiueo_list))
    ctx = {
        'title': '资源下载',
        'hamayarawa_list': aiueo_list
    }
    return render(request, 'ZA_ResourceDownload/Resourcedownload.html', ctx)

