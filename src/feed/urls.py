from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^$', views.about, name='index'),
    url(r'^(?P<article_id>[0-9]+)/$', views.detail, name='index'),
]
