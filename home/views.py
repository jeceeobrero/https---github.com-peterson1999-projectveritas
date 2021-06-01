from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View
from article.URLForms import URLForm
import requests
import datetime

# Create your views here.
val = None


class CoronaIndexView(View):
    def get(self, request):
        return render(request, 'corona.html')

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


class WorldIndexView(View):
    def get(self, request):
        return render(request, 'world.html')

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


class PhilIndexView(View):
    def get(self, request):
        return render(request, 'phil.html')

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


class HealIndexView(View):
    def get(self, request):
        return render(request, 'health.html')

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


class BusIndexView(View):
    def get(self, request):
        return render(request, 'business.html')

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


class TechIndexView(View):
    def get(self, request):
        return render(request, 'technology.html')

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


class EnterIndexView(View):
    def get(self, request):
        return render(request, 'entertainment.html')

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


class SportsIndexView(View):
    def get(self, request):
        return render(request, 'sports.html')

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


class SciIndexView(View):
    def get(self, request):
        return render(request, 'science.html')

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
