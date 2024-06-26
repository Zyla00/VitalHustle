from django.views.generic import ListView
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
import datetime
from django.http import HttpResponse
from django.views import View
from openpyxl import Workbook
from django.shortcuts import render
from django.http import JsonResponse
from wellnessTracker.models import Day, MoodScale, MoodEmotion, MoodNote, Sleep, CoffeHabit, CigaretteHabit, Sports, AlcoholHabit
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

class CaldView(LoginRequiredMixin, ListView):
    template_name = 'calendar.html'
    login_url = '/login/'
    redirect_field_name = 'next'
    model = Day
    context_object_name = 'days'
    paginate_by = 12

    def get_queryset(self):
        queryset = Day.objects.filter(user=self.request.user).order_by('-date')
        return queryset


@login_required
@require_http_methods(["GET", "POST"])
def load_data_view(request):
    if request.method == 'POST':
        user = request.user

        mood_scale = MoodScale.objects.create(scale=5)
        mood_emotion = MoodEmotion.objects.create(emotions=['happy', 'relaxed'])
        mood_note = MoodNote.objects.create(note='A good day')
        sleep = Sleep.objects.create(slept_scale=8.0)
        coffee_habit = CoffeHabit.objects.create(coffee_amount=2, coffee_unit='ml')
        cigarette_habit = CigaretteHabit.objects.create(cigarettes=0, cigarette_type='none')
        alcohol_habit = AlcoholHabit.objects.create(alcohol_amount=0, alcohol_unit='ml', alcohol_type=[])
        sports = Sports.objects.create(exercise_times=30, exercise_unit='minutes', exercise_type=['running'])

        today = datetime.date.today()

        day = Day.objects.create(
            user=user,
            mood_scale=mood_scale,
            mood_emotion=mood_emotion,
            mood_note=mood_note,
            sleep=sleep,
            coffee_habit=coffee_habit,
            cigarette_habit=cigarette_habit,
            alcohol_habit=alcohol_habit,
            sports=sports,
            date=today
        )

        return JsonResponse({'success': True, 'day': {
            'id': day.id,
            'date': day.date.strftime('%d-%m-%Y'),
            'mood_scale': mood_scale.scale,
            'emotions': mood_emotion.emotions,
            'note': mood_note.note,
            'slept_scale': sleep.slept_scale,
            'coffee_amount': coffee_habit.coffee_amount,
            'coffee_unit': coffee_habit.coffee_unit,
            'cigarettes': cigarette_habit.cigarettes,
            'cigarette_type': cigarette_habit.cigarette_type,
            'alcohol_amount': alcohol_habit.alcohol_amount,
            'alcohol_unit': alcohol_habit.alcohol_unit,
            'alcohol_type': alcohol_habit.alcohol_type,
            'exercise_times': sports.exercise_times,
            'exercise_unit': sports.exercise_unit,
            'exercise_type': sports.exercise_type
        }})
    else:
        return render(request, 'calendar.html')
