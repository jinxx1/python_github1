# coding=gbk
import re
import requests
url ='https://www.taobao.com/'

word1 =requests.get(url)
html=word1.content
try:
    word=str(html,'utf-8') #html_doc=html.decode("utf-8","ignore")
except:
    word=str(html,'gbk')
a = re.findall('>(.*?)</?',word,re.S | re.M)
for i in range(len(a)):
    if len(a[i].strip().replace('&nbsp;','').replace(' ',''))>0:
        wword = a[i].strip().replace('&nbsp;','').replace(' ','')
        chineseword = re.findall('^([\\u4e00-\\u9fa5]).*$',wword,re.S | re.M)
        if len(chineseword)>0:
            print(wword)