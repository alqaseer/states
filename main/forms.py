from django import forms
from main.models import City

from django.core.validators import RegexValidator

alphanumeric = RegexValidator(r'^[a-zA-Z]*$', 'Only letters please')

class CitySearchForm(forms.Form):
	name = forms.CharField(required=True, validators=[alphanumeric])
	state = forms.CharField(required=True, validators=[alphanumeric])


class CreateCityForm(forms.ModelForm):
	class Meta:
		model = City
		fields = '__all__'

class CityEditForm(forms.ModelForm):
	class Meta:
		model = City
		fields = '__all__'