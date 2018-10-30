from django.urls import path,include
from ZA_Index import views


urlpatterns = [
    # path('', views.ZA_show),
    path('cp', views.Construction_period),
    #此处设置为首页，以前写法是'^$',新版本不再使用^、$，只需要‘’就可以
    # path('index/', include('ZA_Index.urls')),
]