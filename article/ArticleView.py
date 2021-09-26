from re import A
from django.conf.urls import url
from django.http.response import HttpResponse
from article.URLForms import URLForm
import validators
from django.shortcuts import render, redirect
from django.views.generic import View

import requests
from article.credibility import Credibility
from article.Article import Article
from search.Keyword import Keywords
from newsOutlet.NewsOutlet import NewsOutlets
from urllib.parse import urlparse
# Create your views here.


class ArticleView(View):
    def showCrediblityScores(request):
        if "check" in request.POST:
            print("g")
            article_title = ""
            article_img = None
            article_date = None


            form = URLForm(request.POST)
            # print("HELLO ADSADAS ", str(form.getURL()))
            # validate = URLValidator()

            if form.is_valid() and validators.url(str(form.getURL())):
                url = form.getURL()

                sensational_art, opinion_art, satire_art, relevancy_art, overall_art_cred, article_title, article_img,article_date,topic,pub_date = Credibility.loadCredibility(
                    Credibility, url) 

                #Article.addArticle(overall_art_cred, relevancy_art,opinion_art,satire_art,sensational_art,topic,url)

                context = {'relevancy_art': relevancy_art, 'opinion_art': opinion_art,
                    'satire_art': satire_art, 'sensational_art': sensational_art,
                    'overall_art_cred': overall_art_cred, 
                    'article_title': article_title, 'article_img': article_img,
                    'article_date': article_date}

                url_out, outletName = ArticleView.__getOutletName(url)
                out_id,out_flag = NewsOutlets.addNewsOutlet(overall_art_cred,outletName,url_out)

                art_flag = ArticleView.addArticle(overall_art_cred, relevancy_art,opinion_art,satire_art,sensational_art,topic,url,out_id,pub_date)
                
                if out_flag == 0 and art_flag == 1:
                    ArticleView.__updateNewsOutlet(overall_art_cred, out_id)

                if art_flag == 1:
                    article = Article.objects.latest('id')
                    for x in topic:
                        ArticleView.addKeyword(x, article)

                return render(request, 'article.html', context)
            else:
                print("hi")
                print(form.errors)
                article = 1
                context = {
                    'article': article,
                }
                return render(request, 'article.html', context)
                #return HttpResponse("Not Valid!")
                

    def addArticle(overall_art_cred, relevancy_art,opinion_art,satire_art,sensational_art,topic,url,url_id, pub_date):
        return Article.addArticle(overall_art_cred, relevancy_art,opinion_art,satire_art,sensational_art,topic,url,url_id,pub_date)
    
    def addKeyword(topics,article):
        Keywords.addKeyword(topics,article)

    def __getOutletName(url):
        url_outlet = url.split("/")[2]
        outlet_name = url_outlet.split(".")[1]

        return url_outlet, outlet_name

    def __updateNewsOutlet(overall, outlet_id):
        count = Article.objects.filter(outlet_id = outlet_id)
        outlet = NewsOutlets.objects.filter(id = outlet_id.id)
        for out in outlet:
            totalScore = out.totalScore + overall
        print(totalScore)
        new_overall = (totalScore)/(count.count())
        print(new_overall)
        NewsOutlets.updateNewsOutlet(new_overall, outlet_id,totalScore)
        

