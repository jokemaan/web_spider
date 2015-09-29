#coding:utf-8
#处理HTTPError或者URLError的方法
#第1种方法

from urllib2 import Request,urlopen,URLError,HTTPError

req=Request('http://www.cnblogs.com/sherPur23')

try:
    response=urlopen(req)

except HTTPError,e:
    print 'The server coundn\'t fulfill the request.'
    print 'Error code:',e.code

except URLError,e:
    print 'We failed th reach a server'
    print 'Reason:',e.reason

else:
    print 'No exception was raised'

