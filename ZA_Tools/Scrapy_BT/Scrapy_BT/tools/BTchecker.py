import requests

URL = 'http://tools.bugscaner.com/api/magnetspeed/'

FormData = {
'magnet':'magnet:?xt=urn:btih:c7401de1b1b6d385bd7bcac2f1cb5ea46b626935',
}

_header = {
    'Host':'tools.bugscaner.com',
    'Origin':'http://tools.bugscaner.com',
    'Referer':'http://tools.bugscaner.com/magnetspeed/',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
}

def BTchecker(URL,FormData,_header):
    _respone = requests.post(url=URL,data=FormData,headers=_header)
    _respone.encoding = 'unicode_escape'
    print(_respone.text)

if __name__ == '__main__':
    BTchecker(URL,FormData,_header)