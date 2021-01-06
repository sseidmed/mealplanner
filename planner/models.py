from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Meal(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.CharField(max_length=500)
    

    MEALS = (
        ('v', 'Vegan'),
        ('n', 'Non-Vegan'),
    )
    meal_type = models.CharField(
        max_length=1,
        choices = MEALS,
        help_text = 'Select the type of meal'
    )

    

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('meal-detail', args=[str(self.id)])


class Day(models.Model):
    DAYS = (
        ('m', 'Monday'),
        ('t', 'Tuesday'),
        ('w', 'Wednesday'),
        ('th', 'Thursday'),
        ('f', 'Friday'),
        ('sat', 'Saturday'),
        ('sun', 'Sunday'),
    )

    day_of_week = models.CharField(
        max_length = 3,
        choices = DAYS,
        help_text = 'Day of the Week',
    )

    date_meal = models.DateField()
    meal = models.ManyToManyField(Meal, help_text="Choose meal for the day")
    cook = models.ForeignKey(User,on_delete=models.SET_NULL, null=True, blank=True, related_name='meals')
    class Meta:
        ordering = ['date_meal']

    def __str__(self):
        return f'{self.day_of_week}, {self.date_meal}'

    def get_absolute_url(self):
        return reverse('day-detail', args=[str(self.id)])


