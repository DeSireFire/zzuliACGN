import requests,re,json,hashlib
# from Spyder.aixinxi.aixinxi_config import *
from aixinxi_config import *


# 登陆aixinxi
def login():
    """
    只允许成功不许失败
    :return:登陆成功后返回cookie
    """
    header = get_header()
    choose = True
    while choose:
        req = requests.post(url=login_url, headers=get_header(), data=login_dirt)
        header.update({'cookie':req.headers['Set-Cookie'][:36],})
        choose = logining(header)
        if choose:
            print('登陆成功！')
            print(header)
            return header

# 检测当前cooke的登陆状态
def logining(header):
    """
    判断是否为登陆状态
    :param header: 字典，请求头
    :return: 布尔值
    """
    req = requests.post(url=index_url, headers=header)
    # req = requests.post(url=index_url, headers=header, proxies=proxy_list())
    if '<a href="https://tu.aixinxi.net/views/login.php"><i class="fa fa-user" aria-hidden="true"></i> 登录/注册</a>' not in req.text:
        return True
    else:
        return False

# 读取所有文件列表
def userFiles(header):
    """
    :param header: 字典，请求头
    :return: 列表，所有图片文件名和key,例如：[('6472a56c546d31de83a1xxxxxxxx', 'o_1cq3oq991g0q1lt3121t04boka.jpg'),]
    """
    page = 1
    imgdata = []
    while page != 0:
        url = 'https://tu.aixinxi.net/views/userFiles.php?page=%s' % (page)
        # 普通请求一次,如果失败就会进入循环
        req = requests.get(url=url, headers=header)
        choose = req.status_code
        while choose != 200:
            req = requests.get(url=url, headers=header)
            choose = req.status_code
        pattern = re.compile(r'<td><a style="color:#000" target="_blank" href="https://tu.aixinxi.net/views/fileJump.php\?key=(.*?)&ming=(.*?)">管理</a>', re.S)
        tempfilesList = re.findall(pattern, req.text)
        if tempfilesList:
            imgdata += tempfilesList
            page += 1
        else:
            page = 0
    return imgdata

# 上传并保存文件
def updata(header,fileName,filesRead):
    """

    :param header: 请求头部
    :param filesRead: 已经读取过的文件数据，例如：filesRead = {'file': open('1.jpg', 'rb')}
    :param filesRead: 字符串，带后缀的文件名，例如：xxx.png
    :return: 布尔值
    """
    # if 'referer' in header:
    #     del header['referer']
    #     header.update(update_header)
    # else:
    #     header.update(update_header)

    # 获取上传的地址
    req_ossurl = requests.post(url=index_url, headers=header)
    choose = req_ossurl.status_code
    while choose!=200:
        req = requests.get(url=token_url, headers=header)
        choose = req.status_code
    new_update_url = re.findall('upserver ="(.*?)";var', req_ossurl.text)[0]
    print('获取上传地址:%s'%new_update_url)
    update_url = new_update_url
    temp_data = token_get(header)
    update_data['policy'] = temp_data['policy']
    update_data['signature'] = temp_data['signature']
    update_data['OSSAccessKeyId'] = temp_data['AccessKeyId']
    update_data['name'] = fileName
    update_data['key'] = fileName
    req = requests.post(url=update_url, headers=header, data=update_data, files=filesRead, timeout = 120)
    choose = str(req)
    while choose != '<Response [200]>':
        req = requests.get(url=token_url, headers=header)
        choose = str(req)
    info = save(header,fileName)
    if info:
        print('保存成功！')
        print(info)
        return info
    else:
        print('保存失败！')
        return False

# 保存文件
def save(header,fileName):
    """
    da2293e8d43a8decf0136c6ee44c0f20,jpg,
    {'Server': 'Tengine', 'Date': 'Mon, 12 Nov 2018 12:18:32 GMT', 'Content-Type': 'text/html; charset=UTF-8', 'Transfer-Encoding': 'chunked', 'Connection': 'keep-alive', 'Vary': 'Accept-Encoding', 'X-Powered-By': 'PHP/5.6.30', 'Expires': 'Thu, 19 Nov 1981 08:52:00 GMT', 'Cache-Control': 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0', 'Pragma': 'no-cache', 'Content-Encoding': 'gzip'}
    ['04d1cff3e980155df7538088166d0446,png,']
    {'Server': 'Tengine', 'Date': 'Mon, 12 Nov 2018 12:24:09 GMT', 'Content-Type': 'text/html; charset=UTF-8', 'Transfer-Encoding': 'chunked', 'Connection': 'keep-alive', 'Vary': 'Accept-Encoding', 'X-Powered-By': 'PHP/5.6.30', 'Expires': 'Thu, 19 Nov 1981 08:52:00 GMT', 'Cache-Control': 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0', 'Pragma': 'no-cache', 'Content-Encoding': 'gzip'}

    :param header: 请求头
    :param fileName: 文件名
    :return:列表，例如：[da2293e8d43a8decf0136c6ee44c0f20,jpg,]
    """
    header.update(save_header)
    data_save['ming'] = fileName
    req = requests.post(url=save_url, headers=header, data=data_save)
    print(req)
    print(req.text)
    choose = req.status_code
    while choose!=200:
        req = requests.post(url=save_url, headers=header, data=data_save)
        choose = req.status_code
    return req.text.split(',')[:2]

# 删除图片
def delete(header,key):
    """
    {'User-Agent': 'Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)', 'cookie': 'PHPSESSID=gb9b12bgkn4a8gv1mf2ur50ud3', 'referer': 'https://tu.aixinxi.net/views/pic.php?key=da2293e8d43a8decf0136c6ee44c0f20', 'upgrade-insecure-requests': '1', 'origin': 'https://tu.aixinxi.net'}
    ok.删除成功
    {'Server': 'Tengine', 'Date': 'Mon, 12 Nov 2018 12:38:01 GMT', 'Content-Type': 'text/html; charset=UTF-8', 'Transfer-Encoding': 'chunked', 'Connection': 'keep-alive', 'Vary': 'Accept-Encoding', 'X-Powered-By': 'PHP/5.6.30', 'Content-Encoding': 'gzip'}
    :param header: 请求头部
    :param key: 图片的key
    :return:布尔值
    """
    header.update(delete_header)
    header['referer'] += key
    data_delete['key'] = key
    req = requests.post(url=delete_url, headers=header, data=data_delete)
    if 'ok' in req.text:
        print('OK')
        print(req.status_code)
        print(req.text)
        print(req.headers)
        return True
    else:
        print(req.status_code)
        print(req.text)
        print(req.headers)
        return False

# 关键字查找
def filesFind(header,fileName):
    """
    查找存在fileName的所有文件
    :param header: 请求头
    :param fileName: 需要查询的文件名
    :return: 列表，[key,fileName] 例如：['1b655e2a822747c3c78af0859ca1b63c', 'o_1cq3gdm9jqcm11g87jv1ghiqaea.jpg']
    """
    page = 1
    data = []
    while page != 0:
        url = 'https://tu.aixinxi.net/views/userFiles.php?page=%s' % (page)
        # 普通请求一次,如果失败就会进入循环
        req = requests.get(url=url, headers=header)
        choose = req.status_code
        while choose != 200:
            req = requests.get(url=url, headers=header)
            choose = req.status_code
        pattern = re.compile(r'<td><a style="color:#000" target="_blank" href="https://tu.aixinxi.net/views/fileJump.php\?key=(.*?)&ming=(.*?)">管理</a>', re.S)
        tempfilesList = re.findall(pattern, req.text)
        if tempfilesList:
            for t in tempfilesList:
                if fileName in str(t):
                    fileslist = list(t)
                    print('查找到:%s' % fileslist)
                    data += [fileslist]
            page += 1
        else:
            page = 0
    return data


# token密钥获取
def token_get(header):
    """
    {'policy': 'xx', 'signature': 'xx', 'AccessKeyId': 'xx'}/False
    :param header: 请求头部
    :return: 成功，传回字典；失败传回False
    """
    req = requests.get(url=token_url, headers=header)
    choose = req.status_code
    while choose!=200:
        req = requests.get(url=token_url, headers=header)
        choose = req.status_code
    return json.loads(req.text)

# 文件名生成器
def fileNameIter(name = fileName_data):
    import time
    temp = '%s%s'%(str(int(time.time())),name)
    hash_md5 = hashlib.md5(temp.encode("utf-8"))
    return hash_md5.hexdigest()

# 退出aixinxi
def loginOutloginOut(outcookie):
    """
    只允许成功不允许失败的请求
    :param outcookie: 传入已经登陆了的cookie值
    :return:
    """
    req = requests.post(url=loginOut_url, headers={'cookie':outcookie}, data=loginOut_dirt)
    choose = req.status_code
    while choose!=200:
        req = requests.post(url=loginOut_url, headers={'cookie': outcookie}, data=loginOut_dirt)
        choose = req.status_code
    print('退出成功！')

# 获取指定url的文本内容
def urlText(url):
    '''
    本来是只打算左爱信息图床的文本查看的，但是想象什么区别，
    干脆弄成啥文本都能看算了
    注意：只能查看文本文件，图片不行！！！
    :param url: 需要请求的网络连接
    :return:字符串，文本
    '''
    import chardet
    req = requests.post(url=url)
    choose = req.status_code
    while choose!=200:
        req = requests.post(url=url)
        choose = req.status_code
    # 获取网页编码格式，并修改为request.text的解码类型
    req.encoding = chardet.detect(req.content)['encoding']
    if req.encoding == "GB2312":
        req.encoding = "GBK"
    return req.text


def main():

    # 登陆爱信息图床并返回有关头部信息
    ok = login()
    # 查询操作
    # 查询该登录账号在爱信息图床所有的图片名
    fl = userFiles(ok)
    print(fl)
    # 传入已登陆的cookie值
    loginOutloginOut(ok['cookie'])


if __name__ == '__main__':
    main()