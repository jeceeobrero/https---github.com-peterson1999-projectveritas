from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from newsOutlet.NewsOutlet import NewsOutlets
class NewsOutletView(View):
    def sampleOutlet(request):
        print("HELLO")
        p = NewsOutlets.filterHistory(0,0)
        for i in p:
            print("filter-date:",i.filt)
            print("average score:",i.average)
        return HttpResponse("TESTING TESTING.")
        