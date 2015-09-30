# -*- coding:utf-8 -*-
#------------------------
# be familiar with the regular expression
# a simple re module example used to match 'hello' substring
# the using steps:
# 1. compile the string form of regular expression to Pattern instance
# 2. use the Pattern instance to process the text and get the matching result
# 3. use the matching result(Match instance)to get information

import re

#将正则表达式编译成Pattern对象，注意hello前面的r的意思是“原生字符串”
pattern=re.compile(r'hello')

#use patterm match text,if there is no matching substring,return None
match1=pattern.match('hello world!')
match2=pattern.match('helloo world!')
match3=pattern.match('helllo world!')

if match1:
    print match1.group()
else:
    print 'match1 failed'

if match2:
    print match2.group()
else:
    print 'match2 failed'

if match3:
    print match3.group()
else:
    print 'match3 failed'




