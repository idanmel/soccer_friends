from django.db import IntegrityError
from django.test import TestCase
from tournaments.models import Tournament, Stage, Team, Match, MatchPrediction
from django.contrib.auth.models import User


class MatchPredictionTestCase(TestCase):
    # noinspection PyUnresolvedReferences
    def setUp(self):
        self.wc2018 = Tournament(name="World Cup 2018")
        self.wc2018.save()
        self.group_a = Stage(name="Group A", abbv="A", tournament=self.wc2018)
        self.group_a.save()
        self.russia = Team(name="Russia")
        self.russia.save()
        self.argentina = Team(name="Argentina")
        self.argentina.save()
        self.match = Match(stage=self.group_a, home_team=self.russia, away_team=self.argentina)
        self.match.save()
        self.user = User(username="Idan")
        self.user.save()
        self.match_prediction = MatchPrediction(
            friend=self.user, match=self.match, home_team=self.russia,
            home_goals=5, away_team=self.argentina, away_goals=6
        )
        self.match_prediction.save()
        self.different_user = User(username="Mel")
        self.different_user.save()
        self.different_match_prediction = MatchPrediction(friend=self.different_user, match=self.match,
                                                          home_team=self.russia, away_team=self.argentina)
        self.different_match_prediction.save()

    def test_tournament_created(self):
        self.assertEqual(self.wc2018.name, "World Cup 2018")

    def test_stage_created(self):
        self.assertEqual(self.group_a.name, "Group A")
        self.assertEqual(self.group_a.tournament.name, "World Cup 2018")

    def test_team_created(self):
        self.assertEqual(self.russia.name, "Russia")
        self.assertEqual(self.argentina.name, "Argentina")

    def test_match_created(self):
        self.assertIn('Group A', str(self.match))
        self.assertIn('Russia', str(self.match))
        self.assertIn('Argentina', str(self.match))

    def test_user(self):
        self.assertIn('Idan', str(self.user))

    def test_match_prediction(self):
        self.assertIn('Idan', str(self.match_prediction))
        self.assertIn('Group A', str(self.match_prediction))
        self.assertIn('Russia', str(self.match_prediction))
        self.assertIn('Argentina', str(self.match_prediction))
        self.assertIn('5', str(self.match_prediction))
        self.assertIn('6', str(self.match_prediction))

    def test_no_duplicate_match_predictions(self):
        self.same_match_prediction = MatchPrediction(friend=self.user, match=self.match)
        self.assertRaises(IntegrityError, self.same_match_prediction.save)

    def test_match_prediction_different_user(self):
        self.assertIn('Mel', str(self.different_match_prediction))
        self.assertIn('Group A', str(self.different_match_prediction))
        self.assertIn('Russia', str(self.different_match_prediction))
        self.assertIn('Argentina', str(self.different_match_prediction))
        self.assertIn('0', str(self.different_match_prediction))
        self.assertIn('0', str(self.different_match_prediction))

    def test_cascade_user(self):
        self.user.delete()
        self.assertFalse(User.objects.filter(username="Idan").exists())
        self.assertFalse(MatchPrediction.objects.filter(friend=self.user).exists())
        self.assertTrue(MatchPrediction.objects.filter(friend=self.different_user).exists())

    def test_cascade_team(self):
        self.russia.delete()
        self.assertFalse(Team.objects.filter(name="Russia").exists())
        self.assertFalse(Match.objects.filter(home_team=self.russia).exists())
        self.assertFalse(MatchPrediction.objects.filter(home_team=self.russia).exists())
