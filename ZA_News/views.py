from django.shortcuts import render

# Create your views here.
# 网站模块临时展示页
def ZA_Show(request):
    context = {'title': '宅新闻'}
    return render(request,'ZA_News/index.html',context)