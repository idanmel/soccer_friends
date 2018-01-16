from django.contrib.auth.models import User, Group
from .models import Stage, Match, Team, Tournament
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('name',)


class StageSerializer(serializers.ModelSerializer):
    # matches = MatchSerializer(many=True)

    class Meta:
        model = Stage
        fields = ('name',)


class MatchSerializer(serializers.ModelSerializer):
    home_team = TeamSerializer()
    away_team = TeamSerializer()
    stage = StageSerializer()

    class Meta:
        model = Match
        fields = ('id', 'stage', 'home_team', 'away_team')


class TournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields = ('id', 'name')
