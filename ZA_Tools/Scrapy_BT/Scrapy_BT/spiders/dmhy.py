# -*- coding: utf-8 -*-
import scrapy,re,chardet
# import Scrapy_BT.Scrapy_BT.tools.test
from Scrapy_BT.items import dmhyItem

class DmhySpider(scrapy.Spider):
    '''
    流程： 首先向start_urls地址发送请求，得到的response都会返回到函数parse,通过选择器抓取响应的内容，然后再获取下一页的地址，发送请求。
    '''
    name = "dmhy"
    allowed_domains = ["share.dmhy.org"]
    start_urls = ['https://share.dmhy.org']

    re_infoURL = '<ahref="/topics/view/([\s\S]*?)"target="_blank">'
    re_time = '<li>發佈時間:<span>([\s\S]*?)</span></li>'
    re_type = '<tdwidth="6%"align="center"><aclass="([\s\S]*?)"href="'
    re_title = '<divclass="topic-titleboxui-corner-all"><h3>([\s\S]*?)</h3>'
    re_size = '<li>文件大小:<span>([\s\S]*?)</span></li>'
    re_info = '<strong>簡介:&nbsp;</strong>([\s\S]*?)<a name="description-end"></a>'
    re_magnet1 = '<aclass="magnet"id="a_magnet"href="([\s\S]*?)">([\s\S]*?)</a>'
    re_magnet2 = '<aid="magnet2"href="([\s\S]*?)">([\s\S]*?)</a>'


    def parse(self, response):
        a_i_u_e_o = response.text
        ha_hi_fu_he_ho = list(map(lambda x: self.getDMHY_types('viewInfoURL') + x, self.re_DMHY(a_i_u_e_o, self.re_infoURL)))
        sa_shi_su_se_so = self.re_DMHY(a_i_u_e_o, self.re_type)
        for ma_mi_mu_me_mo, na_ni_nu_ne_no in zip(ha_hi_fu_he_ho, sa_shi_su_se_so):
            rec_dict = {
                '类别': self.getDMHY_types(na_ni_nu_ne_no),
                '标题': '',
                '发布时间': '',
                '文件大小': '',
                'Magnet連接': '',
                'Magnet連接typeII': '',
                '简介': r'<div>\r\n' + '',
                '详情URL': ma_mi_mu_me_mo,
            }
            yield scrapy.Request(url=rec_dict["详情URL"], callback=self.infoView, meta={"item": rec_dict})
        _next = response.css('.nav_title .fl a::attr("href")').extract()
        # 采集下一页的地址，如果有两个元素说明为存在上下页地址
        if len(_next) == 2 :
            _next = _next[1] # 第二个元素必为下一页地址
        else:
            if response.url == 'https://share.dmhy.org':
                _next = _next[0]
            # 当前url和next的URL的尾数字是否相同
            else:
                if int(response.url.split('/')[-1]) >= int(_next[0].split('/')[-1]):
                    # 爬取到底页，回到页首
                    _next = 'https://www.dmhy.org'

        print(_next)
        url = response.urljoin(_next)
        # yield scrapy.Request(url=url,callback=self.parse,dont_filter=False)

    def update_parse(self,response):
        pass

    def infoView(self, response):
        rec_dict_temp = {
            '标题':self.re_DMHY(response.text, self.re_title)[0],
            '发布时间':self.re_DMHY(response.text, self.re_time)[0],
            '文件大小':self.re_DMHY(response.text, self.re_size)[0],
            'Magnet連接':list(self.re_DMHY(response.text, self.re_magnet1)[0]),
            'Magnet連接typeII':list(self.re_DMHY(response.text, self.re_magnet2)[0]),
            '简介':r'<div>\r\n'+self.re_DMHY(response.text, self.re_info,False)[0],
        }
        z = {**response.meta["item"],**rec_dict_temp} # py3.5新语法，合并更新字典
        item = dmhyItem()
        item['rdName'] = z['标题']
        item['rdUpTime'] = z['发布时间']
        item['rdSize'] = z['文件大小']
        item['rdUpNum'] = z['文件大小']
        item['rdDownloadNum'] = z['文件大小']
        item['rdInfo'] = z['简介']
        item['rdOK'] = z['文件大小']
        item['rdMagnet'] = z['Magnet連接'][1]
        item['rdMagnet2'] = z['Magnet連接typeII'][0]
        item['rdTracker'] =z['Magnet連接'][0][len(z['Magnet連接'][1]):]
        item['rdType'] = z['类别']
        item['rdView'] = z['详情URL']


    def getDMHY_types(self, _str):
        '''
        动漫花园资源类别转换
        :param _str: 字符串，传入类似“sort-2”即可
        :return: 字符串
        '''
        types = {
            'sort-2': '动画',
            'sort-31': '季度全集',
            'sort-3': '漫画',
            'sort-41': '港台漫画',
            'sort-42': '日版漫画',
            'sort-4': '音乐',
            'sort-43': '动漫音乐',
            'sort-44': '同人音乐',
            'sort-15': '流行音乐',
            'sort-6': '日剧',
            'sort-7': '生肉（RAW）',
            'sort-9': '游戏',
            'sort-17': '电脑游戏',
            'sort-18': '电视游戏',
            'sort-19': '掌机游戏',
            'sort-20': '网络游戏',
            'sort-21': '游戏周边',
            'sort-12': '特摄',
            'sort-1': '其他',
            'viewInfoURL': 'https://share.dmhy.org/topics/view/',
        }
        return types[_str]

    def re_DMHY(self,html_text, re_pattern, nbsp_del=True):
        '''
        增则过滤函数
        :param html_text: 字符串，网页的文本
        :param re_pattern: 字符串，正则表达式
        :param nbsp_del: 布尔值，控制是否以去除换行符的形式抓取有用信息
        :return:
        '''
        pattern = re.compile(re_pattern)
        if nbsp_del:
            return pattern.findall("".join(html_text.split()))
        else:
            return pattern.findall(html_text)