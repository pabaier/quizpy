from .models import Question, QuestionGame, QuestionAnswerOption
from .serializers import QuestionSerializer, QuestionGameSerializer, QuestionAnswerOptionSerializer, \
    QuestionDetailSerializer, QuestionDetailPublicSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated


class QuestionDetailViewSet(ModelViewSet):
    # Question_Answer_Option.objects.select_related('question').filter(question=1)
    # queryset = Question_Answer_Option.objects.select_related('question').filter()
    queryset = Question.objects.all()
    serializer_class = QuestionDetailSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return Question.objects.filter(creator=user)


class QuestionDetailPublicViewSet(ModelViewSet):
    queryset = Question.objects.filter(public=True)
    serializer_class = QuestionDetailPublicSerializer


class QuestionViewSet(ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return Question.objects.filter(creator=user)


class QuestionGameViewSet(ModelViewSet):
    serializer_class = QuestionGameSerializer
    queryset = QuestionGame.objects.all()
    permission_classes = (IsAuthenticated,)


class QuestionAnswerOptionViewSet(ModelViewSet):
    serializer_class = QuestionAnswerOptionSerializer
    queryset = QuestionAnswerOption.objects.all()
    permission_classes = (IsAuthenticated,)
