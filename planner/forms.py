from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy 
from .models import Day, Meal

class DayForm(forms.ModelForm):

    class Meta:
        model = Day
        fields = ['day_of_week', 'date_meal', 'meal']  
        meal= forms.ModelChoiceField(
            queryset = Meal.objects.all(), 
            initial = 0
        )

    