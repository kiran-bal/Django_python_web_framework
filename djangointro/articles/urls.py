from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^about/$',views.article_list),
    url(r'^$',views.article_home),
]
