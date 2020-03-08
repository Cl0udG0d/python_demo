#-*- coding:utf-8 -*-
from lxml import etree
import requests

base_url='http://ip.yqie.com/ip.aspx?ip='
filename='hello.txt'
file2name='address.txt'
f2=open(file2name,'a+')
with open(filename) as f:
    for line in f:
        line=line.strip()
        url=base_url+line
        rep=requests.get(url)
        html=etree.HTML(rep.text)
        content=html.xpath('//input[@class="displayno_address"]/@value')[0]
        content=line+" "+content+'\n'
        f2.write(content.encode("utf-8"))

f.close()
print "End!"
        

