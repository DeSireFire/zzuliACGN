from django.shortcuts import render

# Create your views here.

# 网站施工（维护）页
def Construction_period(request):
    return render(request,'ZA_Index/Construction_period.html')

# 网站招新展示页
def ZA_show(request):
    return render(request,'ZA_Show/ZA_show.html')
