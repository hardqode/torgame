from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User


from .models import *
from .forms import *
from django.shortcuts import redirect


@login_required
def connect(request):
    """Если введен корректный номер игры, перекидывает на dashboard"""
    game = Game.objects.filter(code=request.POST.get('code')).last()

    if game:
        player = Player.objects.create(
            game=game,
            user=request.user,
            balance=game.balance
        )
        return HttpResponseRedirect('game/player_screen/' + str(game.id))
    else:
        return render(request, 'game/connect.html')


# имеет доступ только владелец игры

@login_required
def dashboard(request, game_id):
    """Лобби"""
    if request.user == User.objects.get('admin'):
        if request.method == 'POST':
            round = Round.objects.get(id=request.POST.get('id'))
            if round.status == 'step1':
                # Перевести на шаг2. Посчитать лучшие предложения от игроков по закупке сырья(т.е. максимальная сумма)
                pass
            elif round.status == 'step2':
                # Перевести на шаг3. Вычесть стоимость налогов, хранения сырья и продукции у игроков. Переработать сырье в продукции.
                pass
            elif round.status == 'step3':
                # Завершить раунд. Посчитать лучшее(минимальное по стоимости) предложение о продаже продукции. Посчитать звершающие балансы.
                pass
        game = Game.objects.get_or_404(id = game_id)
        players_list = Player.objects.filter(game = game)
        rounds_list = Round.objects.filter(game=game)
        last_round = rounds_list.filter(is_active =True).last()
        context = {
            'players_list': players_list,
            'rounds_list': rounds_list,
            'last_round': last_round
        }
        return render(request, 'game/dashboard.html', context)
    else:
        return HttpResponseRedirect('game/player_screen/' + str(game.id))

# имеет доступ только игрок игры
@login_required
def player_screen(request, game_id):
    transaction_types = TransactionType.objects.all()
    pass

# Должна создать раунд и редирект на дашборд
@require_POST
def create_round(request, game_id):
    """Принимает начальные данные и запускает раунд"""
    # Отправлены данные POST; обработать данные
    form = RoundForm(request.POST)
    if form.is_valid():
        new_round = form.save(commit=False)
        new_round.game_id = game_id
        new_round.save()
        return HttpResponseRedirect('game/dashboard.html', args=[game_id])



def player_step1(request):
    pass

def player_step2(request):
    pass

def player_step3(request):
    pass



