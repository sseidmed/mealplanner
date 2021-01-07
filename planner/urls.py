from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('days/', views.DayListView.as_view(), name='days'),
    path('day/<int:pk>', views.DayDetailView.as_view(), name='day-detail'),
    path('meals/', views.MealListView.as_view(), name='meals'),
    path('meal/<int:pk>', views.MealDetailView.as_view(), name='meal-detail'),

    path('day/create/', views.createday, name='day-create'),
    path('day/<int:pk>/update/', views.DayUpdate.as_view(), name='day-update'),
    path('day/<int:pk>/delete/', views.DayDelete.as_view(), name='day-delete'),

    path('meal/create/', views.MealCreate.as_view(), name='meal-create'),
    path('meal/<int:pk>/update/', views.MealUpdate.as_view(), name='meal-update'),
    path('meal/<int:pk>/delete/', views.MealDelete.as_view(), name='meal-delete'),
]