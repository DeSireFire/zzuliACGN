from ZA_Tools.sm.handler import *

def smImgUrlUper(url = None,fileRB = None,fileName = fileNameIter()):
    '''
    传入文本的网络地址，上传爱信息图床工具
    :param url: 需要上传的文本超链接
    :param fileName: 字符串，不含有文件后缀
    :return:
    '''
    try:
        # 如果URL不为None,则使用自带的requests方法来或获得图片数据
        if url:
            tempList = smUpdate(urlImg(url))
        elif fileRB:
            tempList = smUpdate(fileRB)
        else:
            return False
        res = {}
        # 整理返回信息
        if tempList:
            res = {
                'imgName':'o_%s' % (fileName),
                'axxKey':tempList[0],
            }
        return res
    except Exception as e:
        print(e)