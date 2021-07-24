from urllib import request, parse

# url = 'http://httpbin.org/get'
# parms = {
#     'name1': 'value1',
#     'name2': 'value2'
# }
# querystring = parse.urlencode(parms)
# u = request.urlopen(url + '?' + querystring)
# resp = u.read()


# url = 'http://httpbin.org/get'
# parms = {
#     'name1': 'value1',
#     'name2': 'value2'
# }
# querystring = parse.urlencode(parms)
# u = request.urlopen(url, querystring.encode('ascii'))
# resp = u.read()


# url = 'http://httpbin.org/get'
# headers = {
#     'User-agent': 'none/ofyourbusiness',
#     'Spam': 'Eggs'
# }
# parms = {
#     'name1': 'value1',
#     'name2': 'value2'
# }
# querystring = parse.urlencode(parms)
# req = request.Request(url, querystring.encode('ascii'), headers=headers)
# u = request.urlopen(req)
# resp = u.read()
# print(resp)
# import requests as requests
#
# resp = requests.head('http://www.python.org/index.html')
# status = resp.status_code
# last_modified = resp.headers['last-modified']
# content_type = resp.headers['content-type']
# content_length = resp.headers['content-length']
# print(status)
# print(last_modified)
# print(content_type)
# print(content_length)


# import requests
#
# url = 'http://httpbin.org/get'
# resp = requests.get(url)
# resp2 = requests.get(url, cookies=resp.cookies)  # 将第一个请求得到的HTTPcookies传递给下一个请求
# files = {'file': ('data.csv', open('data.csv', 'rb'))}  # 实现内容的上传
# r = requests.post(url, files=files)

# ------------------------------------------------------------------------------------------
# 底层
# from http.client import HTTPConnection
# from urllib import parse
#
# c = HTTPConnection('www.python.org', 80)
# c.request('HEAD', '/index.html')
# resp = c.getresponse()
# print(resp.status)
# for name, value in resp.getheaders():
#     print(name, value)

import urllib.request

auth = urllib.request.HTTPBasicAuthHandler()
auth.add_password('pypi', 'http://pypi.python.org', 'username', 'password')
opener = urllib.request.build_opener(auth)
r = urllib.request.Request('http://pypi.python.org/pypi?:action=login')
u = opener.open(r)
resp = u.read()
