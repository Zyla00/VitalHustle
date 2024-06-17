from django import forms
from .models import Mood, Day, Habit


class MoodForm(forms.ModelForm):
    class Meta:
        model = Mood
        fields = ['scale', 'slept_scale', 'emotions', 'note', 'updated_at']
    # search_fields = ['scale','slept_scale','emotions', 'note']

#
# class DayForm(forms.ModelForm):
#     list_display = ['user', 'mood', 'habit', 'date', 'updated_at']
#     # search_fields = ['user', 'mood', 'date']

class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ['coffee_amount', 'coffee_unit', 'cigarettes', 'cigarette_type', 'alcohol_amount', 'alcohol_unit', 'alcohol_type', 'exercise_minutes', 'exercise_unit', 'exercise_type', 'updated_at']
        # search_fields = ['coffee_amount' , 'coffee_unit', 'cigarettes', 'cigarette_type', 'alcohol_amount', 'alcohol_unit', 'alcohol_type', 'exercise_minutes', 'exercise_unit', 'exercise_type']
