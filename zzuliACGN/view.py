from django.shortcuts import render

# Create your views here.

# 网站404页
def page_not_found(request):
    return render(request,'ZA_Index/Construction_period.html')
