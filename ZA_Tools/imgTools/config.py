import random,time
from zzuliACGN.config import aixinxi_login_dirt

'''
    附加信息设置
'''
# 爱信息图床，登陆用户名和密码
aixinxi_login = aixinxi_login_dirt
# 爱信息图床，退出登陆所需参数
aixinxi_loginOut_dirt = {
    "action":"logout",
}
# 爱信息图床，删除所需data
aixinxi_data_delete = {
'key':'44764c752081126b509b12091356f56c',
}
# 爱信息图床，上传时的附加数据
aixinxi_update_data = {
'name':'o_test.jpg',
'policy':'eyJleHBpcmF0aW9uIjoiMjAxOC0xMS0xMVQxNDozNzo1NFoiLCJjb25kaXRpb25zIjpbWyJjb250ZW50LWxlbmd0aC1yYW5nZSIsMCwxMDQ4NTc2MF0sWyJzdGFydHMtd2l0aCIsIiRrZXkiLCIiXV19',
'signature':'maH2ayNKySSl5nvbPdJvdm4/Gro=',
'OSSAccessKeyId':'LTAIyUoGoXRUSdwm',
'key':'o_test.jpg',
'success_action_status':'200',
}
# 爱信息图床，保存操作所需附加信息
aixinxi_data_save = {
'ming':'o_1cqs8t6tg1s0h1sddovn50ika.mp4',
}
# 爱信息图床，加密用的文件名
fileName_data = "{}{}".format(random.randint(0,9),int(time.time())).encode('utf8')

# sm.ms,上传data
sm_data = {'smfile':'',}



'''
    网页地址设置
'''
# 爱信息图床，网站首页
aixinxi_index_url = "https://tu.aixinxi.net/index.php"
# 爱信息图床，登陆地址
aixinxi_login_url = "https://tu.aixinxi.net/includes/userAction.php"
# 爱信息图床，退出登录的连接地址
aixinxi_loginOut_url = 'https://tu.aixinxi.net//includes/userAction.php?action=logout'
# 爱信息图床，上传文件地址
aixinxi_update_url = 'https://tu-t1.oss-cn-hangzhou.aliyuncs.com/'
# 爱信息图床，保存信息地址
aixinxi_save_url = 'https://tu.aixinxi.net/includes/save.php'
# 爱信息图床，删除文件地址
aixinxi_delete_url = 'https://tu.aixinxi.net/includes/delete_file.php'
# 爱信息图床，token地址
aixinxi_token_url = 'https://tu.aixinxi.net/includes/token.php'

# sm.ms，上传地址
sm_update_url = 'https://sm.ms/api/upload'
# sm.ms,删除地质
sm_delete_url = 'https://sm.ms/delete/%s'




'''
    代理设置
'''
# 本地代理池地址
PROXYURL = "http://193.112.52.146:8000/?types=0&count=10&country=国内"
# 用于测试IP可用的地址
testURL = "http://tu.aixinxi.net/"
# 删除无用IP
delproxyIP = 'http://http://193.112.52.146/delete?ip=%s&port=%s'
# 代理检测时长
TIMEOUT = 3






'''
    UserAgent设置
'''
# UA列表
USER_AGENTS = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10"
]
def get_header():
    return {
        'User-Agent': random.choice(USER_AGENTS),
    }





'''
    请求头设置
'''
# 爱信息图床，上传用时需要添加的请求头信息
update_header = {
'Origin':'https://tu.aixinxi.net',
'Referer':'https://tu.aixinxi.net/index.php',
}
# 爱信息图床，退出操作的头信息
loginOut_Header = {
    'cookie':'PHPSESSID=gb9b12bgkn4a8gv1mf2ur50ud3',
    'referer':'https://tu.aixinxi.net/index.php',
    'upgrade-insecure-requests':'1',
    'user-agent':random.choice(USER_AGENTS),
}
# 爱信息图床，删除操作的头信息
delete_header = {
'origin':'https://tu.aixinxi.net',
'referer':'https://tu.aixinxi.net/views/else.php?key=',
}
# 爱信息图床，保存时用请求头部
save_header = {
'origin':'https://tu.aixinxi.net',
'referer':'https://tu.aixinxi.net/index.php',
}
# 爱信息图床，token用请求头部
token_header = {
    'cache - control':'max-age=0',
    'referer':aixinxi_index_url,
}

# sm.ms，上传
sm_update_header = {
    'Host': 'sm.ms',
    'user-agent':random.choice(USER_AGENTS),
}
