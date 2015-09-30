#coding:utf-8
#urlopen返回的应答对象response/HTTPError实例中两个方法
#info()和geturl()

#info()返回对象的字典对象，该字典描述了获取的页面情况
#通常是服务器发送的特定头headers

from urllib2 import Request,urlopen,URLError,HTTPError

old_url='http://t.cn/RyCmtZI'

req=Request(old_url)
response=urlopen(req)
print 'Info():'
print response.info()