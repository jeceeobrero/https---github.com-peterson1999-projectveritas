from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from newsOutlet.NewsOutlet import NewsOutlets
from article.Article import Article
from article.credibility import Credibility


class NewsOutletView(View):
    def showOutletPerformance(request):
        print("HELLO")
<<<<<<< HEAD
        p = NewsOutlets.filterHistory(0)
        for i in p:
            print("filter-date:", i.filt)
            print("average score:", i.average)
=======
        outlet_id=7
        month_filter, year_filter, day_filter = NewsOutlets.filterHistory(outlet_id) #pass outlet id here and get 3 querysets
        for i in month_filter:
            print("filter-date:",i.filt) #filter date
            print("average score:",i.average) #average score for that date
>>>>>>> 3042166dd5b883c34c6124518c788bee2dfea60b

        articles = NewsOutletView.__getArticleList(7)

        titles = []
        dates = []
        images = []

        for x in articles:
            print(x.url)
            title, date, image = Credibility.getTID(Credibility, x.url)
            titles.append(title)
            dates.append(date)
            images.append(image)

        xlist = list(zip(articles, titles, dates, images))
        context = {
            'filterMonth': month_filter,
            'filterYear': year_filter,
            'filterDay': day_filter,
            'articles': xlist,
        }
        # return HttpResponse('NewsOutletView')
        return render(request, 'outlet.html', context)

    def __getArticleList(outlet_id):
        print("HIHIHIH")
        articles = Article.getOutletArticle(outlet_id)
        print(articles)
        return articles
