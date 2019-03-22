from django.urls import path,include
from . import views


urlpatterns = [
    path('animeTrackerList/get/',views.animeTrackerListGet),
    path('animeTrackerList/post/',views.animeTrackerListPost),
    # path('',views.ZA_Show),
]
