#coding:utf-8
# URLError在没有网络连接（没有路由到特定路由）或服务器不存在的情况下产生
# 异常的处理方式

import urllib2

req=urllib2.Request('http://www.baidiiii.com')

try:urllib2.urlopen(req)

except urllib2.URLError,e:
        print e.reason

