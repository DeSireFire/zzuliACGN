'''
    所有Tool会共同用到的函数
'''
import requests,json,sys,hashlib
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

# 文件名生成器
def fileNameIter():
    hash_md5 = hashlib.md5(fileName_data)
    return hash_md5.hexdigest()