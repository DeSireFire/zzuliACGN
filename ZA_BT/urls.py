from django.urls import path,re_path
from . import views


urlpatterns = [
    path('',views.BTIndex),
    re_path(r'itemInfo/(.*?).html$',views.iteminfo),
]
