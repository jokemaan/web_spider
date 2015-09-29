#一个简单地例子，说明urllib2库的使用

import urllib2
response=urllib2.urlopen('http://www.baidu.com/')
html=response.read()
print html