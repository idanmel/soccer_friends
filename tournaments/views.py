from .models import Match, Tournament
from rest_framework import viewsets, generics
from .serializers import MatchSerializer, TournamentSerializer


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
