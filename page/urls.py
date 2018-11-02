from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^list/$', views.instagram_tag_list, name='instagram_tag_list'),
    url(r'^search/tag/$', views.search_tag, name='search_tag'),
]