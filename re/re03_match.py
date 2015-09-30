# -*- coding:utf-8 -*-
# a simple Function match instance

import re

#matching rules: word + spacing + word + random characters
m=re.match(r'(\w+) (\w+)(?P<sign>.*)','hello world!')

print "m.stirng:",m.string
print "m.re:",m.re
print "m.pos",m.pos
print "m.endpos:",m.endpos
print "m.lastindex:",m.lastindex
print "m.lastgroup:",m.lastgroup

print "m.group():",m.group()
print "m.group(1,2):",m.group(1,2)
print "m.groups():",m.groups()
print "m.groupdict():",m.groupdict()
print "m.start(2):",m.start(2)
print "m.end(2):",m.end(2)
print "m.span(2):",m.span(2)
print r"m.expand(r'\g<2> \g<1>\g<3>'):",m.expand(r'\2 \1\3')

### The Output as follows ###
# m.stirng: hello world!
# m.re: <_sre.SRE_Pattern object at 0x10db768b0>
# m.pos 0
# m.endpos: 12
# m.lastindex: 3
# m.lastgroup: sign
# m.group(): hello world!
# m.group(1,2): ('hello', 'world')
# m.groups(): ('hello', 'world', '!')
# m.groupdict(): {'sign': '!'}
# m.start(2): 6
# m.end(2): 11
# m.span(2): (6, 11)
# m.expand(r'\g<2> \g<1>\g<3>'): world hello!
