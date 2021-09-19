from django.shortcuts import render
from django.http import HttpResponse


class NewsOutletView:
    def sampleOutlet(request):
        return HttpResponse("Hello, world. You're at the News Outlet Page.")