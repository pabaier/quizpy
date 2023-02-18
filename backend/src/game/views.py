from .models import Game, ActiveGame, Hook, ScoringHook
from .serializers import GameSerializer, ActiveGameSerializer, HookSerializer, ScoringHookSerializer, GameDetailSerializer
import logging

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

logger = logging.getLogger(__name__)


class GameViewSet(ModelViewSet):
    serializer_class = GameSerializer
    queryset = Game.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return Game.objects.filter(creator=user)

    # this is so that the user making the game is the creator
    # it also prevents the creator from being changed in a PUT and PATCH
    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class GameDetailViewSet(ModelViewSet):
    serializer_class = GameDetailSerializer
    queryset = Game.objects.all()
    permission_classes = (IsAuthenticated,)


class ActiveGameViewSet(ModelViewSet):
    serializer_class = ActiveGameSerializer
    queryset = ActiveGame.objects.all()
    permission_classes = (IsAuthenticated,)


class HookViewSet(ModelViewSet):
    serializer_class = HookSerializer
    queryset = Hook.objects.all()
    permission_classes = (IsAuthenticated,)


class ScoringHookViewSet(ModelViewSet):
    serializer_class = ScoringHookSerializer
    queryset = ScoringHook.objects.all()
    permission_classes = (IsAuthenticated,)

"""

from django.shortcuts import render
from django.views.generic import ListView, View
from .models import Game, Game_Question
from question.models import Question
from .forms import AddQuestionsForm
from django.http import HttpResponse, QueryDict
from user.models import CustomUser
import json
import logging
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core import serializers
from django.forms.models import model_to_dict


class GameList(View):
    template_name = 'MyGames.html'
    # queryset = Game.objects.get(creator_user_id=request.user.id)
    queryset = Game.objects.all()
    context_object_name = 'games'

    def get(self, request, *args, **kwargs):
        games = Game.objects.filter(creator_user_id=request.user)
        data = {}
        for game in games:
            data[game.id] = game.name
        return render(request, self.template_name, {'data': data})

    def delete(self, request, *args, **kwargs):
        data = QueryDict(request.body)
        logger.info(f'deleting game {data["id"]}')
        Game.objects.filter(id=data["id"]).delete()
        return HttpResponse(json.dumps({'key': 'value'}))

    def post(self, request, *args, **kwargs):
        name = request.POST['name']
        logger.info(f'name: {name}')
        newGame = Game.objects.create(
            creator_user_id = request.user,
            name = name
        )
        newGame.save()
        return HttpResponse(json.dumps({'name': name, 'id': newGame.id}))

class GameEdit(UpdateView):
    template_name = 'EditGame.html'
    fields = ['name']
    model = Game

    def get(self, request, *args, **kwargs):
        gameId = kwargs['id']
        game = Game.objects.get(id=gameId)
        gameName = game.name

        gameQuestions = self.getGameQuestions(gameId, gameName)
        userQuestions = self.getUserQuestions(request.user)
        data = {
            'gameId':gameId, 
            'gameName': gameName, 
            'gameQuestions': gameQuestions,
            'userQuestions': userQuestions
        }
        # for game in games:
        #     data[game.id] = game.name
        return render(request, self.template_name, {'data': data})
    
    def post(self, request, *args, **kwargs):
        logger.info(f'received {request.POST}')
        id = request.POST['id']
        newName = request.POST['name']
        Game.objects.filter(id=id).update(name=newName)
        return HttpResponse(json.dumps({'newName': newName}))

    def put(self, request, *args, **kwargs):
        gameId = kwargs['id']
        data = QueryDict(request.body)
        questionId = data['questionId']
        newValue = data['newValue']
        gameQuestionObject = Game_Question.objects.get(game_id=gameId, question_id=questionId)
        gameQuestionObject.time_limit = newValue
        gameQuestionObject.save(update_fields=['time_limit'])
        return HttpResponse(json.dumps({'success': True}))


    @staticmethod
    def getGameQuestions(gameId, gameName):
        questionIdObjects = Game_Question.objects.filter(game_id=gameId)
        questions = []
        for q in questionIdObjects:
            question = Question.objects.get(id=q.question_id.id)
            questionDict = model_to_dict(question)
            questionDict['time'] = q.time_limit
            questions.append(questionDict)
        return questions

    @staticmethod
    def getUserQuestions(user):
        questionsObjects = Question.objects.filter(creator_user_id = user)
        questions = []
        for q in questionsObjects:
            qd = model_to_dict(q)
            questions.append(qd)
        # j = serializers.serialize("json", questions)
        return questions

class GameDetail(DetailView):
    model = Game
class GameCreate(CreateView):
    template_name = 'game_create.html'
    fields = ['name']
    model = Game
class GameDelete(DeleteView):
    model = Game

"""
