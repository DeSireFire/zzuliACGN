from django.shortcuts import render

# Create your views here.
# 网页渲染部分
def BTIndex(request):
    context = {'title': '资源下载'}
    return render(request,'ZA_ResourceDownload/Resourcedownload.html',context)