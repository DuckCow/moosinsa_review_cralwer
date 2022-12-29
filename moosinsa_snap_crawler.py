import requests
import urllib.request
from bs4 import BeautifulSoup

import os
from urllib.request import urlretrieve

##이전 k값 저장
k=0

#snap = {brandsnap,streetsnap}
snap='streetsnap'
for page in range(1,20):

    webPage=requests.get("https://www.musinsa.com/mz/{}?_m=&gender=&p={}".format(snap,page))
    print(webPage)
    soup=BeautifulSoup(webPage.content,"html.parser")
    imgs=soup.select(".articleImg > a > img")

    ##### page_folder 파일경로
    path_folder = 'C:\image_crawling\{}\image'.format(snap)

    
    for i in imgs:
        k+=1
        src=i['src']
        print(src)

        ##street은  urlretrieve("https:"+src,path_folder+f'{k}.jpg')
        urlretrieve("https:"+src,path_folder+f'{k}.jpg')
    page+=1



    
