from django.urls import path
from . import views


urlpatterns = [
    path('register/',views.register),
    path('login/', views.login),
    path('RegHandle/',views.register_handle),
    path('register_ajax/', views.register_ajax),
    path('loginHandle/', views.login_handler),
    path('logout/',views.login_out),
    path('headerUpdate/', views.header_Update),
    path('loadingBlacklist/', views.loadingBlacklist),
    path('downloadperson/', views.downloadperson),
    path('usercenter/', views.userCenter),

]
