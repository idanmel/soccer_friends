from django.shortcuts import render

from tournaments.models import Match
# Create your views here.


def index(request):
    matches = Match.objects.all()
    context = {'matches': matches}
    return render(request, 'tournaments/index.html', context)