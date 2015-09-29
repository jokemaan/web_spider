# -*- coding:utf-8 -*-
#urllib2默认使用环境变量http_proxy来设置HTTPProxy
#如果想在程序中明确控制proxy而不受环境变量的影响，可使用代理

import urllib2
enable_proxy=True

proxy_handler=urllib2.ProxyHandler({"http":'http://some-proxy.com:8080'})
null_proxy_handler=urllib2.ProxyHandler({})
if enable_proxy:
    opener=urllib2.build_opener(proxy_handler)
else:
    opener=urllib2.build_opener(null_proxy_handler)

urllib2.install_opener(opener)

#注意，使用urllib2.install_opener()会设置urllib2的全局opener，这样不能做到细粒度的控制，比如像在程序中使用两个不同的proxy设置等
#比较好的做法是不适应install_opener去更改全局设置，只是直接调用opener的open方法代替urlopen方法
