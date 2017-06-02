#coding=UTF-8

# 功能:在命令行中查询单词在有道词典网页版中的柯林斯释义
# 使用方法: `python3 dict.py word`
# 或 `alias di='python3 dict.py'` ,然后就可以直接 `di word` 查询单词了

import urllib.request
from bs4 import BeautifulSoup
import re
import sys

url = "http://dict.youdao.com/w/eng/"
word = sys.argv[1]
url = url + word
pagedata = urllib.request.urlopen(url).read()        #获取该单词网页的源代码
pagedata = pagedata.decode('UTF-8')
contentall = BeautifulSoup(pagedata,'lxml')
yy = contentall.find(class_ = "trans-content")

ss = re.sub('\s\s+', ' ', str(yy))
ss = re.sub('\s?</?b>\s?', ' ', ss)
ss = re.sub('<span.*?"title">(.*?)<.*?>', r'@@@\1 ', ss)
ss = re.sub('\s?<.*?>\s?', ' ', ss)
ss = re.sub('\n\n+', '\n', ss)
ss = re.sub('\s\s+', ' ', ss)
ss = re.sub('\s?(\d?\d\.)', r'\n\1', ss)
ss = re.sub('@@@', '\n========================================\n', ss)
ss = re.sub('\s?例[：|:]\s*', '\n\t例: ', ss)
ss = ss.strip()
print(ss)
