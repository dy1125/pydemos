import requests
import json
from bs4 import BeautifulSoup
import re
from datetime import datetime
import time
import csv


#时间转时间戳
def strToTimestamp(s, fmt):          
    return time.mktime(datetime.strptime(s, fmt).timetuple())

#时间戳转时间
def timeStamp2str(ts, fmt='%Y-%m'):
    return datetime.utcfromtimestamp(ts).strftime(fmt)

lst = []    

#修改关键词：农药残留，食品添加剂超，地沟油，瘦肉精，禽流感，H1N1，疯牛病，转基因农产品，化学物质残留，有毒有害食品,农产品质量安全

url = "http://news.chinaso.com/newssearch.htm"

def getDetail(url, keyword='农药残留', page = 1):           
    print('curpage:' + str(page))

    # res = requests.get(f'{url}?q={keyword}&page={page}')  #模板
    res = requests.get(f'{url}?pageNum={page}&keyword={}&siteName=news&facetFlag=true&nodeType=belongsId&nodeId=0')
    content = res.content.decode('utf-8')
    soup = BeautifulSoup(content,'html.parser')
    seResult = soup.find(attrs={"class": "seResult"})
    if seResult is None:              #中新网有文章是表格，在此跳过
        return
    lis = seResult.find_all(attrs={"class": "reItem"})

    for li in lis:
        href = li.find('a').attrs.get('href')
        tm = li.find(class_="snapshot").text[0:10]     #时间获取
        timeNum = strToTimestamp(tm, "%Y-%m-%d")
        title = li.find('h2').text
        print('正在爬取地址:' + href)
        sub_res = requests.get(href)
        sub_res.encoding = sub_res.apparent_encoding
        pattern = re.compile(r'' + keyword)
        targets = pattern.findall(sub_res.text)
        lst.append({
            "title": title,
            "timeNum": timeNum,
            "keyword": keyword,
            "keywordNum": len(targets),
            "url": href
        })

url = "http://search.people.com.cn/cnpeople"
url = "http://news.chinaso.com/newssearch.htm"

for i in range(15):     
    #地沟油：5 农药残留：9 食品添加剂：11  瘦肉精：6 禽流感：5 H1N1:5 疯牛病:5  转基因农产品:4  化学物质残留:5 有毒有害食品:7 农产品质量安全:15
    getDetail(url, keyword='农药残留', page= i + 1)

obj = {

}

for l in lst:
    ym = timeStamp2str(l.get('timeNum'))
    updateNum = obj.get(ym, 0) + l.get('keywordNum')
    obj[ym] = updateNum

print(obj)

with open("rmw-农药残留.csv","a+",newline="") as f:       #改文件名字
    w = csv.DictWriter(f, obj.keys())
    w.writeheader()
    w.writerow(obj)

