from django.urls import path
from . import views
from api.rest_api import my_rest_api

urlpatterns = [
    path("my-first-api/", views.my_first_api),
    path("profils-api-view/", my_rest_api.profils_api_view),
    path("profils-api-view/<int:pk>/", my_rest_api.profils_api_view)
]
