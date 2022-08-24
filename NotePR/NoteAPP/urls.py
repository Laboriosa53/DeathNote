from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="Death Note Defteri"),
    path('about', views.about,name="Death Note Defteri"),
    path('note', views.note,name="Death Note Defteri"),
]