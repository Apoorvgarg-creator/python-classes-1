from django.urls import path

from . import views

app_name= "polls"

urlpatterns = [
    path("", views.index, name="index"),
    #localhost:port/polls/ques_id
    path("<int:ques_id>/",views.detail, name="detail"),
    path("<int:ques_id>/results/",views.results, name="results"),
    path("<int:ques_id>/vote/",views.vote, name="vote"),
]
