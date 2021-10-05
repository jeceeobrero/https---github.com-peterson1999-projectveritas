from django.urls import path
from newsOutlet.NewsOutletView import NewsOutletView as view

app_name = "newsOutlet"

urlpatterns = [
    path('', view.seeOutlet, name='newsOutlet'),
    path('<str:name>', view.seeOutlet, name='newsOutlet')
]
