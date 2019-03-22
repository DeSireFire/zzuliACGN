from django.shortcuts import render,HttpResponseRedirect
from django.http import JsonResponse,HttpResponse
# import urllib.request
import chardet,re
import requests as nya
# Create your views here.
# 网站模块临时展示页

# def testspider(temp):
#     response = urllib.request.urlopen(temp).read().decode("utf-8")
#     return response

# def ZA_Show(request):
#     response = nya.get('http://t1.aixinxi.net/o_1d67ri9e81odjqhr17bbs8s184la.txt')
#     response.encoding = chardet.detect(response.content)['encoding']
#     if response.encoding == "GB2312":
#         response.encoding = "GBK"
#     # 跳转网页
#     # return HttpResponseRedirect('http://t1.aixinxi.net/o_1d67ri9e81odjqhr17bbs8s184la.txt')
#     # 渲染网页
#     # context = {'title': '网站工具', 'test':testspider('http://t1.aixinxi.net/o_1d67ri9e81odjqhr17bbs8s184la.txt')}
#     context = {'title': '网站工具', 'test':response.text}
#     return render(request,'test.html',context)

def animeTrackerListGet(request):
    '''
    优化磁性连接
    :param request:
    :return:
    '''
    getMagnet = request.GET.get('magneturl',)
    listName = request.GET.get('trackers', 'animeTrackers_best')
    dn_get = request.GET.get('dn')
    URLS = {
        'animeTrackers_best',
        'animeTrackers_all',
        'animeTrackers_bad',
        'animeTrackers_all_udp',
        'animeTrackers_all_http',
        'animeTrackers_all_https',
        'animeTrackers_all_ws',
        'animeTrackers_best_ip',
        'animeTrackers_all_ip',
    }
    re_json = {
        'status': False,
        'magnet':'',
    }
    if getMagnet:
        m = r'magnet:?[^"]+'
        if re.findall(m, getMagnet):

            if listName not in URLS:
                listName = 'animeTrackers_all'
            try:
                MBresponse = nya.get('https://raw.githubusercontent.com/DeSireFire/animeTrackerList/master/%s.txt'%listName)
                re_json['magnet'] = r'%s&dn=%s%s'%(getMagnet,dn_get,''.join(list(map(lambda x: '&tr='+x,MBresponse.text.split()))))
                re_json['status'] = True
                return JsonResponse(re_json)
            except:
                return JsonResponse(re_json)
        else:
            re_json['magnet'] = '大兄弟，你这个磁链接接有点不对劲呐'
            return JsonResponse(re_json)
    else:
        re_json['magnet'] = '磁性连接在哪呢？我可爱的宝贝～'
        return JsonResponse(re_json)


def loadingmagnet(request):
    '''
    用于zzuliacgn内部的优化工具
    :param request:
    :return:
    '''
    magnetInfo = {
        'status':'500',# 手动响应状码
        'magnetURL':'',# 生成的磁性链接
        'magnetInfo':'未知错误,，请重试...',# 错误信息说明
    }
    getMagnet = request.POST.get('magnet')
    if getMagnet:
        print(getMagnet)
        m = r'magnet:?[^"]+'
        if re.findall(m, getMagnet):
            try:
                MBresponse = nya.get('https://raw.githubusercontent.com/DeSireFire/animeTrackerList/master/animeTrackers_all.txt')
                magnetInfo['magnetURL'] = r'%s%s'%(getMagnet,''.join(list(map(lambda x: '&tr='+x,MBresponse.text.split()))))
                magnetInfo['status'] = str(MBresponse.status_code)
                magnetInfo['magnetInfo'] = '获取成功，点击下载！'
                return JsonResponse(magnetInfo)
            except:
                magnetInfo['status'] = '404'
                magnetInfo['magnetInfo'] = '获取失败，请重试...'
                return JsonResponse(magnetInfo)
        else:
            magnetInfo['magnetInfo'] = '大兄弟，你这个磁链接接有点不对劲呐'
            return JsonResponse(magnetInfo)
    else:
        magnetInfo['magnetInfo'] = '未接收到磁性链接，请重试...'
        return JsonResponse(magnetInfo)