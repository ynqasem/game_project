from .models import Game
from django import forms

class GameForm(forms.ModelForm):
	class Meta:
		model = Game
		fields = ['name', 'release_date', 'platforms', 'multiplayer', 'image']


		widgets = {
			"release_date": forms.DateInput(attrs={'type':'date'}),
		}