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

                sensational_art, opinion_art, satire_art, relevancy_art, overall_art_cred, article_title, article_img,article_date,topic = Credibility.loadCredibility(
                    Credibility, url) 

                #Article.addArticle(overall_art_cred, relevancy_art,opinion_art,satire_art,sensational_art,topic,url)

                context = {
                    'url': url,
                    'relevancy_art': relevancy_art, 'opinion_art': opinion_art,
                    'satire_art': satire_art, 'sensational_art': sensational_art,
                    'overall_art_cred': overall_art_cred, 
                    'article_title': article_title, 'article_img': article_img,
                    'article_date': article_date}
                
                ArticleView.addArticle(overall_art_cred, relevancy_art,opinion_art,satire_art,sensational_art,topic,url)
                
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
                

    def addArticle(overall_art_cred, relevancy_art,opinion_art,satire_art,sensational_art,topic,url):
        Article.addArticle(overall_art_cred, relevancy_art,opinion_art,satire_art,sensational_art,topic,url)
    
    def addKeyword(topics,article):
        Keywords.addKeyword(topics,article)


#     def get(self, request):
#         return render(request, 'article.html')

# #change name of post
#     def post(self, request):
#         if "check" in request.POST:
#             print("g")
#             form = URLForm(request.POST)
#             article_title = "Health experts want longer lockdown in Metro Manila"
#             article_img = None
#             article_date = None
            

#             # relevancy_src = 40.0
#             # opinion_src = 56.8
#             # satire_src = 15.5
#             # sensational_src = 95.6
#             # overall_src_cred = 85

#             if form.is_valid():

#                 urlTest = request.POST.get("url")
#                 #print(Credibility.credtest(Credibility, url))
#                 sensational_art, opinion_art, satire_art, relevancy_art, overall_art_cred, article_title, article_img,article_date,topic = Credibility.loadCredibility(
#                     Credibility, urlTest)           
#                 form = Article(credibility_score=overall_art_cred,relevancy_score=relevancy_art,nonopinion_score=opinion_art,nonsatire_score=satire_art,nonsensational_score=sensational_art,topic=topic,url=urlTest)             
#                 form.save()
#                 for x in topic:
#                     keyword= Keywords(topic=x, article=form)
#                     keyword.save()
#                 context = {'relevancy_art': relevancy_art, 'opinion_art': opinion_art,
#                     'satire_art': satire_art, 'sensational_art': sensational_art,
#                     #'relevancy_src': relevancy_src, 'opinion_src': opinion_src,
#                     #'satire_src': satire_src, 'sensational_src': sensational_src,
#                     'overall_art_cred': overall_art_cred, #'overall_src_cred': overall_src_cred,
#                     'article_title': article_title, 'article_img': article_img,
#                     'article_date': article_date}

#                 return render(request, 'article.html', context)
#             else:
#                 print("hi")
#                 print(form.errors)
#                 return HttpResponse("Not Valid!")

#         elif 'search' in request.POST:            
#             searchname = request.POST.get("searchbox", None)
#             keywordobjects=Keywords.objects.filter(topic=searchname)
#             articles=[]
#             for x in keywordobjects:
#                 print(x.article_id)
#                 articles.append(Article.objects.filter(id=x.article_id))     
#             print(keywordobjects)
#             flag=0
#             temp=-1  
#             i=0
#             while i < len(articles): 
#                 j=i+1 
#                 for x in articles[i]: 
#                     comp1= x
#                 while j < len(articles):
#                     for y in articles[j]: 
#                         comp2= y
#                     if comp1.credibility_score < comp2.credibility_score:
#                         print("DASDAS")
#                         temp = articles[i]
#                         articles[i]=articles[j]
#                         articles[j]=temp
#                     j+=1
#                 i+=1


#             article_titles = []
#             # article_imgs = []
#             article_dates = []

#             for x in range(len(articles)):
#                 for y in articles[x]:
#                     article_titles.append(Credibility.getTitle(Credibility, y.url))
#                     article_dates.append(Credibility.getDate(Credibility,y.url))
#             # for x in range(len(articles)):
#             #     for y in articles[x]:
#             #         relevancy_arts.append(y.relevancy_score)
#             #         opinion_arts.append(y.nonopinion_score)
#             #         satire_arts.append(y.nonsatire_score)
#             #         sensational_arts.append(y.nonsensational_score)
#             #         overall_art_creds.append(y.credibility_score)

#             # context = {'relevancy_art': relevancy_arts, 'opinion_art': opinion_arts,
#             #         'satire_art': satire_arts, 'sensational_art': sensational_arts,
#             #         'overall_art_cred': overall_art_creds}
#             xlist = zip(articles,article_titles, article_dates)

#             context = {
#                 'articles': xlist,
#             }

#             #print(relevancy_arts)
#             #print(""+str(relevancy_arts[0]))
#             print(articles[0][0].id)
            
#             print(searchname)
#             return render(request, 'result.html', context)