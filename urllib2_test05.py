__author__ = 'sinsea'

#例3：把自身模拟成浏览器，创建一个请求对象时，包括一个包含头数据的字典，User_Agent
import urllib
import  urllib2

url="http://www.someserver.com/register.cgi"

user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.93 Safari/537.36'
values={
    'name':'NNH',
    'location':'XJ',
    'language':'Python'}
headers={'User-Agent',user_agent}
data=urllib.urlencode(values)
req=urllib2.Request(url,data,headers)
response=urllib2.urlopen(req)
the_page=response.read()
