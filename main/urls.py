from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('aboutme', views.about, name="about"),
    path('progects', views.works, name="works"),
    path('contacts', views.contacts, name="contacts")

]
