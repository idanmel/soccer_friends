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
    first_place_leads_to = models.ForeignKey('self', null=True, blank=True, default=None, related_name='first_place_from')
    second_place_leads_to = models.ForeignKey('self', null=True, blank=True, default=None, related_name='second_place_from')

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=255, unique=True)
    flag = models.CharField(max_length=255, null=True, blank=True, default="")

    def __str__(self):
        return self.name


class Match(models.Model):
    stage = models.ForeignKey(Stage, related_name='matches', on_delete=models.CASCADE)
    home_team = models.ForeignKey(Team, related_name='home_team_matches', on_delete=models.CASCADE, null=True,
                                  blank=True)
    away_team = models.ForeignKey(Team, related_name='away_team_matches', on_delete=models.CASCADE, null=True,
                                  blank=True)
    home_goals = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    away_goals = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    finished = models.BooleanField(default=False)

    class Meta:
        unique_together = ('stage', 'home_team', 'away_team')

    def __str__(self):
        return "{}: {} - {}".format(self.stage.name, self.home_team, self.away_team)


class MatchPrediction(models.Model):
    friend = models.ForeignKey(User, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    home_team = models.ForeignKey(
        Team, related_name='home_team_match_predictions', on_delete=models.CASCADE, null=True, blank=True
    )
    away_team = models.ForeignKey(
        Team, related_name='away_team_match_predictions', on_delete=models.CASCADE, null=True, blank=True
    )
    home_goals = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    away_goals = models.IntegerField(default=0, validators=[MinValueValidator(0)])

    class Meta:
        unique_together = ('friend', 'match')

    def __str__(self):
        return "{}, {}: {} {} - {} {}".format(self.friend.username, self.match.stage.name, self.home_team,
                                              self.home_goals, self.away_team, self.away_goals)


class StagesScoringRule(models.Model):
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE)
    precise = models.PositiveSmallIntegerField(default=0)
    imprecise = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return "{} scoring rules".format(self.stage.name)


class MatchPoint(models.Model):
    friend = models.ForeignKey(User, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    points = models.PositiveSmallIntegerField(default=None)

    def __str__(self):
        return "{} points for {}".format(self.friend.username, str(self.match))
