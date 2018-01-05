from django.http import HttpResponseRedirect
from django.shortcuts import render

from tournaments.models import Match, Stage
from .forms import MatchForm
# Create your views here.


def index(request):
    if request.method == 'POST':
        return HttpResponseRedirect('/thanks/')
    else:
        if request.user.is_authenticated():
            matches = Match.objects.all()
            stages = Stage.objects.all()
            context = {'user': request.user, 'matches': matches, 'stages': stages}
            return render(request, 'tournaments/index.html', context)
