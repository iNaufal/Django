from django.urls import path

#pemanggilan views, 3 deklarasi
from . import views

urlpatterns = [
    path('', views.index),
    path('search/', views.search),
    path('news/', views.news),
    path('article/', views.article),
]