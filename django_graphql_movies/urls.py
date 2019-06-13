from django.contrib import admin
from django.urls import path
from graphene_django.views import GraphQLView
from django_graphql_movies.schema import schema


urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql/', GraphQLView.as_view(graphiql=True)),
]