import random
from django.http import HttpResponse
import logging
from seminar2.models import Coin
from django.shortcuts import render

logger = logging.getLogger(__name__)

def eagle(request, count: int):
    game_list = ['орел', 'решка']
    result = []
    for i in range(count):
        response = random.choice(game_list)
        result.append(response)
    context = {
        'result': result
    }
    return render(request, 'seminar1/index.html', context=context)


# def eagle(request):
#     game_list = ('орел', 'решка')
#     responce = random.choice(game_list)
#     coin = Coin(is_eagle=responce)
#     coin.save()
#     logger.info(f'Значение: {coin}')
#     return HttpResponse(coin)

# def eagle(request):
#     game_list = ('орел', 'решка')
#     responce = random.choice(game_list)
#     logger.info(f'Значение: {responce}')
#     return HttpResponse(responce)

def cube(request):
    cube_value = random.randint(1, 6)
    logger.info(f'Кубик выпал: {cube_value}')
    return HttpResponse(cube_value)


def random_number(request):
    number = random.randint(0, 100)
    logger.info(f'Выпало число: {number}')
    return HttpResponse(number)

def show_elements(request, n: int):
    return HttpResponse(f'{Coin.counter(n)}')