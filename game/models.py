from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class Game(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    balance = models.IntegerField(default=0)

    def __str__(self):
        """Возвращает строковое представление модели"""
        return self.code

    class Meta:
        verbose_name =_('Игра')
        verbose_name_plural = _('Игры')


class Player(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    balance = models.IntegerField()
    material = models.IntegerField(default=0)
    product = models.IntegerField(default=0)

    class Meta:
        unique_together = ("game", "user")
        verbose_name = _('Игрок')
        verbose_name_plural = _('Игроки')

    def __str__(self):
        """Возвращает строковое представление модели"""
        return self.user


class RoundStatus(models.Model):
    title = models.CharField(max_length=200, blank=True)
    code = models.CharField(max_length=10)


class Round(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    status = models.ForeignKey(RoundStatus, on_delete=models.CASCADE)
    buy_minimal_materials = models.IntegerField(default=0, verbose_name='Покупка сырья')
    sell_max_goods = models.IntegerField(default=0, verbose_name='Продажа продукции')
    recycling = models.IntegerField(default=0, verbose_name='Переработка')
    store_materials = models.IntegerField(default=0, verbose_name='Хранение сырья')
    store_goods = models.IntegerField(default=0, verbose_name='Хранение продукции')
    tax = models.IntegerField(default=0, verbose_name='Налог')

    def __str__(self):
        """Возвращает строковое представление модели"""
        return self.id

    class Meta:
        verbose_name =_('Раунд')
        verbose_name_plural = _('Раунды')


class TransactionType(models.Model):
    title = models.CharField(max_length=200)
    code = models.CharField(max_length=10)
    count_materials = models.IntegerField()
    count_goods = models.IntegerField()

    def __str__(self):
        """Возвращает строковое представление модели"""
        return self.title

    class Meta:
        verbose_name =_('Тип операции')
        verbose_name_plural = _('Типы операций')


class Transaction(models.Model):
    type = models.ForeignKey(TransactionType, on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    price = models.IntegerField()

    def __str__(self):
        """Возвращает строковое представление модели"""
        return self.type

    class Meta:
        verbose_name =_('Операция')
        verbose_name_plural = _('Операции')


class MaterialBid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    round = models.ForeignKey(Round, on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    count = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        """Возвращает строковое представление модели"""
        return self.count, self.price

    class Meta:
        verbose_name =_('Ставка материалов')
        verbose_name_plural = _('Ставки матриалов')


class GoodsBid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    round = models.ForeignKey(Round, on_delete=models.CASCADE)
    count = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        """Возвращает строковое представление модели"""
        return self.code

    class Meta:
        verbose_name =_('Ставка продукции')
        verbose_name_plural = _('Ставки продукции')