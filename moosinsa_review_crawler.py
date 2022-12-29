import requests
import urllib.request
from bs4 import BeautifulSoup

import os
from urllib.request import urlretrieve

##이전 k값 저장
k=0

#review={photo,style}
review='photo'
real_p=30
for page in range(1,30):

    real_p=30-page
    webPage=requests.get("https://store.musinsa.com/app/reviews/lists?type={}&year_date=2022&month_date=&day_date=&max_rt=2022&min_rt=2009&brand=&page={}&sort=new&hash_id=&best_type=&s_type=all&q=".format(review,real_p), headers={'User-Agent': 'Mozilla/5.0'})
    #print(webPage)
    soup=BeautifulSoup(webPage.content,"html.parser")
    imgs=soup.select(".review-content-photo__item > img")
    

    ##### page_folder 파일경로
    path_folder = 'C:\image_crawling\{}_review_test\image'.format(review)

    
    for i in imgs:
        k+=1
        src=i['src']    
        #print(src)

        ##style은  urlretrieve("https:"+src,path_folder+f'{k}.jpg')
        urlretrieve("https:"+src,path_folder+f'{k}.jpg')
    page+=1