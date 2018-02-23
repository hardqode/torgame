from django.db import models
from django.contrib.auth.models import User


class Game(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    balance = models.IntegerField()


class Player(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    balance = models.IntegerField()
    material = models.IntegerField()
    product = models.IntegerField()

    class Meta:
        unique_together = ("game", "user")


class Round(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    buy_minimal_materials = models.IntegerField(default=0, verbose_name='Покупка сырья')
    sell_max_goods = models.IntegerField(default=0, verbose_name='Продажа продукции')
    recycling = models.IntegerField(default=0, verbose_name='Переработка')
    store_materials = models.IntegerField(default=0, verbose_name='Хранение сырья')
    store_goods = models.IntegerField(default=0, verbose_name='Хранение продукции')
    tax = models.IntegerField(default=0, verbose_name='Налог')


class TransactionType(models.Model):
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
    count = models.IntegerField()
    price = models.IntegerField()
