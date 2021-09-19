from django.db import models

# Create your models here.

class NewsOutlet(models.Model):
    credibility_score = models.FloatField()
    outlet_name = models.CharField(max_length=500)
    url = models.CharField(max_length=1000)

    def addNewsOutlet(overall, outlet_name, url_art):
        try:
            new_outlet = NewsOutlet()
            new_outlet.credibility_score = overall
            new_outlet.outlet_name = outlet_name
            new_outlet.url = url_art
            count=0
            count=NewsOutlet.objects.filter(url=url_art)
            print("count")
            print(count)
            if count.count() == 0 :
                print("Saved")
                new_outlet.save()
            
            new_outlet
        except Exception as e:
            print(e)
    def getNewsOutlet(outlet_id):
        return NewsOutlet.objects.filter(id = outlet_id)

    def getNewsOutletAll():
        return NewsOutlet.objects.order_by('-credibility_score')

    def updateNewsOutlet(overall,outletName):
        NewsOutlet.objects.filter(outlet_name = outletName).update(credibility_score = overall)

