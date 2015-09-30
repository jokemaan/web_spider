#例2：data通过Get请求的url本身编码来传送
import urllib2
import urllib

data={}

data['name']='NNH'
data['location']='XJ'
data['language']='Python'

url_values=urllib.urlencode(data)
print url_values

url='http://www.example.com/example.cgi'
full_url=url+'?'+url_values

data=urllib2.urlopen(full_url)