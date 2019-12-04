import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time
import re
from urllib import parse
import csv


#时间转时间戳
def strToTimestamp(s, fmt):          
    return time.mktime(datetime.strptime(s, fmt).timetuple())

#时间戳转时间
def timeStamp2str(ts, fmt='%Y-%m'):
    return datetime.utcfromtimestamp(ts).strftime(fmt)

def getDetail(page = 1,keyword='%ca%dd%c8%e2%be%ab'):        #######改改改改改改改改改改
    time.sleep(8)
    print('page:' + str(page))
    #汉字转%A%B
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36"}
    # cookie = "JSESSIONID=59C33658A58E06C1699DC2400CE1AA0A; ALLYESID4=129ACF320C573171; sso_c=0; wdcid=439a1c6559042165; _people_ip_new_code=250000; _ma_tk=2nf64eeai55nblir9xab8ipdwbtzznei; _ma_starttm=1575175050817; sfr=1; _ma_is_new_u=0"
    res = requests.get(f'http://search.people.com.cn/cnpeople/search.do?pageNum={page}&keyword={keyword}&siteName=news&facetFlag=true&nodeType=belongsId&nodeId=0',headers=headers)
    try:
        content = res.content.decode('gbk')
        soup = BeautifulSoup(content,'html.parser')
    
    
        lis = soup.select('body > div.w980 > div.fr.w800 > ul > li:nth-child(3)')
        for li in lis:
            href = li.find('a').attrs.get('href')
            tm = re.search(r"\d{4}-\d{2}-\d{2}",li.text).group()
            # print(timeStamp2str)
            timeNum = strToTimestamp(tm, "%Y-%m-%d")
            print('正在爬取地址:' + href)
            
            
            #%S%B转汉字
            keyword = "瘦肉精"          #######改改改改改改改改改改
            sub_res = requests.get(href)
            sub_res.encoding = sub_res.apparent_encoding
            keyword = parse.unquote(keyword)
            pattern = re.compile(r'' + keyword)
            targets = pattern.findall(sub_res.text)
            lst.append({
                "timeNum": timeNum,
                "keyword": keyword,
                "keywordNum": len(targets),
                "url": href
            })
    except:
        print('捕获了一个异常, 跳过. 当前查询页为：' + str(page))

# 瘦肉精(%ca%dd%c8%e2%be%ab)：813 600开始           
lst = []
for i in range(400,450):        #最上方 600-610（没有标志）单纯瘦肉精
    #地沟油(%b5%d8%b9%b5%d3%cd)：725 
    # 农药残留(%c5%a9%d2%a9%b2%d0%c1%f4)：518   
    # 食品添加剂(%ca%b3%c6%b7%cc%ed%bc%d3%bc%c1）：11  
    # 
    # 禽流感(%c7%dd%c1%f7%b8%d0)：1906 
    # H1N1:235 
    # 疯牛病(%b7%e8%c5%a3%b2%a1）:61  
    # 转基因农产品(%d7%aa%bb%f9%d2%f2%c5%a9%b2%fa%c6%b7):57  
    # 化学物质残留(%bb%af%d1%a7%ce%ef%d6%ca%b2%d0%c1%f4):9 
    # 有毒有害食品(%d3%d0%b6%be%d3%d0%ba%a6%ca%b3%c6%b7):222
    # 农产品质量安全(%c5%a9%b2%fa%c6%b7%d6%ca%c1%bf%b0%b2%c8%ab):483
    
    getDetail( page= i + 1, keyword='%ca%dd%c8%e2%be%ab')           #######改
obj = {
                         #农药残留 20
}

for l in lst:
    ym = timeStamp2str(l.get('timeNum'))
    updateNum = obj.get(ym, 0) + l.get('keywordNum')
    
    obj[ym] = updateNum
print(obj)


with open("！！rmw-瘦肉精（300-450）.csv","a+",newline="") as f:       #改文件名字#######改改改改改改改改改改
    w = csv.DictWriter(f, obj.keys())
    w.writeheader()
    w.writerow(obj)



