from django.shortcuts import render

# Create your views here.
# 网页渲染部分
def novelsIndex(request):
    context = {'title': '次元圣经'}
    return render(request,'ZA_Novel/ZA_Novel.html',context)