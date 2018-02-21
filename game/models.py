from django.db import models
from django.contrib.auth.models import User


class Game(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    balance = models.IntegerField()


class Player(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    is_active = models.BooleanField(default=True)
    balance = models.IntegerField()
    material = models.IntegerField()
    product = models.IntegerField()

    class Meta:
        unique_together = ("game", "user")


class Round(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    buy_materials = models.IntegerField()
    sell_goods = models.IntegerField()
    recycling = models.IntegerField()
    store_materials = models.IntegerField()
    store_goods = models.IntegerField()
    tax = models.IntegerField()


class TransactionType(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    code = models.CharField(max_length=10)
    count_materials = models.IntegerField()
    count_goods = models.IntegerField()


class Transaction(models.Model):
    type = models.ForeignKey(TransactionType, on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    price = models.IntegerField()


class MaterialBid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    round = models.ForeignKey(Round, on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    count = models.IntegerField()
    price = models.IntegerField()


class GoodsBid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    round = models.ForeignKey(Round, on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    count = models.IntegerField()
    price = models.IntegerField()
