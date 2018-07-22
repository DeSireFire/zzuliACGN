import urllib.request,re,time,random

my_headers = {
    # 'Host': 'www.ibiqu.net',
    # 'Connection': 'keep-alive',
    # 'Cache-Control': 'max-age=0',
    # 'Upgrade-Insecure-Requests': '1',
    # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    # 'Referer': 'http://www.ibiqu.net/modules/article/search.php?searchkey=%E6%AD%A6%E7%82%BC%E5%B7%85%E5%B3%B0',
    # 'Accept-Language': 'zh-CN,zh;q=0.9',
    # 'Cookie': 'Hm_lvt_18fc5822be0d81f091b08e7dd694d63f=1523192246; width=85%25; Hm_lpvt_18fc5822be0d81f091b08e7dd694d63f=1523193895',

    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Host':'www.xxsy.net',
    'Referer':'http://www.xxsy.net/chapter/8243301.html',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
}

sec_headers={
    # 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    # 'Connection':'keep-alive',
    # 'Cookie':'width=85%25; Hm_lvt_18fc5822be0d81f091b08e7dd694d63f=1523192246,1523198009; Hm_lpvt_18fc5822be0d81f091b08e7dd694d63f=1523198012',
    # 'Host':'www.ibiqu.net',
    # 'Referer':'http://www.ibiqu.net/book/111/75040.htm',
    # 'Upgrade-Insecure-Requests':'1',
    # 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',

    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Host': 'www.xxsy.net',
    'Referer': 'http://www.xxsy.net/chapter/8243301.html',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',

}
The_net = 'http://www.xxsy.net'

#爬取总页码
# my_request = urllib.request.Request('http://www.ibiqu.net/book/111/',data=None,headers = my_headers)
my_request = urllib.request.Request('%s/chapter/8243301.html'%The_net,data=None,headers = my_headers)
my_responese = urllib.request.urlopen(my_request)
my_html = my_responese.read().decode('utf8')
# page_list = re.findall(r'<dd><a href="(.*?)">(.*?)</a></dd>', my_html)
# page_list = re.findall(r'<li>(.*?)</li>', my_html)
# print('FindBookTitleName:%s'%len(page_list))
print(my_html)
# for p in page_list[1140:]:
#     # print('章节名：%s  URL:http://www.ibiqu.net%s'%(p[1],p[0]))
#     print('章节名：%s  URL:%s%s'%(p[1],The_net,p[0]))
#     # URL = 'http://www.ibiqu.net%s'%p[0]
#     URL = '%s%s'%(The_net,p[0])
#     sec_request = urllib.request.Request(URL,data=None,headers = sec_headers)
#     sec_responese = urllib.request.urlopen(sec_request)
#
#     # sec_html = sec_responese.read()
#     try:
#         sec_html = sec_responese.read().decode('gbk')
#     except UnicodeDecodeError as UDE:
#         print('Find The UnicodeDecodeError')
#         with open(r'error.txt' , 'a') as f:
#                 f.write('章节名：%s  URL:%s%s'%(p[1],The_net,p[0]))
#                 f.write('\n')
#     else:
#         # sec_bookname = re.findall(r'<h1>(.*?)</h1>', sec_html)
#         sec_bookname = re.findall(r'<h1 class="chapter-title">(.*?)</h1>', sec_html)
#         sec_content = re.findall(r'<p>(.*?)</p>', sec_html)
#         pline = page_list.index(p)+1
#         with open(r'%s - 古穿今之国民妖精 - %s.txt'%(pline,sec_bookname[0]), 'a') as f:
#             for line in sec_content:
#                 print(line)
#                 f.write(r"%s" % str(line))
#                 f.write('\n')
#         time.sleep(random.randint(5,10))
