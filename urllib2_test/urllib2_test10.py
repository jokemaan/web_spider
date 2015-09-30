#coding:utf-8
#urlopen返回的应答对象response/HTTPError实例中两个方法
#info()和geturl()

#geturl()返回获取的真实URL，因为在urlopen中可能出现重定向

from urllib2 import  urlopen,Request,URLError,HTTPError

old_url='http://t.cn/RyCmtZI'

req=Request(old_url)
response=urlopen(req)
print 'old url:'+old_url
print 'real url:'+response.geturl()