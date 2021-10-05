from django.urls import path
from newssection import views


app_name = 'newssection'
urlpatterns = [
    path('corona', views.CoronaIndexView.as_view(), name="corona"),
    path('world', views.WorldIndexView.as_view(), name="world"),
    path('philippines', views.PhilIndexView.as_view(), name="phil"),
    path('health', views.HealIndexView.as_view(), name="health"),
    path('business', views.BusIndexView.as_view(), name="business"),
    path('technology', views.TechIndexView.as_view(), name="technology"),
    path('entertainment', views.EnterIndexView.as_view(), name="entertainment"),
    path('sports', views.SportsIndexView.as_view(), name="sports"),
    path('science', views.SciIndexView.as_view(), name="science"),
]
