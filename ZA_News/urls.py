from django.urls import path,re_path
from . import views


urlpatterns = [
    path('',views.ZA_News),
    path('types/',views.typeList),
    re_path('type_newsAjax/',views.type_news),
]
