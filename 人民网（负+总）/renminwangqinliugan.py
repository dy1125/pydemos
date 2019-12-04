import requests
import json
from bs4 import BeautifulSoup


#获得列表页下的所有子页面链接
def get_urls(url):
    header = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36"}
    res = requests.get(url,headers = header)
    r = res.content.decode()  #得到的数据类型为字符串
    Dict = json.loads(r)
    results = Dict["content"]["results"]      #换网站则换该行#、
    urls = []
    for result in results:
        if not result is None: 
	        urls.append(result["url"])
    return urls

def getContent(mainContent):


    
    
    

    soup = BeautifulSoup(mainContent,"html.parser")
    pss = soup.select("div #rwb_zw")
    date = soup.select(".f1")
    if  pss and date:
        print("==类型:  div #rwb_zw  .f1")
        return pss,date

    soup = BeautifulSoup(mainContent,"html.parser")
   pss = soup.select("div #rwb_zw")
    date = soup.select(".f1")
    if  pss and date:
        print("==类型:  div #rwb_zw  .f1")
        return pss,date

    soup = BeautifulSoup(mainContent,"html.parser")
    pss = soup.select(".artDet")
    date = soup.select(".artOri")
    if  pss and date:
        print("==类型: .artDet  .artOri")
        return pss,date
    
    soup = BeautifulSoup(mainContent,"html.parser")
   pss = soup.select("div #rwb_zw")
    date = soup.select(".f1")
    if  pss and date:
        print("==类型:  div #rwb_zw  .f1")
        return pss,date

    soup = BeautifulSoup(mainContent,"html.parser")
    pss = soup.select("div #rwb_zw")
    date = soup.select(".f1")
    if  pss and date:
        print("==类型:  div #rwb_zw  .f1")
        return pss,date
    
    soup = BeautifulSoup(mainContent,"html.parser")
    pss = soup.select(".artDet")
    date = soup.select(".artOri")
    if  pss and date:
        print("==类型: .artDet  .artOri")
        return pss,date

    soup = BeautifulSoup(mainContent,"html.parser")
   pss = soup.select("div #rwb_zw")
    date = soup.select(".f1")
    if  pss and date:
        print("==类型:  div #rwb_zw  .f1")
        return pss,date

    soup = BeautifulSoup(mainContent,"html.parser")
    pss = soup.select("div #rwb_zw")
    date = soup.select(".f1")
    if  pss and date:
        print("==类型:  div #rwb_zw  .f1")
        return pss,date
   
    soup = BeautifulSoup(mainContent,"html.parser")
    pss = soup.select("div #rwb_zw")
    date = soup.select(".f1")
    if  pss and date:
        print("==类型:  div #rwb_zw  .f1")
        return pss,date
    
   
    
    soup = BeautifulSoup(mainContent,"html.parser")
    pss = soup.select("div #rwb_zw")
    date = soup.select(".f1")
    if  pss and date:
        print("==类型:  div #rwb_zw  .f1")
        return pss,date  
    
    
    
    soup = BeautifulSoup(mainContent,"html.parser")
    pss = soup.select("div #rwb_zw")
    date = soup.select(".f1")
    if  pss and date:
        print("==类型:  div #rwb_zw  .f1")
        return pss,date

     soup = BeautifulSoup(mainContent,"html.parser")
    pss = soup.select("div #rwb_zw")
    date = soup.select(".f1")
    if  pss and date:
        print("==类型:  div #rwb_zw  .f1")
        return pss,date

      soup = BeautifulSoup(mainContent,"html.parser")
    pss = soup.select(".artDet")
    date = soup.select(".artOri")
    if  pss and date:
        print("==类型: .artDet  .artOri")
        return pss,date
     
     soup = BeautifulSoup(mainContent,"html.parser")
    pss = soup.select("div #rwb_zw")
    date = soup.select(".f1")
    if  pss and date:
        print("==类型:  div #rwb_zw  .f1")
        return pss,date
    
    
    soup = BeautifulSoup(mainContent,"html.parser")
    pss = soup.select("div #rwb_zw")
    date = soup.select(".f1")
    if  pss and date:
        print("==类型:  div #rwb_zw  .f1")
        return pss,date    
    
    soup = BeautifulSoup(mainContent,"html.parser")
    pss = soup.select(".show_text")
    date = soup.select(".sou")
    if  pss and date:
        print("==类型:  .show_text   .sou")
        return pss,date
    

    soup = BeautifulSoup(mainContent,"html.parser")
   pss = soup.select("div #rwb_zw")
    date = soup.select(".f1")
    if  pss and date:
        print("==类型:  div #rwb_zw  .f1")
        return pss,date   
    
    
      soup = BeautifulSoup(mainContent,"html.parser")
    pss = soup.select(".artDet")
    date = soup.select(".artOri")
    if  pss and date:
        print("==类型: .artDet  .artOri")
        return pss,date
     
     soup = BeautifulSoup(mainContent,"html.parser")
   pss = soup.select("div #rwb_zw")
    date = soup.select(".f1")
    if  pss and date:
        print("==类型:  div #rwb_zw  .f1")
        return pss,date   

      soup = BeautifulSoup(mainContent,"html.parser")
    pss = soup.select(".show_text")
    date = soup.select(".sou")
    if  pss and date:
        print("==类型:  .show_text   .sou")
        return pss,date
     
     soup = BeautifulSoup(mainContent,"html.parser")
    pss = soup.select(".show_text")
    date = soup.select(".sou")
    if  pss and date:
        print("==类型:  .show_text   .sou")
        return pss,date
    
    soup = BeautifulSoup(mainContent,"html.parser")
   pss = soup.select("div #rwb_zw")
    date = soup.select(".f1")
    if  pss and date:
        print("==类型:  div #rwb_zw  .f1")
        return pss,date   

     soup = BeautifulSoup(mainContent,"html.parser")
   pss = soup.select("div #rwb_zw")
    date = soup.select(".f1")
    if  pss and date:
        print("==类型:  div #rwb_zw  .f1")
        return pss,date   

     soup = BeautifulSoup(mainContent,"html.parser")
   pss = soup.select("div #rwb_zw")
    date = soup.select(".f1")
    if  pss and date:
        print("==类型:  div #rwb_zw  .f1")
        return pss,date  

   soup = BeautifulSoup(mainContent,"html.parser")
    pss = soup.select(".show_text")
    date = soup.select(".sou")
    if  pss and date:
        print("==类型:  .show_text   .sou")
        return pss,date
    
     soup = BeautifulSoup(mainContent,"html.parser")
   pss = soup.select(".artDet")
    date = soup.select(".artOri")
    if  pss and date:
        print("==类型: .artDet  .artOri")
        return pss,date

    soup = BeautifulSoup(mainContent,"html.parser")
   pss = soup.select(".content clear clearfix")
    date = soup.select(".fr")
    if  pss and date:
        print("==类型:  .content clear clearfix  .fr")
        return pss,date   

    soup = BeautifulSoup(mainContent,"html.parser")
   pss = soup.select(".artDet")
    date = soup.select(".artOri")
    if  pss and date:
        print("==类型: .artDet  .artOri")
        return pss,date

   soup = BeautifulSoup(mainContent,"html.parser")
   pss = soup.select("div #rwb_zw")
    date = soup.select(".f1")
    if  pss and date:
        print("==类型:  div #rwb_zw  .f1")
        return pss,date  

    
    soup = BeautifulSoup(mainContent,"html.parser")
   pss = soup.select(".artDet")
    date = soup.select(".artOri")
    if  pss and date:
        print("==类型: .artDet  .artOri")
        return pss,date
    
    soup = BeautifulSoup(mainContent,"html.parser")
   pss = soup.select("div #rwb_zw")
    date = soup.select(".f1")
    if  pss and date:
        print("==类型:  div #rwb_zw  .f1")
        return pss,date  

    soup = BeautifulSoup(mainContent,"html.parser")
   pss = soup.select("div #rwb_zw")
    date = soup.select(".f1")
    if  pss and date:
        print("==类型:  div #rwb_zw  .f1")
        return pss,date 

     
    soup = BeautifulSoup(mainContent,"html.parser")
   pss = soup.select(".artDet")
    date = soup.select(".artOri")
    if  pss and date:
        print("==类型: .artDet  .artOri")
        return pss,date
    
    soup = BeautifulSoup(mainContent,"html.parser")
   pss = soup.select("div #rwb_zw")
    date = soup.select(".f1")
    if  pss and date:
        print("==类型:  div #rwb_zw  .f1")
        return pss,date  

   
    
    soup = BeautifulSoup(mainContent,"html.parser")
   pss = soup.select("div #rwb_zw")
    date = soup.select(".f1")
    if  pss and date:
        print("==类型:  div #rwb_zw  .f1")
        return pss,date  

     soup = BeautifulSoup(mainContent,"html.parser")
   pss = soup.select("div #rwb_zw")
    date = soup.select(".f1")
    if  pss and date:
        print("==类型:  div #rwb_zw  .f1")
        return pss,date  

     soup = BeautifulSoup(mainContent,"html.parser")
   pss = soup.select("div #rwb_zw")
    date = soup.select(".f1")
    if  pss and date:
        print("==类型:  div #rwb_zw  .f1")
        return pss,date  

     soup = BeautifulSoup(mainContent,"html.parser")
   pss = soup.select("div #rwb_zw")
    date = soup.select(".f1")
    if  pss and date:
        print("==类型:  div #rwb_zw  .f1")
        return pss,date  

    soup = BeautifulSoup(mainContent,"html.parser")
    pss = soup.select(".show_text")
    date = soup.select(".sou")
    if  pss and date:
        print("==类型:  .show_text   .sou")
        return pss,date

    soup = BeautifulSoup(mainContent,"html.parser")
   pss = soup.select("div #rwb_zw")
    date = soup.select(".f1")
    if  pss and date:
        print("==类型:  div #rwb_zw  .f1")
        return pss,date  

    soup = BeautifulSoup(mainContent,"html.parser")
   pss = soup.select("div #rwb_zw")
    date = soup.select(".f1")
    if  pss and date:
        print("==类型:  div #rwb_zw  .f1")
        return pss,date  
    
#每篇文章写入txt
def article(art_url):
    print(art_url)
    cookies= "uid=c873acc8280a4409a9ad44eafafce029; wdcid=6bb163e2b34014d3; xh_regionalNews_v1=13; bdshare_firstime=1574331446644; bfdid=87205254007bf95200005f8002e5a25c5dd666a8; tmc=12.182794287.10720504.1574667333495.1574671801910.1574672051444; tma=182794287.96771765.1574332076531.1574469994917.1574660120719.4; tmd=23.182794287.96771765.1574332076531.; fingerprint=ddecc36df63e1d64a4a58ce8c96f6f99; bfd_s=180312445.865550830237583.1574667333505; bfd_g=87205254007bf95200005f8002e5a25c5dd666a8; cc=3d8273f3ea67d9dd55d855e08aef3bf0; pc=01a28a0071312ba4194ab4a565ddc403.1574325829.1574671048.10; wdlast=1574672220"
    header = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36"}
    response = requests.get(art_url,headers=header)
    
    response.encoding = "utf-8"
    pss = getContent(response.text)
   
  
    with open("人民网禽流感.txt","a+",encoding="utf-8") as file:     #####改名字：一个网站加一个词
	    file.write(str(pss)+"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")    


for page_number in range(1,5):   #所有负面词列表页999页   #####改页数：人民网共28594篇，每页20篇
    urll = "http://so.news.cn/getNews?keyWordAll=&keyWordOne=%25E5%2586%259C%25E8%258D%25AF%25E6%25AE%258B%25E7%2595%2599%25EF%25BC%258C%25E9%25A3%259F%25E5%2593%2581%25E6%25B7%25BB%25E5%258A%25A0%25E5%2589%2582%25E8%25B6%2585%25EF%25BC%258C%25E6%25AF%2592%25E5%25A5%25B6%25E7%25B2%2589%25EF%25BC%258C%25E5%259C%25B0%25E6%25B2%259F%25E6%25B2%25B9%25EF%25BC%258C%25E7%2598%25A6%25E8%2582%2589%25E7%25B2%25BE%25EF%25BC%258C%25E4%25B8%2589%25E8%2581%259A%25E6%25B0%25B0%25E8%2583%25BA%25EF%25BC%258C%25E7%25A6%25BD%25E6%25B5%2581%25E6%2584%259F%25EF%25BC%258CH1N1%25EF%25BC%258C%25E7%2596%25AF%25E7%2589%259B%25E7%2597%2585%25EF%25BC%258C%25E8%25BD%25AC%25E5%259F%25BA%25E5%259B%25A0%25E5%2586%259C%25E4%25BA%25A7%25E5%2593%2581%25EF%25BC%258C%25E5%258C%2596%25E5%25AD%25A6%25E7%2589%25A9%25E8%25B4%25A8%25E6%25AE%258B%25E7%2595%2599%25EF%25BC%258C%25E6%259C%2589%25E6%25AF%2592%25E6%259C%2589%25E5%25AE%25B3%25E9%25A3%259F%25E5%2593%2581%25EF%25BC%258C%25E9%2595%2589%25E5%25A4%25A7%25E7%25B1%25B3&keyWordIg=&searchFields=0&sortField=0&url=&senSearch=1&lang=cn&keyword=%E5%86%9C%E8%8D%AF%E6%AE%8B%E7%95%99%EF%BC%8C%E9%A3%9F%E5%93%81%E6%B7%BB%E5%8A%A0%E5%89%82%E8%B6%85%EF%BC%8C%E6%AF%92%E5%A5%B6%E7%B2%89%EF%BC%8C%E5%9C%B0%E6%B2%9F%E6%B2%B9%EF%BC%8C%E7%98%A6%E8%82%89%E7%B2%BE%EF%BC%8C%E4%B8%89%E8%81%9A%E6%B0%B0%E8%83%BA%EF%BC%8C%E7%A6%BD%E6%B5%81%E6%84%9F%EF%BC%8CH1N1%EF%BC%8C%E7%96%AF%E7%89%9B%E7%97%85%EF%BC%8C%E8%BD%AC%E5%9F%BA%E5%9B%A0%E5%86%9C%E4%BA%A7%E5%93%81%EF%BC%8C%E5%8C%96%E5%AD%A6%E7%89%A9%E8%B4%A8%E6%AE%8B%E7%95%99%EF%BC%8C%E6%9C%89%E6%AF%92%E6%9C%89%E5%AE%B3%E9%A3%9F%E5%93%81%EF%BC%8C%E9%95%89%E5%A4%A7%E7%B1%B3&curPage={}".format(page_number)
     ##########改网址：关键词网址：把12页不同的地方改成{}
    #print(urll)
    print(page_number)
    urls = get_urls(urll)
    for ulz in urls:
	    article(ulz)



