from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('apps.models_practice_app.urls')),

]