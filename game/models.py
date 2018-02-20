from django.db import models


class Game(models.Model):
    id = models.IntegerField()
    code = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    balance = models.IntegerField()
    user = models.ForeignKey(Player)


class Player(models.Model):
    id = models.IntegerField()
    is_active = models.BooleanField(default=True)
    balance = models.IntegerField()
    material =