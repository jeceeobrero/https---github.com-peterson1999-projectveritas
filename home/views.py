from django.db.models import query
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View
from article.URLForms import URLForm
import requests
import datetime
from newsOutlet.NewsOutlet import NewsOutlets
from newsOutlet.NewsOutletView import NewsOutletView


# Create your views here.
val = None


class AllOutletsIndexView(View):
    def get(self, request):
        outlets = NewsOutlets.getNewsOutletAll()
        outlet_logo = []
        outlet_desc = []
        for i in range(len(outlets)):
            outlet_logo.append("../static/images/gmalogo.jpg")
            outlet_desc.append("Get the latest news on the Philippines and the world: News, Business, Overseas, Entertainment, Sports and Lifestyle in text, video, photos and etc. on GMA News.")
        outletList = list(zip(outlets, outlet_logo, outlet_desc))
        context = {
            'outlets': outletList,
        }

        return render(request, 'alloutlets.html', context)

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
