from django import forms
from datetime import date
from decimal import Decimal
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
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Select a date'
        })
    )
    mood_scale = forms.IntegerField(
        label='Mood scale',
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
        label='Sleep scale',
        required=False,
        widget=forms.NumberInput(
            attrs={'class': 'form-control', 'step': 0.5, 'min': 0, 'max': 24, 'placeholder': 'Slept Scale'})
    )
    coffee_amount = forms.IntegerField(
        label='Coffee amount',
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Coffee Amount'})
    )
    coffee_unit = forms.ChoiceField(
        label='Coffee amount unit',
        required=False,
        choices=CoffeHabitForm.Meta.model.UNIT_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Coffee Unit'})
    )
    cigarettes = forms.IntegerField(
        label='Cigarette amount',
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Cigarettes'})
    )
    cigarette_type = forms.ChoiceField(
        label='Cigarette type',
        required=False,
        choices=CigaretteHabitForm.Meta.model.CHOICES,
        widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Cigarette Type'})
    )
    alcohol_amount = forms.IntegerField(
        label='Alcohol amount',
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Alcohol Amount'})
    )
    alcohol_unit = forms.ChoiceField(
        label='Alcohol amount unit',
        required=False,
        choices=AlcoholHabitForm.Meta.model.UNIT,
        widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Alcohol Unit'})
    )
    alcohol_type = forms.MultipleChoiceField(
        label='Alcohol type',
        required=False,
        choices=AlcoholHabitForm.Meta.model.CHOICES,
        widget=forms.SelectMultiple(attrs={'class': 'form-control select2'})
    )
    exercise_times = forms.IntegerField(
        label='Exercise time',
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Exercise Times'})
    )
    exercise_unit = forms.ChoiceField(
        label='Exercise time unit',
        required=False,
        choices=SportsForm.Meta.model.UNIT,
        widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Exercise Unit'})
    )
    exercise_type = forms.MultipleChoiceField(
        label='Exercise type',
        required=False,
        choices=SportsForm.Meta.model.CHOICES,
        widget=forms.SelectMultiple(attrs={'class': 'form-control select2'})
    )

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.instance_id = kwargs.pop('instance_id', None)
        super(CombinedDayForm, self).__init__(*args, **kwargs)

    def clean_mood_scale(self):
        mood_scale = self.cleaned_data.get('mood_scale')
        if mood_scale is not None:
            if not 0 <= mood_scale <= 10:
                raise forms.ValidationError('Mood scale must be between 0 and 10.')
        return mood_scale

    def clean_slept_scale(self):
        slept_scale = self.cleaned_data.get('slept_scale')
        if slept_scale is not None:
            half_step = Decimal('0.5')
            if slept_scale % half_step != 0 or not Decimal('0.0') <= slept_scale <= Decimal('10'):
                raise forms.ValidationError('Slept scale must be a multiple of 0.5 and between 0 and 10.')
        return slept_scale

    def clean_date(self):
        date_value = self.cleaned_data.get('date')
        if not self.instance_id:
            if not date_value:
                raise forms.ValidationError('Date is required')
            elif date_value > date.today():
                raise forms.ValidationError('The date cannot be in the future.')
            elif Day.objects.filter(user=self.user, date=date_value).exists():
                raise forms.ValidationError('An entry for this date already exists.')

        return date_value

    def clean(self):
        cleaned_data = super().clean()

        # Retrieve data from cleaned_data
        cigarettes = cleaned_data.get('cigarettes')
        cigarette_type = cleaned_data.get('cigarette_type')
        alcohol_amount = cleaned_data.get('alcohol_amount')
        alcohol_type = cleaned_data.get('alcohol_type')
        exercise_times = cleaned_data.get('exercise_times')
        exercise_type = cleaned_data.get('exercise_type')

        if cigarette_type and cigarette_type != 'choose-type' and (cigarettes is None or cigarettes == 0):
            self.add_error('cigarettes', 'You must specify the amount of cigarettes if you select a cigarette type.')

        if alcohol_type and (alcohol_amount is None or alcohol_amount == 0):
            self.add_error('alcohol_amount', 'You must specify the amount of alcohol if you select an alcohol type.')

        if exercise_type and (exercise_times is None or exercise_times == 0):
            self.add_error('exercise_times',
                           'You must specify the number of exercise times if you select an exercise type.')

        return cleaned_data

class DateRangeForm(forms.Form):
    date_from = forms.DateField(
        label='Start Date',
        widget=forms.DateInput(attrs={
            'type': 'date',
            'id': 'date_from_picker'
        })
    )
    date_to = forms.DateField(
        label='End Date',
        widget=forms.DateInput(attrs={
            'type': 'date',
            'id': 'date_to_picker'
        })
    )

    def clean(self):
        cleaned_data = super().clean()
        date_from = cleaned_data.get('date_from')
        date_to = cleaned_data.get('date_to')

        if not date_from or not date_to:
            raise forms.ValidationError('Both start and end dates are required.')

        if date_to < date_from:
            raise forms.ValidationError('The end date cannot be earlier than the start date.')

        return cleaned_data


class UploadFileForm(forms.Form):
    file = forms.FileField()