#与test02作用相同，先显式地创建对象Request，然后通过urlopen调用对象
import urllib2
req=urllib2.Request('http://www.baidu.com')
response=urllib2.urlopen(req)
the_page=response.read()
print the_page