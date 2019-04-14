from axx import *
# 默认cookie头部
default_h = {
    'User-Agent': 'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52',
    'cookie': 'PHPSESSID=ns4e93j1oppq5qkn51dl5dko62',
    'referer': 'https://tu.aixinxi.net/views/pages.php?id=explore',
    'upgrade-insecure-requests': '1'
}
if not logining(default_h):
    default_h = login()


def strUper(tempStr,header=default_h,logout = False,fileName = fileNameIter()):
    '''
    传入字符串，上传爱信息图床工具
    :param headrs: 头部，包含默认值
    :param tempStr: 需要上传的字符串
    :param fileName: 字符串，不含有文件后缀
    :return:
    '''
    # 检查登陆状态
    files = {'file': bytes(tempStr, encoding = "utf8")}
    try:
        temp = updata(header, 'o_%s.txt'%fileName, files)
        res = {
            '文件名':'o_%s.txt'%fileName,
            'url':'http://t1.aixinxi.net/o_%s.txt'%fileName,
            'key':temp[0],
            '文件格式':temp[1],
        }
        return res
    except Exception as e:
        print(e)
    finally:
        if logout:
            loginOutloginOut(header['cookie'])

def textUrlUper(url,header=default_h,logout = False,fileName = fileNameIter()):
    '''
    传入文本的网络地址，上传爱信息图床工具
    :param url: 需要上传的文本超链接
    :param headrs: 头部，包含默认值
    :param logout: 布尔值，是否在完成操作后退出登陆状态
    :param fileName: 字符串，不含有文件后缀
    :return:
    '''
    try:
        tempStr = urlText(url)
        files = {'file': bytes(tempStr, encoding="utf8")}
        return updata(header, 'o_%s.txt' % fileName, files)
    except Exception as e:
        print(e)
    finally:
        if logout:
            loginOutloginOut(header['cookie'])

def textContrast(tempStr1,header=default_h,logout = False):
    '''
    查询字符串与图床上的文本是否一致..
    不建议使用次方法..查询速度特别慢
    :param tempStr1:
    :param header:
    :param logout:
    :return:
    '''
    try:
        txtfiles = filesFind(header, 'txt')
        for i in txtfiles:
            tempStr2 = ''.join(urlText('http://t1.aixinxi.net/%s'%(i[1])))
            tempStr1 = ''.join(tempStr1)
            if len(tempStr1) == len(tempStr2):
                print(i)
        # return updata(header, 'o_%s.txt' % fileName, files)
    except Exception as e:
        print(e)
    finally:
        if logout:
            loginOutloginOut(header['cookie'])

if __name__ == '__main__':
    # f = open('1文学少女.txt', 'r', encoding='UTF-8')
    # tempStr = f.read()
    # f.close()
    tempStr = '从前有座山，山里有座庙，庙里有个和尚,在吃肉松饼！'
    try:
        a = strUper(tempStr,default_h,fileName='d9285d6239ctestnv1233')
        print(a)
        # textContrast(tempStr,header=default_h,logout = False)
    except Exception as e:
        pass
        # print(e)
    finally:
        pass
        loginOutloginOut(default_h['cookie'])

