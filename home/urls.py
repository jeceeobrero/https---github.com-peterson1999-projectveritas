from django.urls import path
from home import views
from home.HomeView import HomeIndexView

app_name = 'home'
urlpatterns = [
    path('', HomeIndexView.displayArticles, name='homepage'),
    path('about', views.AboutIndexView.as_view(), name="about"),
    path('howdoesitwork', views.HowIndexView.as_view(), name="how"),
    path('tryitout', views.ContactIndexView.as_view(), name="contact"),
    path('alloutlets', views.AllOutletsIndexView.as_view(), name="alloutlets"),
    #path('article', views.ArticleIndexView.as_view(), name = "article"),
]
