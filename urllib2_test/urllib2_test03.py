#例1：发送data表单数据，通过POST发送

import urllib
import urllib2

url="http://www.someserver.com/register.cgi"

values={
    'name':'NNH',
    'location':'XJ',
    'language':'Python'}

data=urllib.urlencode(values) #编码工作
req=urllib2.Request(url,data) #发送请求同时传data表单
response=urllib2.urlopen(req) #接收反馈的消息
the_page=response.read() #读取反馈的消息
