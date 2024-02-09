from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("shristy", views.shristy),
    path("<str:name>", views.greet, name="greet"),
]
