from django.contrib import admin
from tournaments.models import Tournament, Stage, Team, Match

# Register your models here.
admin.site.register(Tournament)
admin.site.register(Stage)
admin.site.register(Team)
admin.site.register(Match)
