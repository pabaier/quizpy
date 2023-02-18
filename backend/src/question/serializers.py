from .models import Question, QuestionGame, QuestionAnswerOption
from rest_framework.serializers import ModelSerializer


class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"


class QuestionAnswerOptionSerializer(ModelSerializer):
    class Meta:
        model = QuestionAnswerOption
        fields = "__all__"


class QuestionGameSerializer(ModelSerializer):
    class Meta:
        model = QuestionGame
        fields = "__all__"


class QuestionDetailSerializer(ModelSerializer):
    answerOptions = QuestionAnswerOptionSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = "__all__"


class QuestionDetailPublicSerializer(ModelSerializer):
    answerOptions = QuestionAnswerOptionSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = "__all__"


class QuestionGameDetailsSerializer(ModelSerializer):
    question = QuestionDetailSerializer(read_only=True)

    class Meta:
        model = QuestionGame
        exclude = ("id", "game")