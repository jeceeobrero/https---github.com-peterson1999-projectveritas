from django.conf.urls import url
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View

import requests
from article.Article import Article
import datetime
from article.credibility import Credibility

# Create your views here.


class HomeIndexView(View):
    def displayArticles(request):
        context = HomeIndexView.showLatestUpdates()
        return render(request, 'home.html', context)

    def getTopArticles():
        articles = Article.getArticleAll()
        return articles

    def showLatestUpdates():
        flag = False
        url = 'http://api.openweathermap.org/data/2.5/forecast?q={}&units=metric&appid=97c08871353e0aee15a30d25127bcd1f'
        city = 'Cebu City'

        if not flag:
            r = requests.get(url.format(city)).json()

        city_weather = {
            'city':
            city,
            'temperature':
            r['list'][0]['main']['temp'],
            'description':
            r['list'][0]['weather'][0]['description'],
            'icon':
            r['list'][0]['weather'][0]['icon'],
            'dt1':
            datetime.datetime.strptime(str(r['list'][1]['dt_txt'][5:7]),
                                       "%m").strftime("%b") + " " +
            r['list'][1]['dt_txt'][8:10],
            'temperature1':
            r['list'][1]['main']['temp'],
            'description1':
            r['list'][1]['weather'][0]['description'],
            'icon1':
            r['list'][1]['weather'][0]['icon'],
            'dt2':
            datetime.datetime.strptime(str(r['list'][6]['dt_txt'][5:7]),
                                       "%m").strftime("%b") + " " +
            r['list'][6]['dt_txt'][8:10],
            'temperature2':
            r['list'][2]['main']['temp'],
            'description2':
            r['list'][2]['weather'][0]['description'],
            'icon2':
            r['list'][2]['weather'][0]['icon'],
            'dt3':
            datetime.datetime.strptime(str(r['list'][13]['dt_txt'][5:7]),
                                       "%m").strftime("%b") + " " +
            r['list'][13]['dt_txt'][8:10],
            'temperature3':
            r['list'][3]['main']['temp'],
            'description3':
            r['list'][3]['weather'][0]['description'],
            'icon3':
            r['list'][3]['weather'][0]['icon'],
            'dt4':
            datetime.datetime.strptime(str(r['list'][21]['dt_txt'][5:7]),
                                       "%m").strftime("%b") + " " +
            r['list'][21]['dt_txt'][8:10],
            'temperature4':
            r['list'][4]['main']['temp'],
            'description4':
            r['list'][4]['weather'][0]['description'],
            'icon4':
            r['list'][4]['weather'][0]['icon'],
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
            'infected': format(r2[-1]['Confirmed'], ',d'),
            'icon': icon,
            'active': format(r2[-1]['Active'], ',d'),
            'recovered': format(r2[-1]['Recovered'], ',d'),
            'deceased': format(r2[-1]['Deaths'], ',d'),
        }
        # articles
        top_articles = HomeIndexView.getTopArticles()
        titles = []
        dates = []
        images = []
        for article in top_articles:
            title, date, image = Credibility.getTID(Credibility, article.url)
            titles.append(title)
            dates.append(date)
            images.append(image)

        print(top_articles)
        articleList = list(zip(top_articles, titles, dates, images))

        # outlets

        outlet_name = ["GMA", "ABS-CBN", "CNN Philippines"]
        outlet_logo = images
        outlet_score = [86.75, 90.20, 91.73]
        outletList = list(zip(outlet_name, outlet_logo, outlet_score))

        context = {'city_weather': city_weather,
                   'phil_covid': phil_covid,
                   'top_articles': articleList,
                   'top_outlets': outletList}
        flag = True
        return context


#    def displayArticles(request):
#        if "check" in request.POST:
#            form = URLForm(request.POST)
#            if form.is_valid():
#                urlTest = request.POST.get("url")
#                global val
#                def val():
#                    return urlTest
#                return redirect('article:article')
#            else:
#                print("home")
#                print(form.errors)
#                return HttpResponse("Not Valid!")
