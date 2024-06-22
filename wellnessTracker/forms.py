from django import forms
from .models import MoodScale, MoodEmotion, MoodNote, Sleep, CoffeHabit, CigaretteHabit, Sports, AlcoholHabit

class MoodScaleForm(forms.ModelForm):
    class Meta:
        model = MoodScale
        fields = ['scale']
        widgets = {
            'scale': forms.NumberInput(attrs={'step': 1, 'min': 0, 'max': 10, 'required': False}),
        }

    def __init__(self, *args, **kwargs):
        super(MoodScaleForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False

class MoodEmotionForm(forms.ModelForm):
    class Meta:
        model = MoodEmotion
        fields = ['emotions']
        widgets = {
            'emotions': forms.SelectMultiple(attrs={'required': False}),
        }

    def __init__(self, *args, **kwargs):
        super(MoodEmotionForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False

class MoodNoteForm(forms.ModelForm):
    class Meta:
        model = MoodNote
        fields = ['note']
        widgets = {
            'note': forms.Textarea(attrs={'required': False}),
        }

    def __init__(self, *args, **kwargs):
        super(MoodNoteForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False

class CoffeHabitForm(forms.ModelForm):
    class Meta:
        model = CoffeHabit
        fields = ['coffee_amount', 'coffee_unit']
        widgets = {
            'coffee_amount': forms.NumberInput(attrs={'required': False}),
            'coffee_unit': forms.Select(attrs={'required': False}),
        }

    def __init__(self, *args, **kwargs):
        super(CoffeHabitForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False

class CigaretteHabitForm(forms.ModelForm):
    class Meta:
        model = CigaretteHabit
        fields = ['cigarettes', 'cigarette_type']
        widgets = {
            'cigarettes': forms.NumberInput(attrs={'required': False}),
            'cigarette_type': forms.Select(attrs={'required': False}),
        }

    def __init__(self, *args, **kwargs):
        super(CigaretteHabitForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False

class SportsForm(forms.ModelForm):
    class Meta:
        model = Sports
        fields = ['exercise_times', 'exercise_unit', 'exercise_type']
        widgets = {
            'exercise_times': forms.NumberInput(attrs={'required': False}),
            'exercise_unit': forms.Select(attrs={'required': False}),
            'exercise_type': forms.SelectMultiple(attrs={'required': False}),
        }

    def __init__(self, *args, **kwargs):
        super(SportsForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False

class AlcoholHabitForm(forms.ModelForm):
    class Meta:
        model = AlcoholHabit
        fields = ['alcohol_amount', 'alcohol_unit', 'alcohol_type']
        widgets = {
            'alcohol_amount': forms.NumberInput(attrs={'required': False}),
            'alcohol_unit': forms.Select(attrs={'required': False}),
            'alcohol_type': forms.SelectMultiple(attrs={'required': False}),
        }

    def __init__(self, *args, **kwargs):
        super(AlcoholHabitForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False

class SleepForm(forms.ModelForm):
    class Meta:
        model = Sleep
        fields = ['slept_scale']
        widgets = {
            'slept_scale': forms.NumberInput(attrs={'step': 0.5, 'min': 0, 'max': 24, 'required': False}),
        }

    def __init__(self, *args, **kwargs):
        super(SleepForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False
