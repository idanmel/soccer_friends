from django.shortcuts import render

from tournaments.models import Team
# Create your views here.


def index(request):
    teams = Team.objects.all()
    context = {'teams': teams}
    return render(request, 'tournaments/index.html', context)