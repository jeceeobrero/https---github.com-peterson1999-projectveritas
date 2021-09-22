from django.urls import path
from newsoutlet.OutletView import OutletIndexView as view

app_name = "newsoutlet"

urlpatterns = [
    path('newsoutlet', view.displayOutlets, name="newsoutlet"),
]