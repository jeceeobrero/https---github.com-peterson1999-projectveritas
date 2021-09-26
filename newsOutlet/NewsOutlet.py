from django.db import models

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

