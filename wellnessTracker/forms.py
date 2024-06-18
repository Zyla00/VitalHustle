from django import forms
from .models import Mood, Day, Habit

class MoodForm(forms.ModelForm):
    class Meta:
        model = Mood
        fields = ['scale', 'slept_scale', 'emotions', 'note']
        widgets = {
            'scale': forms.NumberInput(attrs={'required': False}),
            'slept_scale': forms.NumberInput(attrs={'required': False}),
            'emotions': forms.SelectMultiple(attrs={'required': False}),
            'note': forms.Textarea(attrs={'required': False}),
        }

    def __init__(self, *args, **kwargs):
        super(MoodForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False

class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ['coffee_amount', 'coffee_unit', 'cigarettes', 'cigarette_type', 'alcohol_amount', 'alcohol_unit', 'alcohol_type', 'exercise_minutes', 'exercise_unit', 'exercise_type']
        widgets = {
            'coffee_amount': forms.NumberInput(attrs={'required': False}),
            'coffee_unit': forms.Select(attrs={'required': False}),
            'cigarettes': forms.NumberInput(attrs={'required': False}),
            'cigarette_type': forms.Select(attrs={'required': False}),
            'alcohol_amount': forms.NumberInput(attrs={'required': False}),
            'alcohol_unit': forms.Select(attrs={'required': False}),
            'alcohol_type': forms.SelectMultiple(attrs={'required': False}),
            'exercise_minutes': forms.NumberInput(attrs={'required': False}),
            'exercise_unit': forms.Select(attrs={'required': False}),
            'exercise_type': forms.SelectMultiple(attrs={'required': False}),
        }

    def __init__(self, *args, **kwargs):
        super(HabitForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False
