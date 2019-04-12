from django.shortcuts import render
from .models import *
# Create your views here.
# 网页渲染部分
def novelsIndex(request):
    Ntype = type.objects.select_related().all().order_by("id").exclude(isdelete=1)
    # print(list(Ntype.values_list('Type_title', flat=True)))
    context = {
        'title': '次元圣经',
        'novelTypes':list(Ntype.values_list('Type_title', flat=True))
    }
    return render(request,'ZA_Novel/ZA_Novel.html',context)