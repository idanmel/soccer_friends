from django.test import TestCase
from tournaments.models import Tournament, Stage, Team


class StageTestCase(TestCase):
    def setUp(self):
        Tournament.objects.create(name="World Cup 2018")
        self.wc2018 = Tournament.objects.get(name="World Cup 2018")
        Stage.objects.create(name="Group A", abbv="A", tournament=self.wc2018)

    def test_tournament_created(self):
        self.assertEqual(self.wc2018.name, "World Cup 2018")

    def test_stage_created(self):
        self.group_a = Stage.objects.get(name="Group A")
        self.assertEqual(self.group_a.name, "Group A")
        self.assertEqual(self.group_a.tournament.name, "World Cup 2018")


class TeamTestCase(TestCase):
    def setUp(self):
        Team.objects.create(name="Russia")
        self.russia = Team.objects.get(name="Russia")

    def test_team_created(self):
        self.assertEqual(self.russia.name, "Russia")
