from django.shortcuts import render

# Create your views here.

# 网站招新展示页
def ZA_show(request):
    return render(request,'ZA_Show/ZA_show.html')