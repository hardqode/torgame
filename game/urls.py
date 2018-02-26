from django.urls import path, include

from .views import *

app_name = "game"

urlpatterns = [
    path('connect', connect, name='connect'),
    #   только по id
    path('dashboard/<int:game_id>', dashboard, name='connect'),
    path('player_screen/<int:game_id>', player_screen, name='connect'),
]