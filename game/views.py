# from curtsies.events import get_key
from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

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



# TODO имеет доступ только владелец игры

@login_required
def dashboard(request, game_id):
    """Лобби"""
    if request.user == User.objects.get(username='admin'):
        if request.method == 'POST':
            round = Round.objects.get(id=request.POST.get('id'))
            if round.status == 'step1':
                # TODO Перевести на шаг2. Посчитать лучшие предложения от игроков по закупке сырья(т.е. максимальная сумма)
                """Допустим есть 20 ед сырья и 3 игрока, которые не видят ставки друг друга. Первый предложил купить 5ед за 1000Р каждая,
                второй 10 по 1500, третий 15 по 2000. Нужно выбрать максимальную цену(3й игрок и по ней продать все сырье
                которое он запросил, далее у второго игрока оставшееся(5 получается), а первому не остается ничего). В процессе отображать изменения баланса и кол-ва сырья"""
                # TODO Проверить логику
                price_list_user = {} #словарь для извлечения юзеров с наибольшей ценой
                price_list = [] #список из сумм, которые готовы предложить
                for user in MaterialBid.objects.all(): # добавляем юзеров и их предложенную сумму
                    user_name = user.user.username
                    price = user.price
                    count = user.count
                    total_price = price * count
                    price_list_user[user_name] = total_price
                    price_list.append(total_price)
                price_list.sort()
                price_list.reverse()


                for i in range(len(price_list)):  # вычитаем у всех балансы
                    player = get_key(price_list_user, i)  # тут извлекаем игрока
                    get_player = MaterialBid.objects.get(user=player)
                    round_result = Game.objects.get(id=game_id).balance
                    player_balance = Player.objects.get(user_name=player).balance
                    player_material = Player.objects.get(user_name=player).material
                    round_result = int(round_result) - int(get_player.count)

                    if round_result != -1 | round_result == 0:
                        Game.objects.get(id=game_id).balance = round_result
                        Player.objects.get(user_name=player).balance = int(player_balance) - int(get_player.price * get_player.count)
                        Player.objects.get(user_name=player).material = int(get_player.count) + int(player_material)

                    elif round_result < 0 & round_result != -1:
                        Player.objects.get(user_name=player).balance = int(player_balance) - int(get_player.price * get_player.count)
                        Player.objects.get(user_name=player).material = int(get_player.count) + int(round_result)
                        Game.objects.get(id=game_id).balance = -1
                round.status = RoundStatus.objects.get(code='step2')
            elif round.status == 'step2':
                # TODO Перевести на шаг3. Переработать сырье в продукцию.
                pass
            elif round.status == 'step3':
                # TODO Перевести на шаг4. Реализация продукции. Посчитать лучшее(минимальное по стоимости) предложение о продаже продукции. Занести все в транзакции.
                pass
            elif round.status == 'step4':
                # TODO Завершить раунд. Вычесть стоимость хранения и налоги.
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
        return render(request, 'game/dashboard.html', {})
    else:
        game = Game.objects.filter(code=request.POST.get('code')).last()
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


# TODO смотри Схема.jpg


@require_POST
def player_step1(request, round_id):
    """Заполняет форму по количеству и стоимости покупки сырья"""
    form = Step1Form(request.POST)
    if form.is_valid():
        step1 = form.save()
        step1.round_id = round_id
        step1.save()
        return HttpResponseRedirect('game/dashboard.html', args=[round_id])


@require_POST
def player_step2(request, round_id):
    """Заполняет форму по кол-ву переработки сырья в продукцию"""
    form = Step2Form(request.POST)
    if form.is_valid():
        step2 = form.save()
        step2.round_id = round_id
        step2.save()
        return HttpResponseRedirect('game/dashboard.html', args=[round_id])


@require_POST
def player_step3(request, round_id):
    """Заполняет форму по продаже продукции и стоимости"""
    form = Step3Form(request.POST)
    if form.is_valid():
        step3 = form.save()
        step3.round_id = round_id
        step3.save()
        return HttpResponseRedirect('game/dashboard.html', args=[round_id])


