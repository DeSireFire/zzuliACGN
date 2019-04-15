from ZA_Tools.sm.handler import *

def imgUrlUper(url,fileName = fileNameIter()):
    '''
    传入文本的网络地址，上传爱信息图床工具
    :param url: 需要上传的文本超链接
    :param fileName: 字符串，不含有文件后缀
    :return:
    '''
    try:

        tempList = smUpdate(files)
        res = {}
        # 整理返回信息
        if tempList:
            res = {
                'imgName':'o_%s.%s' % (fileName, url.split('.')[-1]),
                'axxKey':tempList[0],
            }
        return res
    except Exception as e:
        print(e)