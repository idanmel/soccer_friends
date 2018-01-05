from django import forms


class MatchForm(forms.Form):
    home_goals = forms.IntegerField(min_value=0, initial=0)
    away_goals = forms.IntegerField(min_value=0, initial=0)
