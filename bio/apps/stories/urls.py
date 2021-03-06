"""Stories URL Configuration"""
from django.urls import path

from . import views

urlpatterns = [
    path("", views.StagesView.as_view(), name="stages"),
    path("<slug:slug>/", views.StoriesListView.as_view(), name="stories"),
]
