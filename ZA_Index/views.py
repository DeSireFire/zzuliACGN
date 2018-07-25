from django.shortcuts import render

# Create your views here.

# 网站施工（维护）页
def Construction_period(request):
    return render(request,'ZA_Index/Construction_period.html')


