from django.contrib.auth.models import User
from .models import Stage, Match, Team, Tournament
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('name', 'flag', 'id')


class MatchSerializer(serializers.ModelSerializer):
    home_team = TeamSerializer()
    away_team = TeamSerializer()

    class Meta:
        model = Match
        fields = ('id', 'home_team', 'away_team', 'home_goals', 'away_goals', 'finished')


class TournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields = ('id', 'name')


class StageSerializer(serializers.ModelSerializer):
    matches = MatchSerializer(many=True, read_only=True)
    tournament = TournamentSerializer()

    class Meta:
        model = Stage
        fields = ('name', 'id', 'first_place_leads_to', 'second_place_leads_to', 'matches', 'tournament')

