#네이버 뉴스
from bs4 import BeautifulSoup
import requests
import re
import csv

from bs4 import BeautifulSoup
import requests

def project_csv(news_list):
    with open('project_csv', 'w', encoding='utf8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(news_list)
def naver_news_it():
    url = f'https://news.naver.com/main/list.naver?mode=LSD&mid=sec&sid1=105'
    res = requests.get(url)
    source = res.text
    soup = BeautifulSoup(source,'html.parser')
    #신문사
    companies = soup.select('#main_content > div.list_body.newsflash_body > ul.type06_headline > li > dl > dd > span.writing')
    images = soup.select('#main_content > div.list_body.newsflash_body > ul.type06_headline > li > dl > dt.photo > a > img')
    titles = soup.select('#main_content > div.list_body.newsflash_body > ul.type06_headline > li > dl > dt:nth-child(2) > a')

    companies_new = []
    for span in companies:
        companies_new.append(span.get_text())

    images_new = []
    for img in images:
        images_new.append(img.get('src'))

    titles_new = []
    for a in titles:
        titles_new.append((a.get_text().strip(), a['href']))


    #요약
    summary = soup.select('#main_content > div.list_body.newsflash_body > ul.type06_headline > li > dl > dd > span.lede')
    summary_new = []
    for span in summary:
        summary_new.append(span.get_text())

    news_list = list(zip(titles_new, images_new, summary_new, companies_new))
    return news_list







if __name__ == '__main__':

    news = naver_news_it()#[((제목,링크주소),이미지URL,요약,신문사),(),(),......]
    print(news)
    project_csv(news)
    '''
    for article, img, summary, company in news:
        print(article)
        #for titles,img,company in article:
        title,link = article
        print(f'제목:{title},주소:{link},사진:{img}')
        print(f'요약:{summary}, 신문사:{company}')
    '''
