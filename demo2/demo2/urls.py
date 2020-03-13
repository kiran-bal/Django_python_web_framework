from .api import router
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bookdata/',include(router.urls)),
]
