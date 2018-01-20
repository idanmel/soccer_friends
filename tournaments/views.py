from .models import Match, Tournament, User, MatchPrediction
from rest_framework import viewsets, generics
from .serializers import MatchSerializer, TournamentSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


class TournamentViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that shows all tournaments
    """
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer


class MatchesList(generics.ListAPIView):
    """
    API endpoint that shows all the matches in a specific tournament
    """
    serializer_class = MatchSerializer

    def get_queryset(self):
        pk = int(self.kwargs['pk'])
        return Match.objects.filter(stage__tournament=pk)


@api_view(['POST'])
def match_predictions(request):
    if request.method == 'POST':
        user = User.objects.get(email=request.data["body"]["email"])
        for match_prediction in request.data["body"]["matches"]:
            match = Match.objects.get(pk=match_prediction["id"])
            mp, created = MatchPrediction.objects.update_or_create(
                friend=user, match=match,
                defaults={'home_goals': match_prediction["home_goals"], 'away_goals': match_prediction['away_goals']})
        return Response({"message": "Match Predictions Saved!"})
    else:
        return Response({"message": "This endpoint only likes post for now"})
