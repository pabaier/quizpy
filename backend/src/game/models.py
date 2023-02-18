from django.db import IntegrityError
from django.db import models
from django.utils.crypto import get_random_string
from question.models import Question
from user.models import CustomUser


class ScoringHook(models.Model):
    code = models.TextField()


class Hook(models.Model):
    code = models.TextField()
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True)

    class Meta:
        unique_together = ('creator', 'name')


class Game(models.Model):
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    questions = models.ManyToManyField(Question, through='question.QuestionGame')
    individual_scoring_hook = models.ForeignKey(ScoringHook, related_name='game_individual_scoring_hook',
                                                on_delete=models.CASCADE, blank=True, null=True)
    team_scoring_hook = models.ForeignKey(ScoringHook, related_name='game_team_scoring_hook', on_delete=models.CASCADE,
                                          blank=True, null=True)
    outline = models.TextField()


class ActiveGame(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=7, unique=True)

    def save(self, *args, **kwargs):
        try:
            self.slug = get_random_string(7)
            super().save(*args, **kwargs)
        except IntegrityError:
            self.save(*args, **kwargs)