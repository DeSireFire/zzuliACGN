import re,requests,config,json

__author__ = 'DeSireFire'



# 是否使用专用爬虫
def crawlerChoice(parser):
    '''

    :param parser: config的parserList中的元素
    :return:
    '''
    if parser['crawler'] == 'wenku8':
        import spyder.wenku8
        print("wenku8 专用爬虫")
        return spyder.wenku8.wenku8(parser)
    else:
        print("使用通用爬虫")
        return None

# 页面尽头检测
def endDetection(response,keyList = config.keyList):
    """

    :param response: 检测是不是爬取到了网站的尽头
    :param keyList: 判断到尽头的关键字
    :return: 布尔值
    """
    if response:
        for i in keyList:
            if i in response:
                return False
        return True
    else:
        return False

# 二阶请求检测
def responseAgain(infoDict):
    """
    一般结合reglux_list方法使用，检测config.parserList[X]['pattern']['novel_info']['responseAgain']是否为空
    :param infoDict: 传入键值中有“responseAgain”的字典即可
    :return: 布尔值
    """
    if infoDict['responseAgain']:
        if re.match(r'^https?:/{2}\w.+$', infoDict['responseAgain'][0]):
            # 需要二次请求
            return True
        else:
            # 不需要二次请求,或没匹配到二次请求的地址
            return False
    else:
        return False

def reglux(str_pattern,text):
    """
    正则抓取
    :param str_pattern:正则表达式
    :param text: 需要匹配的1文本
    :return:
    """
    pattern = re.compile(str_pattern)
    matchs = pattern.findall(text)
    return  matchs


def reglux_list(mydict,response):
    """
    遍历正则抓取数据
    :param mydict: 字典类型{key:正则表达式，}
    :param response: request.text需要正则匹配的字符串
    :return: 字典类型
    """
    temp = {}
    for m,n in mydict.items():
        if '' != n:
            pattern = re.compile(n)
            matchs = pattern.findall(response)
            temp.update({m:matchs,})
        else:
            temp.update({m: list(n),})
    return temp

def proxy_list(url = config.PROXYURL,testURL = config.testURL):
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
                r = requests.get(testURL, proxies=proxies,timeout=config.TIMEOUT)
                if (not r.ok) or len(r.content) < 500:
                    r = requests.get("http://127.0.0.1:8000/delete?ip=%s&port=%s"%(ip,port))
                else:
                    return proxies

    except Exception as e:
        # print(e)
        return None

# 卷名识别以及章节从属
def titleCheck(tlist,Rlist,tkey='class="vcss"'):
    """
    若出现卷名和章节名都在同一个页面时（例如：https://www.wenku8.net/novel/1/1592/index.htm）,
    用此函数整理分卷和其所属章节的关系,并用reglux_list方法进行清洗
    :param tlist:列表，包含卷名和章节名的列表
    :param tkey:字符串，用来判断区分列表卷名和章节的关键字
    :param Rlist:传入config.parserList[i]["pattern"]["Chapter"]
    :return:
    """
    tids = []   # 筛选出“原矿”列表中，所有册名的下标
    for i in tlist:
        if tkey in i:
            tids.append(tlist.index(i))
    count = 0
    recdict = {}
    while count+1 < len(tids):# 使用卷名下标来对列表中属于章节的部分切片出来
        temp = tlist[tids[count]:tids[count + 1]]
        if count+1 == len(tids)-1:
            temp=tlist[tids[count + 1]:]
        recdict[reglux(Rlist['novel_title'],temp[0])[0]] = reglux(Rlist['novel_chapter'], ''.join(temp[1:]))
        count +=1
    print(recdict)
    # for m,n in recdict.items():
    #     print(type(n))
    #     print('%s:%s'%(m,n))