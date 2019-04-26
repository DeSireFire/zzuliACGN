from django.shortcuts import render,HttpResponseRedirect
from django.http import JsonResponse,HttpResponse
# import urllib.request
import chardet,re
import requests
from .models import *

# 网站模块临时展示页

# def testspider(temp):
#     response = urllib.request.urlopen(temp).read().decode("utf-8")
#     return response

# def ZA_Show(request):
#     response = requests.get('http://t1.aixinxi.net/o_1d67ri9e81odjqhr17bbs8s184la.txt')
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
                MBresponse = requests.get('https://raw.githubusercontent.com/DeSireFire/animeTrackerList/master/%s.txt'%listName)
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
        'status':500,# 手动响应状码
        'magnet':'',# 生成的磁性链接
        'magnetInfo':'未知错误,，请重试...',# 错误信息说明
    }
    getMagnet = request.POST.get('magnet')
    if getMagnet:
        m = r'magnet:?[^"]+'
        if re.findall(m, getMagnet):
            try:
                MBresponse = requests.get('https://raw.githubusercontent.com/DeSireFire/animeTrackerList/master/animeTrackers_all.txt')
                magnetInfo['magnet'] = r'%s%s'%(getMagnet,''.join(list(map(lambda x: '&tr='+x,MBresponse.text.split()))))
                magnetInfo['status'] = MBresponse.status_code
                magnetInfo['magnetInfo'] = '获取成功，点击下载！'
                return JsonResponse(magnetInfo)
            except:
                magnetInfo['status'] = 404
                magnetInfo['magnetInfo'] = '获取失败，请重试...'
                return JsonResponse(magnetInfo)
        else:
            magnetInfo['magnetInfo'] = '大兄弟，你这个磁链接接有点不对劲呐'
            return JsonResponse(magnetInfo)
    else:
        magnetInfo['magnetInfo'] = '未接收到磁性链接，请重试...'
        return JsonResponse(magnetInfo)

def imgUrlSave(request):
    '''
    通过图片URL保存
    :param imgUrl: 字符串，客户端通过get请求传的图片URL
    :return:
    '''
    imgInfo = {
        'imgName':None,
        'axxUrl':None,
        'smUrl':None,
        'axxKey':None,
        'smhash':None,
        'imgfrom':None,
        'status':False,
    }
    # 倒入axx图床图片上传函数,以及图片请求函数,文件命名函数
    from ZA_Tools.axx.mainer import axxImgUrlUper,urlImg,fileNameIter
    # 导入sm图窗上传函数
    from ZA_Tools.sm.mainer import smImgUrlUper
    imgUrl = request.GET.get('imgUrl')
    # TODO 短时间内如果发送两次请求，会保存两次
    if imgUrl:
        # 图片bytes数据
        imgBytes = urlImg(imgUrl)
        # 生成的图片名字
        fileName = '{Fname}.{Fformat}'.format(Fname = fileNameIter(imgUrl.split('/')[-1].split('.')[0]),Fformat = imgUrl.split('/')[-1].split('.')[1])


        # 由于sm图床会自动命名文件名所以优先上传
        smTemp = smImgUrlUper(fileRB=imgBytes, fileName=fileName)
        if smTemp:
            imgInfo.update(smTemp)
            fileName = imgInfo['imgName']

        axxTemp = axxImgUrlUper(fileRB = imgBytes,fileName = fileName)
        if axxTemp:
            imgInfo.update(axxTemp)
        if imgInfo['axxKey'] or imgInfo['smhash']:
            imgInfo['status'] = True
            return JsonResponse(imgInfo)
        else:
            return JsonResponse(imgInfo)
    else:
        return JsonResponse(imgInfo)

def imgBytesUpdate(fileName,fileRB,bedName = 'sm',imgfrom = 'tools',imgMd5 = None):
    '''
    图片更新上传工具函数,只用sm.ms
    :param fileRB:图片文件bytes数据
    :return:
    '''
    imgInfo = {
        'imgName':None,
        'url':None,
        'origin':'',
        'hash':None,
        'imgMd5':imgMd5,
        'bedName':bedName,
        'imgfrom':imgfrom,
    }
    from ZA_Tools.sm.mainer import smImgUrlUper
    smTemp = smImgUrlUper(fileRB=fileRB, fileName=fileName)
    if smTemp:  # 上传是否成功
        imgInfo.update(smTemp)  # 更新字典
        if imgMd5:  # md5如果不为空则为更新
            pass
        else:   # 为空则直接存
            # 生成图片身份md5
            imgInfo['imgMd5'] = genearteMD5(imgInfo['imgName'])
            # 创建新的图片对象
            newImg = Gallerys()
            newImg.imgMd5 = imgInfo['imgMd5']
            newImg.imgName = imgInfo['imgName']
            newImg.url = imgInfo['url']
            newImg.origin = imgInfo['origin']
            newImg.hash = imgInfo['hash']
            newImg.bedName = imgInfo['bedName']
            newImg.imgfrom = imgInfo['imgfrom']
            newImg.save()

    else:
        return None


'''
    所有Tool会共同用到的函数
'''
import json,sys,hashlib
from ZA_Tools.imgTools.config import delproxyIP,TIMEOUT,fileName_data

def proxy_list(url,testURL):
    """
    获取并检测代理池返回的IP
    :param url: 获取IP的代理池地址
    :param testURL: 检测网址
    :return: 一个能用的ip组成的proxies字典
    """
    count = 0 # 获取的IP数
    try:
        r = requests.get(url)
        count = len(json.loads(r.text))
        while count != 0:
            r = requests.get(url)
            ip_ports = json.loads(r.text)
            count = len(ip_ports)
            for i in range(0,4):
                ip = ip_ports[i][0]
                port = ip_ports[i][1]
                proxies = {
                    'http': 'http://%s:%s' % (ip, port),
                    'https': 'https://%s:%s' % (ip, port)
                }
                r = requests.get(testURL, proxies=proxies,timeout=TIMEOUT)
                if (not r.ok) or len(r.content) < 500:
                    r = requests.get(delproxyIP%(ip,port))
                else:
                    return proxies

    except Exception as e:
        # print(e)
        return None

# 判断文件大小
def fileSize(filesReadRB):
    """
    判断文件大小
    :param filesReadRB:byte,以rb方式读取的文件
    :return:布尔值
    """
    size = sys.getsizeof(filesReadRB)/float(1024)
    if size < 5120:
        return True
    else:
        return False

# 生成MD5
def genearteMD5(tempStr):
    # 创建md5对象
    hl = hashlib.md5()

    # Tips
    # 此处必须声明encode
    # 否则报错为：hl.update(str)    Unicode-objects must be encoded before hashing
    hl.update(tempStr.encode(encoding='utf-8'))
    return hl.hexdigest()