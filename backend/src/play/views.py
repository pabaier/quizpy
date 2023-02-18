from django.shortcuts import render
from game.models import Game, ActiveGame
from django.http import JsonResponse
from django.forms.models import model_to_dict

def index(request):
    return render(request, 'play/index.html', {})

def host(request, game_id):
    activeGame = ActiveGame(game_id=game_id)
    activeGame.save()

    return JsonResponse(model_to_dict(activeGame))

    # return render(request, 'play/host.html', {
    #     'game_token': activeGame.slug,
    #     'game_id': game_id
    # })

def join(request, game_token):
    return render(request, 'play/join.html', {
        'game_token': game_token
    })