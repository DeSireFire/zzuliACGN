from django.conf.urls import url
from ZA_users import views

urlpatterns=[
    url(r'^Register/$',views.Register),
    url(r'^test/$',views.Test),
    # url(r'^login/$', views.login),
    url(r'^RegEmail/$',views.Register_handle_Email),
    url(r'^RegPhone/$',views.Register_handle_Phone),
    # url(r'^register_skip/$', views.register_skip),
    # url(r'^login_handle/$', views.login_handle),
    # url(r'^logout/$',views.login_skip),
    # url(r'^info/$', views.info),
    # url(r'^site/$', views.site),

]