from django.db import models


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

