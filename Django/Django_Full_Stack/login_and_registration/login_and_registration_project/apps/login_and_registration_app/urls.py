from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^user/registration$', views.process_registration),
    url(r'^user/login$', views.process_login),
    url(r'^user/homepage/$', views.home_page),
    url(r'^user/logout$', views.logout),
]