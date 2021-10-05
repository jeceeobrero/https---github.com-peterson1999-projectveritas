from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.generic import View
from newsOutlet.NewsOutlet import NewsOutlets
from article.Article import Article
from article.credibility import Credibility
from json import dumps


class NewsOutletView(View):
    def showOutletPerformance(request, outlet_id, name):
        # print("HELLO")
        month_filter, year_filter, day_filter, latest = NewsOutlets.filterHistory(
            outlet_id)  # pass outlet id here and get 3 querysets
        # print("latest", latest)
        for i in latest:
            print("nonsensational:", i.nonsensational)  # filter date
            print("nonsensational:", i.nonsatire)  # filter date
            print("nonsensational:", i.nonsensational)  # filter date
            print("nonsensational:", i.credibility)

        for i in month_filter:
            print("filter-date:", i.filt)  # filter date
            print("average score:", i.average)  # average score for that date

        articles = NewsOutletView.__getArticleList(outlet_id)

        name = name.upper()

        titles = []
        dates = []
        images = []

        monthDates = []
        monthValues = []

        dayDates = []
        dayValues = []

        yearDates = []
        yearValues = []
        for i in month_filter:
            monthDates.append(i.filt)
            monthValues.append(i.average)

        for i in day_filter:
            dayDates.append(i.filt)
            dayValues.append(i.average)

        for i in year_filter:
            yearDates.append(i.filt)
            yearValues.append(i.average)

        print("months ", monthDates)
        print("values ", monthValues)

        for x in articles:
            print(x.url)
            title, date, image = Credibility.getTID(Credibility, x.url)
            titles.append(title)
            dates.append(date)
            images.append(image)

        xlist = list(zip(articles, titles, dates, images))
        print("cred", latest[0].credibility)
        dataDictionary = {
            'month_dates': monthDates,
            'month_values': monthValues,
            'day_dates': dayDates,
            'day_values': dayValues,
            'year_dates': yearDates,
            'year_values': yearValues
        }

        cred = [{
            'nonopinion': round(latest[0].nonopinion, 2),
            'nonsatire': round(latest[0].nonsatire, 2),
            'nonsensational': round(latest[0].nonsensational, 2),
            'credibility': round(latest[0].credibility, 2),
        }]
        context = {
            'data': dumps(dataDictionary),
            'articles': xlist,
            'latest': cred,
            'name': name
        }
        print(context)
        # return HttpResponse('NewsOutletView')
        return render(request, 'outlet.html', context)

    def seeOutlet(request, name):
        print(name)
        id = 0
        if request.method == "POST":
            id = request.POST.get("outletID")
        return NewsOutletView.showOutletPerformance(request, id, name)

    def __getArticleList(outlet_id):
        print("HIHIHIH")
        articles = Article.getOutletArticle(outlet_id)
        print(articles)
        return articles
