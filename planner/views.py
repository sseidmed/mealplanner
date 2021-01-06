from django.shortcuts import render
from django.views import generic
from django.urls import reverse 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from planner.models import Meal, Day

def index(request):
    num_meals = Meal.objects.all().count()

    context = {
        'num_meals': num_meals,
    }

    return render(request, 'index.html', context=context)

# @login_required
# def days(request):
#     """Show all topics"""
#     days=Day.objects.filter(cook=request.user)
#     context={'days': days}
#     return render(request, 'planner/day_list.html', context)

class DayListView(LoginRequiredMixin, generic.ListView):
    model = Day

    def get_queryset(self):
      day_list = Day.objects.filter(cook=self.request.user)
      return day_list
      

class DayDetailView(LoginRequiredMixin, generic.DetailView):
    model = Day

# show all meals that this cook assigned to particular days on her calendar
class MealListView(LoginRequiredMixin, generic.ListView):
    model = Meal

class MealDetailView(LoginRequiredMixin, generic.DetailView):
    model = Meal

# CRUD for Day model
class DayCreate(LoginRequiredMixin, CreateView):
    model = Day
    fields = ['day_of_week', 'date_meal', 'meal']

class DayUpdate(LoginRequiredMixin, UpdateView):
    model = Day
    fields = ['day_of_week', 'date_meal', 'meal', 'cook']

class DayDelete(LoginRequiredMixin, DeleteView):
    model = Day
    success_url = reverse_lazy('days')

# CRUD for Meal model
class MealCreate(LoginRequiredMixin, CreateView):
    model = Meal
    fields = ['name', 'ingredients', 'meal_type']

class MealUpdate(LoginRequiredMixin, UpdateView):
    model = Meal
    fields = ['name', 'ingredients', 'meal_type']

class MealDelete(LoginRequiredMixin, DeleteView):
    model = Meal
    success_url = reverse_lazy('meals')
