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
#    source = models.ForeignKey(Source,on_delete = models.CASCADE)

#class Source(models.Model):
#    credibility_score = models.FloatField()
#    journalism_score= models.FloatField()
#    opinion_score =models.FloatField()
#    sattire_score = models.FloatField()
#    sensational_score = models.FloatField()
#    reliable_score = models.FloatField()
#    topic = models.CharField(max_length=500)
#    name = models.constants(max_length=100)