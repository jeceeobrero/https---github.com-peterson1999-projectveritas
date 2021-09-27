from django.urls import path
from newsOutlet.NewsOutletView import NewsOutletView as view

app_name = "newsOutlet"

urlpatterns = [
    path('newsOutlet', view.showOutletPerformance, name="newsOutlet"),
]
