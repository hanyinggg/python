from django import forms
from .models import Strategy

class StrategyForm(forms.ModelForm):
	clas Meta:
		model = Strategy
		fields = ['title', 'pub_time', 'text']