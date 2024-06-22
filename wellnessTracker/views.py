from django.http import JsonResponse
from django.db import transaction
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from .forms import MoodScaleForm, MoodEmotionForm, MoodNoteForm, CoffeHabitForm, CigaretteHabitForm, SportsForm, AlcoholHabitForm, SleepForm
from .models import MoodScale, MoodEmotion, MoodNote, Sleep, CoffeHabit, CigaretteHabit, Sports, AlcoholHabit, Day

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'homepage.html'
    login_url = '/login/'
    redirect_field_name = 'next'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        day = self.get_or_create_day(user)
        context.update({
            'mood_scale_form': MoodScaleForm(instance=day.mood_scale),
            'mood_emotion_form': MoodEmotionForm(instance=day.mood_emotion),
            'mood_note_form': MoodNoteForm(instance=day.mood_note),
            'sleep_form': SleepForm(instance=day.sleep),
            'coffee_form': CoffeHabitForm(instance=day.coffee_habit),
            'cigarette_form': CigaretteHabitForm(instance=day.cigarette_habit),
            'alcohol_form': AlcoholHabitForm(instance=day.alcohol_habit),
            'sports_form': SportsForm(instance=day.sports),
        })
        return context

    @staticmethod
    def get_or_create_day(user):
        today = timezone.now().date()
        with transaction.atomic():
            day, created = Day.objects.select_related(
                'mood_scale',
                'mood_emotion',
                'mood_note',
                'sleep',
                'coffee_habit',
                'cigarette_habit',
                'alcohol_habit',
                'sports'
            ).get_or_create(user=user, date=today)

            if created:
                day.mood_scale = MoodScale.objects.create()
                day.mood_emotion = MoodEmotion.objects.create()
                day.mood_note = MoodNote.objects.create()
                day.sleep = Sleep.objects.create()
                day.coffee_habit = CoffeHabit.objects.create()
                day.cigarette_habit = CigaretteHabit.objects.create()
                day.alcohol_habit = AlcoholHabit.objects.create()
                day.sports = Sports.objects.create()
                day.save()
            elif not all([
                day.mood_scale,
                day.mood_emotion,
                day.mood_note,
                day.sleep,
                day.coffee_habit,
                day.cigarette_habit,
                day.alcohol_habit,
                day.sports
            ]):
                if not day.mood_scale:
                    day.mood_scale = MoodScale.objects.create()
                if not day.mood_emotion:
                    day.mood_emotion = MoodEmotion.objects.create()
                if not day.mood_note:
                    day.mood_note = MoodNote.objects.create()
                if not day.sleep:
                    day.sleep = Sleep.objects.create()
                if not day.coffee_habit:
                    day.coffee_habit = CoffeHabit.objects.create()
                if not day.cigarette_habit:
                    day.cigarette_habit = CigaretteHabit.objects.create()
                if not day.alcohol_habit:
                    day.alcohol_habit = AlcoholHabit.objects.create()
                if not day.sports:
                    day.sports = Sports.objects.create()
                day.save()

        return day

    def post(self, request, *args, **kwargs):
        user = request.user
        day = self.get_or_create_day(user)
        form_id_list = request.POST.getlist('form_id')
        form_id = form_id_list[0] if form_id_list else None

        if form_id == 'mood-scale-form':
            form = MoodScaleForm(request.POST, instance=day.mood_scale)
        elif form_id == 'mood-emotions-form':
            form = MoodEmotionForm(request.POST, instance=day.mood_emotion)
        elif form_id == 'mood-note-form':
            form = MoodNoteForm(request.POST, instance=day.mood_note)
        elif form_id == 'sleep-form':
            form = SleepForm(request.POST, instance=day.sleep)
        elif form_id == 'coffee-form':
            form = CoffeHabitForm(request.POST, instance=day.coffee_habit)
        elif form_id == 'cigarette-form':
            form = CigaretteHabitForm(request.POST, instance=day.cigarette_habit)
        elif form_id == 'alcohol-form':
            form = AlcoholHabitForm(request.POST, instance=day.alcohol_habit)
        elif form_id == 'sports-form':
            form = SportsForm(request.POST, instance=day.sports)
        else:
            return

        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False})
