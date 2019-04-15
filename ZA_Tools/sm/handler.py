import requests,re,json
from ZA_Tools.imgTools.config import *
from ZA_Tools.imgTools.publicHandlers import *

# 获取指定url的图片bytes
def urlImg(url):
    '''
    本来是只打算左sm图床的文本查看的，但是想象什么区别，
    :param url: 需要请求的网络连接
    :return:bytes
    '''
    req = requests.get(url=url)
    choose = req.status_code
    while choose!=200:
        req = requests.post(url=url)
        choose = req.status_code
    return req.content

# 上传文件
def smUpdate(filesReadRB):
    """
    上传文件,运行结果：
    sm.ms OK!
    {'code': 'success', 'data': {'width': 150, 'height': 155, 'filename': '1.jpg', 'storename': '5bec117f535fc.jpg', 'size': 28902, 'path': '/2018/11/14/5bec117f535fc.jpg', 'hash': 'FvYgRt1ok4LHCiM', 'timestamp': 1542197631, 'ip': '182.88.140.112', 'url': 'https://i.loli.net/2018/11/14/5bec117f535fc.jpg', 'delete': 'https://sm.ms/delete/FvYgRt1ok4LHCiM'}}

    :param filesReadRB:byte,以rb方式读取的文件
    :return:成功返回respones,失败返回None
    """
    try:
        if fileSize(filesReadRB):
            files = {'smfile': filesReadRB, }
            req = requests.post(url=sm_update_url, headers=sm_update_header, files=files)
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

# 删除文件
def delete(hash):
    """
    ['File delete success.']
    :param hash: 字符串，sm存图时用的hash
    :return: 布尔值
    """
    try:
        req = requests.post(url=sm_delete_url%hash)
        pattern = re.compile(
            '<div class="bs-callout bs-callout-warning" style="border-left-width: 2px;">([\s\S]*?)</div>', re.S)
        titles = re.findall(pattern, req.text)
        if "File delete success." == titles[0] or 'File already deleted.' in titles[0]:
            print('图片删除成功')
            return True
        else:
            print('图片删除失败')
            return False
    except Exception as e:
        # print(e)
        return False


if __name__ == '__main__':
    files = open('1.jpg','rb')
    reqtext = smUpdate(files)
    files.close()
    delete(reqtext['data']['hash'])