from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
]



# this page creates the links and tells them where to go app directory