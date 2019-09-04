from django.conf.urls import url
from. import views

urlpatterns = [
    url(r'^clear$', views.index),
    url(r'^reset$', views.clear),
]