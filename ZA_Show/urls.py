from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.ZA_Show),
    #此处设置为首页，以前写法是'^$',新版本不再使用^、$，只需要‘’就可以
    # path('index/', include('ZA_Index.urls')),
]