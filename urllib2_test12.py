# -*- coding:utf-8 -*-
# Opener和Handler的使用
# 使用opener获取url，默认opener是urlopen，可以创建自定义openers
# openers使用处理器handlers，
# 实现基本认证，创建和安装一个handler

import urllib2

# 创建一个密码管理者
password_mgr=urllib2.HTTPPasswordMgrWithDefaultRealm()

# 添加用户名和密码
top_level_url='http://example.com/foo'

# 如果知道realm，可以用它代替 ‘None’
# password_mgr.addpassword(None,top_level_url,username,password)
password_mgr.add_password(None,top_level_url,'sherpur','123456')

# 创建一个新的handler
handler=urllib2.HTTPBasicAuthHandler(password_mgr)

# 创建“opener”（OpenDirector实例）
opener=urllib2.build_opener(handler)

a_url='http://www.baidu.com/'

#使用opener获取一个url
opener.open(a_url)

#安装opener
#现在所有调用urllib2.urlopen将使用我们定义的opener
urllib2.install_opener(opener)