# -*- coding:utf-8 -*-
#---------------------------------
# Author: Nina Huo
# Date:2015-9-29
# Python2.7
# Function:download  all content within the corresponding page number and transform it to html format

import string,urllib2

#define the function to download web contents
def tieba_download(url,begin_page,end_page):
    for i in range(begin_page,end_page):
        sName=string.zfill(i,5)+'.html'
        print 'Downloading the'+str(i)+'th web page,and saving it as '+sName+'......'
        f=open(sName,'w+')
        response=urllib2.urlopen(url+str(i)).read()
        f.write(response)
        f.close()




#----------input the parameter------------
url=str(raw_input(u'please input the website without the number after pn=:\n'))
begin_page=int(raw_input(u'please input the begin page number:\n'))
end_page=int(raw_input(u'please input the end page number:\n'))

#run
tieba_download(url,begin_page,end_page)