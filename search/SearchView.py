from django.conf.urls import url
from django.http.response import HttpResponse
from search.SearchForm import SearchForm
from django.shortcuts import render, redirect
from django.views.generic import View
import requests

from .Keyword import Keywords
from article.Article import Article
from article.credibility import Credibility
from newsOutlet.NewsOutlet import NewsOutlets
# Create your views here.


class SearchView(View):
    def displayArticles(request):
        if 'search' in request.POST:

            form = SearchForm(request.POST)
            is_outlet = False


            searchname = form.getKeyWord()
            print(searchname)
            if (NewsOutlets.isNewsOutlet(searchname.lower())):
                is_outlet=True
                print(is_outlet)
                outlet_id=NewsOutlets.getNewsOutletID(searchname.lower())
            else:
                outlet_id=-1
            outlet = NewsOutlets.getNewsOutlet(outlet_id) 
            print("outlet: ",outlet.values_list('outlet_name', flat=True))
            keywordobjects= Keywords.getArticleList(searchname)

            articles=[]
            emptyList=[]
            for x in keywordobjects:
                print(x.article_id)
                if x.article_id not in emptyList:
                    emptyList.append(x.article_id)
                    articles.append(SearchView.getArticles(x.article_id))     
            print(keywordobjects)
            flag=0
            temp=-1  
            i=0
            while i < len(articles): 
                j=i+1 
                for x in articles[i]: 
                    comp1= x
                while j < len(articles):
                    for y in articles[j]: 
                        comp2= y
                    if comp1.credibility_score < comp2.credibility_score:
                        print("DASDAS")
                        temp = articles[i]
                        articles[i]=articles[j]
                        articles[j]=temp
                    j+=1
                i+=1


            titles = []
            dates = []
            images = []

            for x in range(len(articles)):
                for y in articles[x]:
                    title, date, image = Credibility.getTID(Credibility, y.url)
                    titles.append(title)
                    print(date)
                    dates.append(date)
                    images.append(image)

            xlist = list(zip(articles, titles, dates, images))
            outlet_desc = ""
            outlet_logo = ""
            if is_outlet:
                outlet = outlet[0]
                outlet_logo = "../static/images/gmalogo.jpg"
                outlet_desc = "Get the latest news on the Philippines and the world: News, Business, Overseas, Entertainment, Sports and Lifestyle in text, video, photos and etc. on GMA News."
            context = {
                'articles': xlist,
                'outlet':outlet,
                'outlet_logo':outlet_logo,
                'outlet_desc':outlet_desc,
                'is_outlet': is_outlet #In frontend, maybe check first if is_outlet is true before getting values of outlet variable.
            }

            #print(articles[0][0].id)
            
            #print(searchname)
            return render(request, 'result.html', context)

    def getArticles(article_id):
        return Article.getArticle(article_id)