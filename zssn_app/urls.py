from django.contrib import admin
from django.urls import path
from zssn_app import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('', views.index, name='home'),
    path('survivors/', views.SurvivorsList.as_view()),
    path('survivors/reports', views.SurvivorListInfected.as_view()),
    path('survivors/<int:id>', views.SurvivorsList.as_view()),
    path('post', views.post, name='post')
]
