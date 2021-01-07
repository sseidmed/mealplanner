from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy 
from .models import Day, Meal
from bootstrap_datepicker_plus import DatePickerInput

class DayForm(forms.ModelForm):

    class Meta:
        model = Day
        fields = ['date_meal', 'day_of_week', 'meal']  
        meal = forms.ModelChoiceField(
            queryset = Meal.objects.all()
        )
        widgets = {
            'date_meal': DatePickerInput(format='%m/%d/%Y'),
        }