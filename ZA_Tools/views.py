from django.shortcuts import render,HttpResponseRedirect
# import urllib.request
import chardet
import requests as nya
# Create your views here.
# 网站模块临时展示页

# def testspider(temp):
#     response = urllib.request.urlopen(temp).read().decode("utf-8")
#     return response

def ZA_Show(request):
    response = nya.get('http://t1.aixinxi.net/o_1d67ri9e81odjqhr17bbs8s184la.txt')
    response.encoding = chardet.detect(response.content)['encoding']
    if response.encoding == "GB2312":
        response.encoding = "GBK"
    # 跳转网页
    # return HttpResponseRedirect('http://t1.aixinxi.net/o_1d67ri9e81odjqhr17bbs8s184la.txt')
    # 渲染网页
    # context = {'title': '网站工具', 'test':testspider('http://t1.aixinxi.net/o_1d67ri9e81odjqhr17bbs8s184la.txt')}
    context = {'title': '网站工具', 'test':response.text}
    return render(request,'test.html',context)