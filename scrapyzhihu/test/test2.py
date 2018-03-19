from copyheaders import headers_raw_to_dict
import requests
import json

post_headers_raw = '''
    accept:application/json, text/plain, */* 
    Accept-Encoding:gzip, deflate, br 
    Accept-Language:zh-CN,zh;q=0.9,zh-TW;q=0.8
    authorization:oauth c3cef7c66a1843f8b3a9e6a1e3160e20
    x-xsrftoken:2d9cfde4-374b-44c9-a89c-261df5aedf56
    Connection:keep-alive 
    DNT:1 
    Host:www.zhihu.com 
    Origin:https://www.zhihu.com 
    Referer:https://www.zhihu.com/signup?next=%2F 
    User-Agent:Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36 
'''

headers = headers_raw_to_dict(post_headers_raw)
cookies = {
    'capsion_ticket':'"2|1:0|10:1521370130|14:capsion_ticket|44:OGJhODYzOWM3NGM3NGE0ZmE1Yjg5NjZhOTZkZjhlODY=|3891bd8c49dd4674fc62c2d860f8b6d79479d235b221286dc94398fa29a1a2d7"'
}
captcha = requests.put('https://www.zhihu.com/api/v3/oauth/captcha?lang=en', headers=headers, cookies=cookies)
print captcha.json()
