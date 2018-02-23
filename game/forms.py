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
