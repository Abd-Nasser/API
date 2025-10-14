from django.urls import path
from . import views

urlpatterns = [
    path("my-first-api/", views.my_first_api)
]
