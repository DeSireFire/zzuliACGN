from django.urls import path,re_path
from . import views


urlpatterns = [
    path('',views.novelsIndex),
    path('ajaxCategoryIndex/', views.categoryIndex),
    path('ajaxCategory/', views.category),
    re_path(r'book/(.*?).html$', views.bookInfo),
]
