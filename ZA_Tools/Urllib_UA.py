import urllib.request,re
import random

'''
import chardet   #需要导入这个模块，检测编码格式
encode_type = chardet.detect(html)  
html = html.decode(encode_type['encoding']) #进行相应解码，赋给原标识符（变量）

从str到bytes:调用方法encode().
编码是把Unicode字符串以各种方式编码成为机器能读懂的ASCII字符串
从bytes到str:调用方法decode().
'''
my_headers = {
    'Content-Type':'text/html; charset=UTF-8',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # 'Cookie':'__utma=233080474.91846665.1520173981.1520173981.1520173981.1; __utmb=233080474; __utmc=233080474; __utmz=233080474.1520173981.1.1.utmccn=(referral)|utmcsr=google.co.jp|utmcct=/|utmcmd=referral',
    'Host': 'www.useragentstring.com',
    'Referer': 'http://www.useragentstring.com/pages/useragentstring.php',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
}

#爬取总页码
my_request = urllib.request.Request('http://www.useragentstring.com/pages/useragentstring.php?typ=Browser',data=None,headers = my_headers)
my_responese = urllib.request.urlopen(my_request)
my_html = my_responese.read()
Deco_html = my_html.decode('iso-8859-1')
UA_list = re.findall(r"<a href='/index\.php\?id=(.*?)'>(.*?)</a></li>", Deco_html)
print('发现共%s条UA'%len(UA_list))
with open(r'UA_list2.txt', 'a') as f:
    for line in UA_list:
        f.write(r"%s" %str(line[1]))
        f.write('\n')
# s = open(r'UA_list.txt','r').readline()
# print(s)

