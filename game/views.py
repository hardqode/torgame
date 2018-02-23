from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.shortcuts import redirect


@login_required
def connect(request):
    """Если введен корректный номер игры, перекидывает на dashboard"""
    form = ConnectForm(request.POST)
    last_code = Game.objects.last('code')
    if form == last_code:
        return HttpResponseRedirect('game/dashboard.html')
    else:
        return render(request, 'game/connect.html')


@login_required
def dashboard(request):
    """Лобби"""
    players = Player.objects.order_by('id')
    rounds = Round.objects.order_by('id')
    transaction_types = TransactionType.objects.all()
    context = {'players': players, 'rounds': rounds, 'transaction_types': transaction_types}
    return render(request, 'game/dashboard.html', context)


def start_round(request, round_id):
    """Принимает начальные данные и запускает раунд"""
    round = Round.objects.get(id=round_id)
    if request.method != 'POST':
        # Данные не отправлялись; создаются пустые формы.
        form = RoundForm()
    else:
        # Отправлены данные POST; обработать данные
        form = RoundForm(data=request.POST)
        if form.is_valid():
            new_round = form.save(commit=False)
            new_round.save()
            return HttpResponseRedirect('game/dashboard.html', args=[round_id])
    context = {'round' : round,'form': form}
    return render(request, 'game/dashboard.html', context)


def actions_in_round(request):
    """Совершает рассчеты внутри раунда"""



