import requests,re,json,sys
from ZA_Tools.imgTools.config import *

# 上传文件
def update(filesReadRB):
    """

    :param filesReadRB:byte,以rb方式读取的文件
    :return:
    """
    try:
        if fileSize(filesReadRB):
            files = {'smfile': filesReadRB, }
            req = requests.post(url=sm_update_url, headers=sm_update_header, files=files, proxies=proxy_list())
            if req.json()['code'] == 'success':
                print('sm.ms OK!')
                print(req.json())
                return req.json()

            else:
                print('sm.ms error!')
                print(req.json())
                return None
        else:
            return None
    except Exception as e:
        # print(e)
        return None

# 判断文件大小
def fileSize(filesReadRB):
    """

    :param filesReadRB:byte,以rb方式读取的文件
    :return:
    """
    size = sys.getsizeof(filesReadRB)/float(1024)
    if size < 5120:
        return True
    else:
        return False



def proxy_list(url = PROXYURL,testURL = testURL):
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



if __name__ == '__main__':
    # myheader = {
    # 'Host':'sm.ms',
    # }
    files = open('1.jpg','rb')
    reqtext = update(files)
    # req = requests.post(url="https://sm.ms/api/upload",files=files)
    # print(req.json())
    files.close()
    '''
    成功以后运行结果如下：
    {'code': 'success', 'data': {'width': 150, 'height': 155, 'filename': '1.jpg', 'storename': '5bc9d5e084d19.jpg', 'size': 28902, 'path': '/2018/10/19/5bc9d5e084d19.jpg', 'hash': 'nVgKA5E8tLcofJx', 'timestamp': 1539954144, 'ip': '171.36.8.151', 'url': 'https://i.loli.net/2018/10/19/5bc9d5e084d19.jpg', 'delete': 'https://sm.ms/delete/nVgKA5E8tLcofJx'}}
    其他结果均为失败！
    由于只是测试所以就不要给别人的图床增加那么多负担啦,这是浪费资源，何况这是一个免费的良心图床，
    不要让贡献者寒心，所以测试完，记得删除！这是礼仪！
    '''
    req = requests.post(url=reqtext['data']['delete'])
    pattern = re.compile('<div class="bs-callout bs-callout-warning" style="border-left-width: 2px;">([\s\S]*?)</div>',re.S)
    titles = re.findall(pattern,req.text)
    print(titles)
