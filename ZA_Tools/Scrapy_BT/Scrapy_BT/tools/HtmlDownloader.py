# coding:utf-8

import random
from Scrapy_BT.tools import config
import json
from Scrapy_BT.tools import HtmlHandler
# from db.DataStore import sqlhelper

__author__ = 'DeSireFire'

import requests
import chardet

P = {
    "http":"http://114.113.126.86:80",
    "https":"https://220.161.202.12:808",
    # "https":"https://106.60.44.145:80",

}

class Html_Downloader(object):
    @staticmethod
    def download(url):
        """
        获取网页
        :param url: 请求的网页地址
        :return: 返回网页内容
        """
        try:
            # 网页请求成功
            r = requests.get(url=url, headers=config.get_header(), timeout=config.TIMEOUT, proxies=HtmlHandler.proxy_list())
            # r = requests.get(url=url, headers=config.get_header(), timeout=config.TIMEOUT)

            # 获取网页编码格式，并修改为request.text的解码类型
            r.encoding = chardet.detect(r.content)['encoding']
            if r.encoding == "GB2312":
                r.encoding = "GBK"

            # 网页请求OK或者请求得到的内容过少，判断为连接失败
            if (not r.ok) or len(r.content) < 500:
                raise ConnectionError
            else:
                return r.text

        except Exception:
            count = 0  # 重试次数
            # proxylist = sqlhelper.select(10)
            proxylist = json.loads(requests.get(config.PROXYURL).text)
            if not proxylist:
                return None

            while count < config.RETRY_TIME:
                try:
                    proxy = random.choice(proxylist)
                    ip = proxy[0]
                    port = proxy[1]
                    proxies = {"http": "http://%s:%s" % (ip, port), "https": "http://%s:%s" % (ip, port)}

                    # r = requests.get(url=url, headers=config.get_header(), timeout=config.TIMEOUT, proxies=P)
                    r = requests.get(url=url, headers=config.get_header(), timeout=config.TIMEOUT, proxies=proxies)
                    r.encoding = chardet.detect(r.content)['encoding']
                    if (not r.ok) or len(r.content) < 500:
                        raise ConnectionError
                    else:
                        return r.text
                except Exception:
                    count += 1

        return None

if __name__ == '__main__':
    # print(config.parserList[0]["urls"][0])
    # c = Html_Downloader
    # rec = c.download(config.parserList[0]["urls"][0])
    # print(rec)
    # print(len(rec))
    pass