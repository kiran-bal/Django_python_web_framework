from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from .api import router
from graphene_django.views import GraphQLView
from collegeapp_graphql.schema import schema

urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql', GraphQLView.as_view(graphiql=True)),
    url(r'api/', include(router.urls)),  # api urls for student and university
]
