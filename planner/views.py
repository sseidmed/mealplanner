from django.shortcuts import render
from django.views import generic
from django.urls import reverse 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import DayForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

from planner.models import Meal, Day

def index(request):
    num_meals = Meal.objects.all().count()

    context = {
        'num_meals': num_meals,
    }

    return render(request, 'index.html', context=context)

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
# class DayCreate(LoginRequiredMixin, CreateView):
#     model = Day
#     fields = ['day_of_week', 'date_meal', 'meal']

@login_required
def createday(request):
    if request.method != "POST":
        form = DayForm()
    else:
        form = DayForm(data=request.POST)
        if form.is_valid():
            new_day = form.save(commit=False)
            new_day.cook = request.user
            meal = form.cleaned_data['meal']
            new_day.save()
            new_day.meal.add(meal[0])
            return HttpResponseRedirect(reverse('days'))
    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'planner/day_form.html', context)

class DayUpdate(LoginRequiredMixin, UpdateView):
    model = Day
    fields = ['day_of_week', 'date_meal', 'meal']

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
