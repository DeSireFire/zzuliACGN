from django.urls import path
from . import views


urlpatterns = [
    path('animeTrackerList/get/',views.animeTrackerListGet),
    path('loadingmagnet/',views.loadingmagnet),
    # path('',views.ZA_Show),
]
