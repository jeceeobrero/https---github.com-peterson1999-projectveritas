from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

class NewsOutletView(View):
    def sampleOutlet(request):
        return HttpResponse("TESTING TESTING.")