from django.shortcuts import render
from django.core.paginator import Paginator
from .models import *
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
# 网页渲染部分以及分页
def BTIndex(request):
    try:

        # 跳转到第1页
        get_page = int(request.GET.get('page', 1))

        get_category = int(request.GET.get('category', 0))

    except PageNotAnInteger:
        # 若发现无页码，跳转会第一页
        get_page = 1
        get_category = 0

    print(get_category)

    # 如果类别为0（False），即为‘全部’，读取全部索引
    #todo 此处建议查询优化，使用select_related。
    if get_category != 0:
        temp = Rtypes.objects.all()
        Bt_type_name = {
            1:[1,11],# 查询动漫，包含动漫、季度全集,下同
            2:[2,21,22],
            3:[3,31,32,33,34],
            4:[4,41,42],
            5:[5,],
            6:[6,61,62,63,64,65,],
            7:[7],
            8:[8],
            9:[9],
        }
        all_type_list = [11,21,22,31,32,33,34,41,42,61,62,63,64,65]
        # 此处说明get_category有非0值，按类型表id查找
        if get_category < 10:
            aiueo_list = Items.objects.filter(rdType__in=Bt_type_name[get_category]).order_by("-rdUpTime").exclude(isdelete=1)
        else:
            if get_category in all_type_list:
                aiueo_list = Items.objects.filter(rdType=get_category).order_by("-rdUpTime").exclude(isdelete=1)
            else:
                aiueo_list = Items.objects.all().order_by("-rdUpTime").exclude(isdelete=1)

        # 查询动画
        # tempType = Rtypes.objects.get(BTtitle='动画')

        # 按照get请求的category参数来查询id得到一条类别
        # 注意用get()方法得到的是单个对象而不是queryset,若有多个对象满足条件应该使用filter()方法。
        # tempType = Rtypes.objects.get(id=tachitsuteto)

        # get请求的参数可以直接传给数据库查询
        # aiueo_list = Items.objects.filter(rdType__in=get_category)

        # __in表示查询多个
        # aiueo_list = Items.objects.filter(rdType__in=[1,11])

    else:
        # '全部'类型时间倒序全查,排除删除项
        aiueo_list = Items.objects.all().order_by("-rdUpTime").exclude(isdelete=1)

    # 默认首页为1，如果最后一页的数据少于5条，合并到上一页，request为必传
    # 每页80条
    akasatana = Paginator(aiueo_list, per_page=80, orphans=5, request=request)

    aiueo_list = akasatana.page(get_page)
    ctx = {
        'title': '资源下载',
        'hamayarawa_list': aiueo_list
    }
    return render(request, 'ZA_ResourceDownload/Resourcedownload.html', ctx)

# 资源具体信息页面
def iteminfo(request,url_param):
    # 用get方法查询的时候，查询不到内容的时候会抛出异常，同样查询结果多余1条的时候也会抛出异常
    # 所以建议使用filter
    itemData = Items.objects.filter(rdMagnet=url_param.split('nyaYaNya')[0])
    print(itemData)
    print(len(itemData))
    print(type(itemData))
    if itemData:
        ctx = {
            'title': '资源下载',
            'itemData':list(itemData)[0],
        }
        return render(request, 'ZA_ResourceDownload/itemView.html',ctx)
    else:
        ctx = {
            'title': '资源下载',
        }
        return render(request, 'ZA_Index/Construction_period.html')