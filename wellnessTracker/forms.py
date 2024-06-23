from django import forms
from datetime import date
from .models import MoodScale, MoodEmotion, MoodNote, Sleep, CoffeHabit, CigaretteHabit, Sports, AlcoholHabit, Day


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


class CombinedDayForm(forms.Form):
    date = forms.DateField(
        label='Date',
        input_formats=['%d-%m-%Y'],
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Select a date'
        })
    )
    mood_scale = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(
            attrs={'class': 'form-control', 'step': 1, 'min': 0, 'max': 10, 'placeholder': 'Mood Scale'})
    )
    emotions = forms.MultipleChoiceField(
        required=False,
        choices=MoodEmotionForm.Meta.model.EMOTION_CHOICES,
        widget=forms.SelectMultiple(attrs={'class': 'form-control select2'})
    )
    note = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Note'})
    )
    slept_scale = forms.DecimalField(
        required=False,
        widget=forms.NumberInput(
            attrs={'class': 'form-control', 'step': 0.5, 'min': 0, 'max': 24, 'placeholder': 'Slept Scale'})
    )
    coffee_amount = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Coffee Amount'})
    )
    coffee_unit = forms.ChoiceField(
        required=False,
        choices=CoffeHabitForm.Meta.model.UNIT_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Coffee Unit'})
    )
    cigarettes = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Cigarettes'})
    )
    cigarette_type = forms.ChoiceField(
        required=False,
        choices=CigaretteHabitForm.Meta.model.CHOICES,
        widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Cigarette Type'})
    )
    alcohol_amount = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Alcohol Amount'})
    )
    alcohol_unit = forms.ChoiceField(
        required=False,
        choices=AlcoholHabitForm.Meta.model.UNIT,
        widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Alcohol Unit'})
    )
    alcohol_type = forms.MultipleChoiceField(
        required=False,
        choices=AlcoholHabitForm.Meta.model.CHOICES,
        widget=forms.SelectMultiple(attrs={'class': 'form-control select2'})
    )
    exercise_times = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Exercise Times'})
    )
    exercise_unit = forms.ChoiceField(
        required=False,
        choices=SportsForm.Meta.model.UNIT,
        widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Exercise Unit'})
    )
    exercise_type = forms.MultipleChoiceField(
        required=False,
        choices=SportsForm.Meta.model.CHOICES,
        widget=forms.SelectMultiple(attrs={'class': 'form-control select2'})
    )

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(CombinedDayForm, self).__init__(*args, **kwargs)

    def clean_date(self):
        date_value = self.cleaned_data.get('date')
        if date_value > date.today():
            raise forms.ValidationError('The date cannot be in the future.')
        if Day.objects.filter(user=self.user, date=date_value).exists():
            raise forms.ValidationError('An entry for this date already exists.')
        return date_value