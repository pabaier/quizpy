from .models import Game, ActiveGame, Hook, ScoringHook
from question.serializers import QuestionGameDetailsSerializer
from rest_framework import serializers


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = "__all__"
        read_only_fields = ("creator",)


class GameDetailSerializer(serializers.ModelSerializer):
    questions = QuestionGameDetailsSerializer(source="game_questions", many=True)

    class Meta:
        model = Game
        fields = "__all__"


class ActiveGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActiveGame
        fields = "__all__"


class HookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hook
        fields = "__all__"


class ScoringHookSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScoringHook
        fields = "__all__"
