import urllib.request,re

my_headers = {
    'Host':'www.liuli.in',
    'Referer':'http://www.llss.pw/wp/about.html',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
}

#爬取总页码
my_request = urllib.request.Request('https://www.liuli.in/wp/anime.html',data=None,headers = my_headers)
my_responese = urllib.request.urlopen(my_request)
my_html = my_responese.read().decode('utf-8')
page_list = re.findall(r'<ul><li class="page_info">Page (.*?) of (.*?)</li><li class="active_page">', my_html)
print('一共查找数据%s页'%page_list)

#爬取第一层动画数据
second_list = []
# for i in range(1,int(page_list[0][1])):
for i in range(25,30):
    my_request = urllib.request.Request('https://www.liuli.in/wp/anime.html/page/%s'%i,data=None,headers = my_headers)
    my_responese = None
    try:
        my_responese = urllib.request.urlopen(my_request,timeout=60)
    except:
        print('请求不到数据！')

    if my_responese != None:
        my_html = my_responese.read().decode('utf-8')
        titie_url = re.findall('<h1 class="entry-title"><a href="(.*?)" rel="bookmark">(.*?)</a></h1>',my_html)
        for i in titie_url:
            print("Save %s"%str(i))
            second_list.append(i)
    else:
        print('爬取完毕！')

print('第一层地址写入text!')
with open(r'url-list.txt', 'a') as f:
    for line in second_list:
        f.write(r"%s" %str(line))
        f.write('\n')

# 爬取第二层动画数据
page_list = {v: k for k, v in dict(second_list).items()}
# page_list = {'233':'http://www.llss.pw/wp/44979.html'}

Finall_dict = {}
with open(r'url.txt','a') as f:
    for k1,v1 in page_list.items():
        print("开始爬取!%s"%v1)
        my_request = urllib.request.Request(v1, data=None, headers=my_headers)
        my_responese = urllib.request.urlopen(my_request)
        my_html = my_responese.read().decode('utf-8')
        magent_list = ['magnet:?xt=urn:btih:%s'%x[1] for x in re.findall(r'(magnet:?xt=urn:btih:)?((?!\d+$)[0-9A-z\u672c\u7ad9\u4e0d\u63d0\u4f9b\u4e0b\u8f7d]{40,47})[^"_\.jpg\.jpeg]', my_html)]
        new_magent_list = []
        for i in range(len(magent_list)):
            next_if = magent_list.pop()

            if '本站不提供下载' in next_if and len(next_if) == 67 and "_" not in next_if or len(next_if) == 60 and "_" not in next_if:
                magent_str = next_if.replace('本站不提供下载','')
                new_magent_list.append(magent_str)
                print('发现关键字(本站不提供下载),去除！')
            else:
                if len(magent_list) == 0:
                    print('%s的磁性链接没有查找到！进行二次查找' % v1)
                    magent_list = ['magnet:?xt=urn:btih:%s' % x[1] for x in re.findall(r'@(.*)([: ])(.*){32,40}',my_html)]
                    for i in range(len(magent_list)):
                        next_if = magent_list.pop()
                        if len(next_if) != 21:
                            new_magent_list.append(magent_list)
                else:
                    print('发现疑似假冒磁性链接！%s 已经过滤！' % next_if)

            Finall_dict[k1] = '%s'%new_magent_list
            print('%s写入text!'%Finall_dict[k1])
            f.write("""
    标题名：%s
    磁性链接地址：%s
    详细页面地址：%s
            """%(k1,Finall_dict[k1],page_list[k1]))
            f.write('\n')
