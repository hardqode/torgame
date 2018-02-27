from django.forms import ModelForm
from .models import *


class ConnectForm(ModelForm):
    class Meta:
        model = Game
        fields = ['code']


class RoundForm(ModelForm):
    class Meta:
        model = Round
        fields = '__all__'


class Step1Form(ModelForm):
    class Meta:
        model = MaterialBid
        fields = '__all__'


class Step2Form(ModelForm):
    class Meta:
        model = TransactionType
        fields = '__all__'


class Step3Form(ModelForm):
    class Meta:
        model = GoodsBid
        fields = '__all__'
