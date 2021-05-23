from django.urls import path
from search.SearchView import SearchView as view

app_name = "search"
urlpatterns = [
    path('searchRes',view.displayArticles, name = 'search'),
]