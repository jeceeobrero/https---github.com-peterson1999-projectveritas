from article.credibility import Credibility
from django.db import models

# Create your models here.

class Article(models.Model):
    credibility_score = models.FloatField()
    relevancy_score= models.FloatField()
    nonopinion_score =models.FloatField()
    nonsatire_score = models.FloatField()
    nonsensational_score = models.FloatField()
    topic = models.CharField(max_length=500)
    url = models.CharField(max_length=1000)


    def addArticle(overall_art_cred, relevancy_art, opinion_art, satire_art, sensational_art, topic_art, url_art ):
        try:
            new_article = Article()
            new_article.credibility_score = overall_art_cred
            new_article.relevancy_score = relevancy_art
            new_article.nonopinion_score = opinion_art
            new_article.nonsatire_score = satire_art
            new_article.nonsensational_score = sensational_art
            new_article.topic = topic_art
            new_article.url = url_art
            count=0
            count=Article.objects.filter(url=url_art)
            print("count")
            print(count)
            if count.count() == 0 :
                print("Saved")
                new_article.save()
            
            new_article
        except Exception as e:
            print(e)

    def getArticle(art_id):
        return Article.objects.filter(id = art_id)

    def getArticleAll():
        return Article.objects.order_by('-credibility_score')
