from django.urls import path, re_path
from materials import views;

urlpatterns = [

    # path('fabric/',include([
    #     path('',views.fabric),
    #     path('<int:id>/',views.fabricDetail),
    #
    # ]))

    path('',views.materials2),
    path('fabric/',views.materials2),
    path('upload/',views.upload),
    path('query/',views.queryByOrm),
    path('leather/',views.leather),
    path('download/',views.download),
    # path('fabric/<int:id>/',views.fabricDetail),
    # path('car/',views.fabric),
    # path('index/',views.index),
]