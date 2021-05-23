from django.http.response import HttpResponse
#from home.forms import URLForm
from django.shortcuts import render, redirect
from django.views.generic import View

#from article import views
import requests
#from home.credibility import Credibility
from home.models import Article, Keywords
import datetime

# Create your views here.
val = None

""" class HomeIndexView(View):
    def get(self, request):
        flag = False
        url = 'http://api.openweathermap.org/data/2.5/forecast?q={}&units=metric&appid=97c08871353e0aee15a30d25127bcd1f'
        city = 'Cebu City'

        if not flag:
            r = requests.get(url.format(city)).json()

        city_weather = {
            'city': city,
            'temperature': r['list'][0]['main']['temp'],
            'description': r['list'][0]['weather'][0]['description'],
            'icon': r['list'][0]['weather'][0]['icon'],
            
            'dt1': datetime.datetime.strptime(str(r['list'][1]['dt_txt'][5:7]), "%m").strftime("%b") + " " + r['list'][1]['dt_txt'][8:10],
            'temperature1': r['list'][1]['main']['temp'],
            'description1': r['list'][1]['weather'][0]['description'],
            'icon1': r['list'][1]['weather'][0]['icon'],

            'dt2': datetime.datetime.strptime(str(r['list'][6]['dt_txt'][5:7]), "%m").strftime("%b") + " " + r['list'][6]['dt_txt'][8:10],
            'temperature2': r['list'][2]['main']['temp'],
            'description2': r['list'][2]['weather'][0]['description'],
            'icon2': r['list'][2]['weather'][0]['icon'],

            'dt3': datetime.datetime.strptime(str(r['list'][13]['dt_txt'][5:7]), "%m").strftime("%b") + " " + r['list'][13]['dt_txt'][8:10],
            'temperature3': r['list'][3]['main']['temp'],
            'description3': r['list'][3]['weather'][0]['description'],
            'icon3': r['list'][3]['weather'][0]['icon'],

            'dt4': datetime.datetime.strptime(str(r['list'][21]['dt_txt'][5:7]), "%m").strftime("%b") + " " + r['list'][21]['dt_txt'][8:10],
            'temperature4': r['list'][4]['main']['temp'],
            'description4': r['list'][4]['weather'][0]['description'],
            'icon4': r['list'][4]['weather'][0]['icon'],

        }

        url2 = 'https://api.covid19api.com/live/country/philippines/status/confirmed/date/2020-05-01T13:13:30Z'
        if not flag:
            r2 = requests.get(url2.format()).json()

        icon = ""
        if r2[-1]['Confirmed'] >= r2[-2]['Confirmed']:
            icon = "bi bi-arrow-up-right"
        else:
            icon = "bi bi-arrow-down-left"

        phil_covid = {
            'infected':  format(r2[-1]['Confirmed'], ',d'),
            'icon': icon,
            'active': format(r2[-1]['Active'], ',d'),
            'recovered': format(r2[-1]['Recovered'], ',d'),
            'deceased': format(r2[-1]['Deaths'], ',d'),
        }

        context = {'city_weather': city_weather,'phil_covid': phil_covid}
        flag = True
        return render(request, 'home.html', context)
    
    def post(self, request):
        if "check" in request.POST:
            form = URLForm(request.POST)
            if form.is_valid():
                urlTest = request.POST.get("url")
                global val
                def val():
                    return urlTest
                return redirect('article:article')
            else:
                print("home")
                print(form.errors)
                return HttpResponse("Not Valid!") """


class CoronaIndexView(View):
    def get(self, request):
        return render(request, 'corona.html')

    def post(self, request):
        form = URLForm(request.POST)
        if form.is_valid():
            urlTest = request.POST.get("url")
            global val

            def val():
                return urlTest
            return redirect('article:article')
        else:
            print(form.errors)
            return HttpResponse("Not Valid!")


class WorldIndexView(View):
    def get(self, request):
        return render(request, 'world.html')

    def post(self, request):
        form = URLForm(request.POST)
        if form.is_valid():
            urlTest = request.POST.get("url")
            global val

            def val():
                return urlTest
            return redirect('article:article')
        else:
            print(form.errors)
            return HttpResponse("Not Valid!")


class PhilIndexView(View):
    def get(self, request):
        return render(request, 'phil.html')

    def post(self, request):
        form = URLForm(request.POST)
        if form.is_valid():
            urlTest = request.POST.get("url")
            global val

            def val():
                return urlTest
            return redirect('article:article')
        else:
            print(form.errors)
            return HttpResponse("Not Valid!")


class HealIndexView(View):
    def get(self, request):
        return render(request, 'health.html')

    def post(self, request):
        form = URLForm(request.POST)
        if form.is_valid():
            urlTest = request.POST.get("url")
            global val

            def val():
                return urlTest
            return redirect('article:article')
        else:
            print(form.errors)
            return HttpResponse("Not Valid!")


class BusIndexView(View):
    def get(self, request):
        return render(request, 'business.html')

    def post(self, request):
        form = URLForm(request.POST)
        if form.is_valid():
            urlTest = request.POST.get("url")
            global val

            def val():
                return urlTest
            return redirect('article:article')
        else:
            print(form.errors)
            return HttpResponse("Not Valid!")


class TechIndexView(View):
    def get(self, request):
        return render(request, 'technology.html')

    def post(self, request):
        form = URLForm(request.POST)
        if form.is_valid():
            urlTest = request.POST.get("url")
            global val

            def val():
                return urlTest
            return redirect('article:article')
        else:
            print(form.errors)
            return HttpResponse("Not Valid!")


class EnterIndexView(View):
    def get(self, request):
        return render(request, 'entertainment.html')

    def post(self, request):
        form = URLForm(request.POST)
        if form.is_valid():
            urlTest = request.POST.get("url")
            global val

            def val():
                return urlTest
            return redirect('article:article')
        else:
            print(form.errors)
            return HttpResponse("Not Valid!")


class SportsIndexView(View):
    def get(self, request):
        return render(request, 'sports.html')

    def post(self, request):
        form = URLForm(request.POST)
        if form.is_valid():
            urlTest = request.POST.get("url")
            global val

            def val():
                return urlTest
            return redirect('article:article')
        else:
            print(form.errors)
            return HttpResponse("Not Valid!")


class SciIndexView(View):
    def get(self, request):
        return render(request, 'science.html')

    def post(self, request):
        form = URLForm(request.POST)
        if form.is_valid():
            urlTest = request.POST.get("url")
            global val

            def val():
                return urlTest
            return redirect('article:article')
        else:
            print(form.errors)
            return HttpResponse("Not Valid!")


class AboutIndexView(View):
    def get(self, request):
        return render(request, 'about.html')

    def post(self, request):
        form = URLForm(request.POST)
        if form.is_valid():
            urlTest = request.POST.get("url")
            global val

            def val():
                return urlTest
            return redirect('article:article')
        else:
            print(form.errors)
            return HttpResponse("Not Valid!")


class HowIndexView(View):
    def get(self, request):
        return render(request, 'howtouse.html')

    def post(self, request):
        form = URLForm(request.POST)
        if form.is_valid():
            urlTest = request.POST.get("url")
            global val

            def val():
                return urlTest
            return redirect('article:article')
        else:
            print(form.errors)
            return HttpResponse("Not Valid!")


class ContactIndexView(View):
    def get(self, request):
        return render(request, 'contactus.html')

    def post(self, request):
        form = URLForm(request.POST)
        if form.is_valid():
            urlTest = request.POST.get("url")
            global val

            def val():
                return urlTest
            return redirect('article:article')
        else:
            print(form.errors)
            return HttpResponse("Not Valid!")


# class ArticleIndexView(View):
#     def get(self, request):
#         return render(request, 'article.html')

# #change name of post
#     def post(self, request):
#         if "check" in request.POST:
#             print("g")
#             form = URLForm(request.POST)
#             url = None
#             article_title = "Health experts want longer lockdown in Metro Manila"
#             article_img = None
#             article_date = None
#             topic = None
#             relevancy_art = 50.0
#             opinion_art = 50.9
#             satire_art = 51.5
#             sensational_art = 85.4
#             overall_art_cred = 70
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
            
