# -*- coding:utf-8 -*-
# instance pattern's method and using example
# try to understand the difference between match and search
# match function checks whether the RegEx matches the string at the beginning
# search function scans the string and find if matched substring exists

import re

pattern=re.compile(r'world')

# 1. a match example
match=pattern.match('hello world!')

if match:
    print match.group()
else:
    print 'The string doesn\'t match the regular expression '

# 2.a search example
match=pattern.search('hello world!')
if match:
    print match.group()

# 3.a split function example
# Split the string according to the given re
p=re.compile(r'\d+')
print p.split('one12two23three34four45')

# 4.a findall example
# find all the matched substring in string
print p.findall('one12two23three34four45')

# 5.a finditer example
# traverse the string and return the iterator of matched substring(Match object) in order
for m in p.finditer('one12two23three34four45'):
    print m.group(),    # the comma is used to keep all the output in a line

# 6.a sub example
# sub function replaces the matched substring with repl
# then return the new string
p=re.compile(r'(\w+) (\w+)')
s='i say,i wanna be Gandalf'
print '\n',p.sub(r'\2 \1',s)

def func(m):
    return m.group(1).title()+' '+m.group(2).title()

print p.sub(func,s)


# 7.a subn example
# function subn return the (sub,count),count means the times of replacing
print p.subn(r'\2 \1',s)
print p.subn(func,s)
