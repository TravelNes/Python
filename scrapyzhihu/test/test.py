# coding=utf-8
import requests
import re
import time
import execjs
from requests_toolbelt.multipart.encoder import MultipartEncoder
from copyheaders import headers_raw_to_dict
import json


post_headers_raw = '''
    accept:application/json, text/plain, */* 
    Accept-Encoding:gzip, deflate, br 
    Accept-Language:zh-CN,zh;q=0.9,zh-TW;q=0.8
    authorization:oauth c3cef7c66a1843f8b3a9e6a1e3160e20 
    Connection:keep-alive 
    DNT:1 
    Host:www.zhihu.com 
    Origin:https://www.zhihu.com 
    Referer:https://www.zhihu.com/signup?next=%2F 
    User-Agent:Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36 
'''


class ZhiHu():
    def __init__(self):
        self.session = requests.session()

        self.session.headers = {
            'Host':	'www.zhihu.com',
            'Referer': 'https://www.zhihu.com/signup?next=%2F',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:58.0) Gecko/20100101 Firefox/58.0'
        }
        # cookiejar = cookielib.LWPCookieJar()
        # cookiejar.load('cookie.txt')
        # self.session.cookies = cookiejar
        pass

    def post_headers(self):
        response = self.session.get('https://www.zhihu.com', verify=False)
        xsrf = response.headers['Set-Cookie'].split('=')[1][:-6]
        pattern = re.compile('xUDID&quot;:&quot;(.*?)&quot;')
        xudid = re.findall(pattern, response.text)[0]
        headers = headers_raw_to_dict(post_headers_raw)
        headers['authorization'] = 'oauth c3cef7c66a1843f8b3a9e6a1e3160e20'
        headers['X-UDID'] = xudid
        headers['X-Xsrftoken'] = xsrf
        return headers

    @staticmethod
    def post_data(username, password, captcha=''):
        timestamp = int(time.time() * 1000)
        jsfile = open('jstest.js', 'r').read()
        ec = execjs.compile(jsfile)
        signature = ec.call('run', 'password', timestamp)
        postdata = {
            'client_id': 'c3cef7c66a1843f8b3a9e6a1e3160e20',
            'grant_type': 'password',
            'timestamp': str(timestamp),
            'source': 'com.zhihu.web',
            'signature': signature,
            'username': username,
            'password': password,
            'lang': 'cn',
            'captcha': captcha,
            'ref_source': 'homepage',
            'utm_source': ''
        }
        return postdata

    def check_captcha(self, headers, cn=True):
        if cn:
            url = 'https://www.zhihu.com/api/v3/oauth/captcha?lang=cn'
        else:
            url = 'https://www.zhihu.com/api/v3/oauth/captcha?lang=en'
        z = self.session.get(url, headers=headers)
        show_captcha = json.loads(z.text)['show_captcha']
        if show_captcha:
            print z.text
        else:
            captcha = ''
        print z.json()
        return z.json()

    def login(self):
        username = ''
        password = ''
        post_data = self.post_data(username, password)
        post_headers = self.post_headers()
        self.check_captcha(post_headers)
        encoder = MultipartEncoder(post_data, boundary='----WebKitFormBoundarycGPN1xiTi2hCSKKZ')
        post_headers['Content-Type'] = encoder.content_type
        pages = self.session.post('https://www.zhihu.com/api/v3/oauth/sign_in', data=encoder,
                                  headers=post_headers, verify=False)
        self.check_login(pages)

    def check_login(self, response):
        headers = {
            'Host': 'www.zhihu.com',
            'Referer': 'https://www.zhihu.com/signup?next=%2F',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:58.0) Gecko/20100101 Firefox/58.0'
        }
        page = self.session.get('https://www.zhihu.com', headers=headers)
        with open('index.html', 'w') as f:
            f.write(page.text.encode('utf-8'))


ZhiHu().login()
