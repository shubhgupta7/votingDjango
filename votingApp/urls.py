from django.urls import path
from . import views

urlpatterns= [
    path("home",views.index,name = "Index"),
    path("time",views.time,name = "time"),

]