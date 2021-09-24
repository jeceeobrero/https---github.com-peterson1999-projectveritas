from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View
from article.URLForms import URLForm
import requests
import datetime

# Create your views here.
val = None


class AllOutletsIndexView(View):
    def get(self, request):
        return render(request, 'alloutlets.html')

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
