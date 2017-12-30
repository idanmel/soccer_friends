from django.shortcuts import render

from tournaments.models import Tournament
# Create your views here.


def index(request):
    tournaments = Tournament.objects.all()
    context = {'tournaments': tournaments}
    return render(request, 'tournaments/index.html', context)