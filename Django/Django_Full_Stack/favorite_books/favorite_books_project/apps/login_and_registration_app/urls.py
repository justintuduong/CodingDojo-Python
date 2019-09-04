from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^user/registration$', views.process_registration),
    url(r'^user/login$', views.process_login),
    url(r'^user/logout$', views.logout),
]



    # url(r'^$', views.index),
    # url(r'^book_desc/(?P<book_id>\d+)$', views.book_desc),
    # url(r'^add_author$', views.add_author_to_book),
    # url(r'^authors$', views.authors),
    # url(r'^add_new_author$', views.add_new_author),    
    # url(r'^author_notes/(?P<author_id>\d+)$', views.author_notes),
    # url(r'^add_book_to_author$', views.add_book_to_author),
