from django.conf.urls import url
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View

import requests


class OutletIndexView(View):
    def displayOutlets(request):
        return render(request, 'outlet.html')


# Create your views here.
