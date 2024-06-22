from django.contrib import admin
from .models import MoodScale, MoodEmotion, MoodNote, Sleep, CoffeHabit, CigaretteHabit, Sports, AlcoholHabit, Day


@admin.register(MoodScale)
class MoodScaleAdmin(admin.ModelAdmin):
    list_display = ['scale', 'updated_at']
    search_fields = ['scale']

@admin.register(MoodEmotion)
class MoodEmotionAdmin(admin.ModelAdmin):
    list_display = ['emotions', 'updated_at']
    search_fields = ['emotions']

@admin.register(MoodNote)
class MoodNoteAdmin(admin.ModelAdmin):
    list_display = ['note', 'updated_at']
    search_fields = ['note']

@admin.register(Sleep)
class SleepAdmin(admin.ModelAdmin):
    list_display = ['slept_scale', 'updated_at']
    search_fields = ['slept_scale']

@admin.register(CoffeHabit)
class CoffeHabitAdmin(admin.ModelAdmin):
    list_display = ['coffee_amount', 'coffee_unit', 'updated_at']
    search_fields = ['coffee_amount', 'coffee_unit']

@admin.register(CigaretteHabit)
class CigaretteHabitAdmin(admin.ModelAdmin):
    list_display = ['cigarettes', 'cigarette_type', 'updated_at']
    search_fields = ['cigarettes', 'cigarette_type']

@admin.register(Sports)
class SportsAdmin(admin.ModelAdmin):
    list_display = ['exercise_times', 'exercise_unit', 'exercise_type', 'updated_at']
    search_fields = ['exercise_times', 'exercise_unit', 'exercise_type']

@admin.register(AlcoholHabit)
class AlcoholHabitAdmin(admin.ModelAdmin):
    list_display = ['alcohol_amount', 'alcohol_unit', 'alcohol_type', 'updated_at']
    search_fields = ['alcohol_amount', 'alcohol_unit', 'alcohol_type']

@admin.register(Day)
class DayAdmin(admin.ModelAdmin):
    list_display = ['user', 'mood_scale', 'mood_emotion', 'mood_note', 'sleep', 'sports', 'cigarette_habit',
                    'alcohol_habit', 'coffee_habit', 'date', 'updated_at']
    search_fields = ['user__username', 'mood__note', 'date']
