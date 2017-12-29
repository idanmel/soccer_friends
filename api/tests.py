from django.test import TestCase
from api.models import Tournament


class TournamentTestCase(TestCase):
    def setUp(self):
        Tournament.objects.create(name="World Cup 2018")

    def test_tournament_created(self):
        wc2018 = Tournament.objects.get(name="World Cup 2018")
        self.assertEqual(wc2018.name, "World Cup 2018")
