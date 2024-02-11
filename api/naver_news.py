from flask_restful import Resource
from flask import make_response
from model.naver_news_crawling import naver_news_it
import json

class Naver(Resource):
    def get(self):
        articles = naver_news_it()
        #print(articles)
        keys=['title','link','image','summary']
        news_dict=[]
        for titles,imageUrl,summary,_ in articles:
            title,link = titles #구조분해
            news_dict.append({'title':title,'link':link,'imageUrl':imageUrl,'summary':summary})

        #print(news_dict)
        return make_response(json.dumps(news_dict,ensure_ascii=False))