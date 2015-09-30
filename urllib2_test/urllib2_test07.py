#coding:utf-8
#当一个错误号产生后，服务器返回一个HTTP错误号，和一个错误页面
#使用HTTPError实例作为页面返回的应答对象response

import urllib2

req=urllib2.Request('http://www.cnblogs.com/sherPur23')

try:
    urllib2.urlopen(req)

except  urllib2.URLError,e:
        print e.code
