from django.shortcuts import render
from .models import *
# Create your views here.
# 网页渲染部分
def novelsIndex(request):
    context = {
        'title': '次元圣经',
        'novelTypes':[]
    }
    NtypeAll = Ntype.objects.select_related().all().order_by("id").exclude(isdelete=1)
    NtypeAll_list = list(NtypeAll.values_list('Type_title', flat=True))
    for a, b in zip(NtypeAll_list, [i for i in NtypeAll_list if i not in NtypeAll_list[1::2]]):
        context['novelTypes'].append('<li><a href="?id=%s">%s</a><a href="?id=%s">%s</a></li>'%(NtypeAll_list.index(a),a,NtypeAll_list.index(b),b))
    if not context['novelTypes']:
        context['novelTypes'] = ['<li><a href="#">暂无</a></li>']
    return render(request,'ZA_Novel/ZA_Novel.html',context)