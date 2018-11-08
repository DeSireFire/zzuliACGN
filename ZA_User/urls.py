from django.urls import path,include
from . import views


urlpatterns = [
    path('register/',views.register),
    path('login/', views.login),
    path('RegHandle/',views.register_handle),
    path('register_ajax/', views.register_ajax),
    path('loginHandle/', views.login_handler),
    path('logout/',views.login_out),
    path('usercenter/', views.userCenter),
    path('headUpdate/', views.head_Update),
    # path('site/', views.site),
    #此处设置为首页，以前写法是'^$',新版本不再使用^、$，只需要‘’就可以
    # path('index/', include('ZA_Index.urls')),
]
