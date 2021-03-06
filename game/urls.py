from django.urls import path, include

from .views import *

app_name = "game"

urlpatterns = [
    path('connect', connect, name='connect'),
    path('dashboard/<int:game_id>', dashboard, name='dashboard'),
    path('player_screen/<int:game_id>', player_screen, name='player_screen'),
]