from django.urls import path,re_path
from . import views


urlpatterns = [
    path('',views.novelsIndex),
    re_path(r'itemInfo/(.*?).html$', views.bookInfo),
]
