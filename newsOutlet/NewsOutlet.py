from django.db import models
import article.Article
# Create your models here.

class NewsOutlets(models.Model):
    credibility_score = models.FloatField()
    outlet_name = models.CharField(max_length=500)
    url = models.CharField(max_length=1000)
    totalScore = models.FloatField(default=None)

    def addNewsOutlet(overall, outlet_name, url_art):
        try:
            new_outlet = NewsOutlets()
            new_outlet.credibility_score = overall
            new_outlet.outlet_name = outlet_name
            new_outlet.url = url_art
            count=0
            count=NewsOutlets.objects.filter(outlet_name=outlet_name)
            id = None
            flag = 0
            if count.count() == 0 :
                new_outlet.totalScore = overall
                print("Saved")
                new_outlet.save()
                id = NewsOutlets.objects.latest('id')
                flag = 1
                print(id)
            else:
                id = NewsOutlets.objects.latest('id')
                print(id)
            return id,flag
        except Exception as e:
            print(e)
    def getNewsOutlet(outlet_id):
        return NewsOutlets.objects.filter(id = outlet_id)
        
    def getNewsOutletAll():
        return NewsOutlets.objects.order_by('-credibility_score')

    def updateNewsOutlet(overall,outlet_id,totalscore):
        NewsOutlets.objects.filter(id = outlet_id.id).update(credibility_score = overall, totalScore = totalscore)

    def filterHistory(outlet_id):
        o_id =outlet_id 
        
        querymonth = '''SELECT 1 as id, DATE_FORMAT(pub_date,'%%Y %%m') as filt, avg(credibility_score) as average
                from article_article
                WHERE outlet_id = {0}
                GROUP BY filt
                ORDER BY filt desc'''.format(o_id)
        
        queryyear = '''SELECT 1 as id, DATE_FORMAT(pub_date,'%%Y') as filt, avg(credibility_score) as average
                from article_article
                WHERE outlet_id = {0}
                GROUP BY filt
                ORDER BY filt desc'''.format(o_id)
        
        queryday = '''SELECT 1 as id, DATE_FORMAT(pub_date,'%%Y %%m %%e') as filt, avg(credibility_score) as average
                from article_article
                WHERE outlet_id = {0}
                GROUP BY filt
                ORDER BY filt desc'''.format(o_id)
        month_filter= article.Article.Article.objects.raw(querymonth)
        year_filter= article.Article.Article.objects.raw(queryyear)
        day_filter= article.Article.Article.objects.raw(queryday) 
        return month_filter, year_filter, day_filter

