# -*- coding: utf-8 -*-


import httplib,urllib

httpClient = None

# 第一种请求方式
try:
    httpClient = httplib.HTTPConnection('localhost',90,timeout=30)
    httpClient.request('GET','/test')
    response = httpClient.getresponse()
    print(response.status)
    print(response.reason)
    print(response.read())
except Exception,e:
    print(e)
finally:
    if httpClient:
        httpClient.close()


# 第二种请求方式
try:
    params = urllib.urlencode({'name':'tao','age':18})
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    httpClient = httplib.HTTPConnection('localhost',90,timeout=30)
    response = httpClient.getresponse("POST","/test",params,headers)
    print response.status
    print response.reason
    print response.read()
    print response.getheaders() #获取头信息
except Exception,e:
    print(e)
finally:
    if httpClient:
        httpClient.close()