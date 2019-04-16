from django.urls import path
from . import views


urlpatterns = [
    path('animeTrackerList/get/',views.animeTrackerListGet),
    path('loadingmagnet/',views.loadingmagnet),
    path('imgUrlSave/',views.imgUrlSave),
    # path('',views.ZA_Show),
]
