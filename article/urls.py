from django.urls import path
from article.ArticleView import ArticleView as view


app_name = "article"
urlpatterns = [
    path('articleCred',view.showCrediblityScores, name = 'article'),
]