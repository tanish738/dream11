from django.contrib import admin
from django.urls import path,include 
from .views import *


urlpatterns = [
    path('players_list/', PlayerList.as_view()),
    path('update_player/' , PlayerDetail.as_view()),
    path('team_list/',  TeamList.as_view()),
    path('update_team/', TeamDetail.as_view()),
    path('team/', create_team),
    path('player/', create_player),
    path('match/',matchday),
]