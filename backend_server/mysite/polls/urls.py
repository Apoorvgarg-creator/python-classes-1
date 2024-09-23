from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("apoorv/",views.index2, name="apoorv")
]
