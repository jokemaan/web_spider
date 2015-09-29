#coding:utf-8
#处理HTTPError或者URLError异常的
#第2中方法

from urllib2 import Request,urlopen,HTTPError,URLError

req=Request('http://www.cnblogs.com/sherPur')

try:
    response=urlopen(req)
except URLError,e:
    if hasattr(e,'code'):
        print 'The server couldn\'t fulfill the request.'
        print 'Error code: ',e.code
    elif hasattr(e,'reason'):
        print 'We failed to reach a server.'
        print 'Reason:',e.reason

else:
    print 'No exception was raised'
