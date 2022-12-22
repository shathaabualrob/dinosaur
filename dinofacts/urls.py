from . import views
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter


from django.urls import path

from dinofacts.views import show_dino

urlpatterns = [
    path("show_dino/<str:name>/", show_dino),
]
