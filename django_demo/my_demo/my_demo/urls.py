from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from .api import router

urlpatterns = [
    url(r'^admin/', admin.site.urls), # admin URL for login
    url(r'^api/', include(router.urls)), # api urls for student and university
]
