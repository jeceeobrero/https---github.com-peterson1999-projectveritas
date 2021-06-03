from types import new_class
from django.db import models
from article.Article import Article

# Create your models here.
class Keywords(models.Model):
    topic = models.CharField(max_length=100)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    #searchbox = models.CharField(max_length=100)

    def addKeyword(topics, artikulo):
        try:
            new_keywords = Keywords()
            new_keywords.topic = topics
            new_keywords.article = artikulo
            new_keywords.save()
        except Exception as e:
            print(e)

    def getArticleList(topics):
        newtopics= topics.split()
        print("newtopics: ")
        print(newtopics)
        keywords = Keywords.objects.filter(topic__in=newtopics)
        print(keywords)
        return Keywords.objects.filter(topic__in=newtopics)
