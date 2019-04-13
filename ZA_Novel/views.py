from django.shortcuts import render
from .models import *
# Create your views here.
# 网页渲染部分
def novelsIndex(request):
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