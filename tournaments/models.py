from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth.models import User


class Tournament(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Stage(models.Model):
    tournament = models.ForeignKey(Tournament, related_name='stages', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    abbv = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Match(models.Model):
    stage = models.ForeignKey(Stage, related_name='matches', on_delete=models.CASCADE)
    home_team = models.ForeignKey(Team, related_name='home_team_matches', on_delete=models.CASCADE)
    away_team = models.ForeignKey(Team, related_name='away_team_matches', on_delete=models.CASCADE)
    home_goals = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    away_goals = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    finished = models.BooleanField(default=False)

    def __str__(self):
        return "{}: {} - {}".format(self.stage.name, self.home_team, self.away_team)


class MatchPrediction(models.Model):
    friend = models.ForeignKey(User, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    home_goals = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    away_goals = models.IntegerField(default=0, validators=[MinValueValidator(0)])

    def __str__(self):
        return "{}: {} {} - {} {}".format(self.match.stage.name, self.match.home_team, self.home_goals,
                                          self.match.away_team, self.away_goals)

