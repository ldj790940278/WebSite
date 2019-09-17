from myblog import views;

from django.urls import path, re_path
urlpatterns = [
    path('',views.myblog),

]