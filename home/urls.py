from django.urls import path
from home import views


app_name = 'home'
urlpatterns = [
    path('top', views.HomeIndexView.as_view(), name = "main"),
    path('corona', views.CoronaIndexView.as_view(), name = "corona"),
    path('world', views.WorldIndexView.as_view(), name = "world"),
    path('philippines', views.PhilIndexView.as_view(), name = "phil"),
    path('health', views.HealIndexView.as_view(), name = "health"),
    path('business', views.BusIndexView.as_view(), name = "business"),
    path('technology', views.TechIndexView.as_view(), name = "technology"),
    path('entertainment', views.EnterIndexView.as_view(), name = "entertainment"),
    path('sports', views.SportsIndexView.as_view(), name = "sports"),
    path('science', views.SciIndexView.as_view(), name = "science"),
    path('about', views.AboutIndexView.as_view(), name = "about"),
    path('howdoesitwork', views.HowIndexView.as_view(), name = "how"),
    path('tryitout', views.ContactIndexView.as_view(), name = "contact"),
    #path('article', views.ArticleIndexView.as_view(), name = "article"),
]