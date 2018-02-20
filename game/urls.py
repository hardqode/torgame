from django.urls import path, include

from .views import *

app_name="game"

urlpatterns = [
    path('connect', connect, name='connect'),
]