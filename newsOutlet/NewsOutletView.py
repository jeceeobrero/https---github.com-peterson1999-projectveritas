from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from newsOutlet.NewsOutlet import NewsOutlets
from article.Article import Article

class NewsOutletView(View):
    def showOutletPerformance(request):
        print("HELLO")
        p = NewsOutlets.filterHistory(0,0)
        for i in p:
            print("filter-date:",i.filt)
            print("average score:",i.average)

        articleList = NewsOutletView.__getArticleList(7)
        print(articleList)
        
        context = {
            'filterResults': p,
            'articleList': articleList,
        }
        return render(request, 'outlet.html', context)

    def __getArticleList(outlet_id):
        articles = Article.getOutletArticle(outlet_id)
        print(articles)
        return articles