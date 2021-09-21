from django.shortcuts import render
from django.http import HttpResponse


class NewsOutletView:
    def sampleOutlet(request):
        return HttpResponse("TESTING TESTING.")