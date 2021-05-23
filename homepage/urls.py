from django.urls import path
from homepage.HomeView import HomeIndexView as view

app_name = "homepage"
urlpatterns = [
    path('main',view.displayArticles, name = 'homepage'),
]