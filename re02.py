# -*- coding:utf-8 -*-
# two equivalent matching regular expression to match float

import re

a=re.compile(r"""\d+ #the integral part
                  \. #the decimal point
                  \d* #some fractional digits""",re.X)

b=re.compile(r"\d+\.\d*")


match11=a.match('3.983.2')
match12=b.match('2.9832')
match21=a.match('314.')
match22=b.match('314')

if match11:
    print match11.group()
else:
    print u'match11 is not a decimal'


if match12:
    print match12.group()
else:
    print u'match12 is not a decimal'


if match21:
    print match21.group()
else:
    print u'match21 is not a decimal'

if match22:
    print match22.group()
else:
    print u'match22 is not a decimal'
