from django.shortcuts import render,redirect
from django.views.generic import View

import requests

import datetime

# Create your views here.
class HomeIndexView(View):
	def get(self,request):
		url = 'http://api.openweathermap.org/data/2.5/forecast?q={}&units=metric&appid=97c08871353e0aee15a30d25127bcd1f'
		city = 'Cebu City'
		r = requests.get(url.format(city)).json()
		
		city_weather = {
            'city' : city,

            'temperature' : r['list'][0]['main']['temp'],
            'description' : r['list'][0]['weather'][0]['description'],
			'icon' : r['list'][0]['weather'][0]['icon'],

			'dt1': self.returnMonth(str(r['list'][1]['dt_txt'][5:7])) + " " + r['list'][1]['dt_txt'][8:10],
            'temperature1' : r['list'][1]['main']['temp'],
            'description1' : r['list'][1]['weather'][0]['description'],
			'icon1' : r['list'][1]['weather'][0]['icon'],

			'dt2': self.returnMonth(str(r['list'][6]['dt_txt'][5:7])) + " " + r['list'][6]['dt_txt'][8:10],
            'temperature2' : r['list'][2]['main']['temp'],
            'description2' : r['list'][2]['weather'][0]['description'],
			'icon2' : r['list'][2]['weather'][0]['icon'],

			'dt3': self.returnMonth(str(r['list'][13]['dt_txt'][5:7])) + " " + r['list'][13]['dt_txt'][8:10],
            'temperature3' : r['list'][3]['main']['temp'],
            'description3' : r['list'][3]['weather'][0]['description'],
			'icon3' : r['list'][3]['weather'][0]['icon'],

			'dt4': self.returnMonth(str(r['list'][21]['dt_txt'][5:7])) + " " + r['list'][21]['dt_txt'][8:10],
            'temperature4' : r['list'][4]['main']['temp'],
            'description4' : r['list'][4]['weather'][0]['description'],
			'icon4' : r['list'][4]['weather'][0]['icon'],

        }

		url2 = 'https://api.apify.com/v2/datasets/sFSef5gfYg3soj8mb/items?format=json&clean=1'
		r2 = requests.get(url2.format()).json()

		icon = ""
		if r2[-1]['infected'] >= r2[-2]['infected']:
			icon = "bi bi-arrow-up-right"
		else:
			icon = "bi bi-arrow-down-left"

		phil_covid = {
			'infected':  format(r2[-1]['infected'], ',d'),
			'icon': icon,
			'active': format(r2[-1]['activeCases'], ',d'),
			'recovered': format(r2[-1]['recovered'], ',d'),
			'deceased': format(r2[-1]['deceased'], ',d'),
		}
		#print(phil_covid)
		context = {'city_weather' : city_weather, 'phil_covid': phil_covid}
		print("hello")
		return render(request,'home.html', context)
	
	def returnMonth(self,month_number):
		datetime_object = datetime.datetime.strptime(month_number, "%m")
		month_name = datetime_object.strftime("%b")
		return month_name

class CoronaIndexView(View):
	def get(self, request):
		return render(request, 'corona.html')

class WorldIndexView(View):
	def get(self, request):
		return render(request, 'world.html')

class PhilIndexView(View):
	def get(self, request):
		return render(request, 'phil.html')

class HealIndexView(View):
	def get(self, request):
		return render(request, 'health.html')

class BusIndexView(View):
	def get(self, request):
		return render(request, 'business.html')

class TechIndexView(View):
	def get(self, request):
		return render(request, 'technology.html')

class EnterIndexView(View):
	def get(self, request):
		return render(request, 'entertainment.html')

class SportsIndexView(View):
	def get(self, request):
		return render(request, 'sports.html')

class SciIndexView(View):
	def get(self, request):
		return render(request, 'science.html')

class AboutIndexView(View):
	def get(self, request):
		return render(request, 'about.html')

class HowIndexView(View):
	def get(self, request):
		return render(request, 'howtouse.html')

class ContactIndexView(View):
	def get(self, request):
		return render(request, 'contactus.html')

class ArticleIndexView(View):
	def get(self, request):
		return render(request, 'article.html')