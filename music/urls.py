from music import views;

from django.urls import path, re_path
urlpatterns = [
    path('',views.music),
    path('album/',views.album),

]