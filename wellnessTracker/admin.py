from django.contrib import admin
from .models import Mood, Day, Habit


@admin.register(Mood)
class MoodAdmin(admin.ModelAdmin):
    list_display = ['scale', 'slept_scale', 'emotions', 'note', 'updated_at']
    search_fields = ['scale','slept_scale','emotions', 'note']

@admin.register(Day)
class DayAdmin(admin.ModelAdmin):
    list_display = ['user', 'mood', 'habit', 'date', 'updated_at']
    search_fields = ['user', 'mood', 'date']

@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ['coffee_amount' , 'coffee_unit', 'cigarettes', 'cigarette_type', 'alcohol_amount', 'alcohol_unit', 'alcohol_type', 'exercise_minutes', 'exercise_unit', 'exercise_type', 'updated_at']
    search_fields = ['coffee_amount' , 'coffee_unit', 'cigarettes', 'cigarette_type', 'alcohol_amount', 'alcohol_unit', 'alcohol_type', 'exercise_minutes', 'exercise_unit', 'exercise_type']
