from django.urls import path

#pemanggilan views, 3 deklarasi
from . import views

urlpatterns = [
    path('', views.index),
]