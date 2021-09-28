from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from newsOutlet.NewsOutlet import NewsOutlets
from article.Article import Article
from article.credibility import Credibility


class NewsOutletView(View):
    def showOutletPerformance(request):
        print("HELLO")
        p = NewsOutlets.filterHistory(0)
        for i in p:
            print("filter-date:", i.filt)
            print("average score:", i.average)

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
            'filterResults': p,
            'articles': xlist,
        }
        # return HttpResponse('NewsOutletView')
        return render(request, 'outlet.html', context)

    def __getArticleList(outlet_id):
        print("HIHIHIH")
        articles = Article.getOutletArticle(outlet_id)
        print(articles)
        return articles
