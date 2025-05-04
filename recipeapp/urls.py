from django.urls import path
from .import views

urlpatterns = [
    path('', views.index),
    path('addrecipe/',views.addrecipe),
    # path('searchresult',views.search),
]