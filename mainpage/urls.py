from django.urls import path
from .views.index import MainPage

urlpatterns = [
    path('',MainPage.as_view(), name="index"),
]