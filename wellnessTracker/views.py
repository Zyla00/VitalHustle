from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from .forms import MoodForm, HabitForm
from .models import Day, Mood, Habit

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'homepage.html'
    login_url = '/login/'
    redirect_field_name = 'next'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        day = self.get_day(user)
        context['user'] = user
        context['mood_form'] = MoodForm(instance=day.mood)
        context['habit_form'] = HabitForm(instance=day.habit)
        return context

    @staticmethod
    def get_day(user):
        today = timezone.now().date()
        try:
            day = Day.objects.get(user=user, date=today)
        except Day.DoesNotExist:
            mood = Mood.objects.create()
            habit = Habit.objects.create()
            day = Day.objects.create(user=user, date=today, mood=mood, habit=habit)
        return day

    def post(self, request, *args, **kwargs):
        user = request.user
        day = self.get_day(user)
        form_id_list = request.POST.getlist('form_id')
        form_id = form_id_list[0] if form_id_list else None

        if form_id == 'mood-form':
            mood_form = MoodForm(request.POST, instance=day.mood)
            if mood_form.is_valid():
                mood = mood_form.save()
                day.mood = mood
            else:
                # Print form errors to debug why the form is not valid
                print('Mood form errors:', mood_form.errors)

        elif form_id == 'habit-form':
            habit_form = HabitForm(request.POST, instance=day.habit)
            if habit_form.is_valid():
                habit = habit_form.save()
                day.habit = habit
            else:
                # Print form errors to debug why the form is not valid
                print('Habit form errors:', habit_form.errors)

        day.save()

        return JsonResponse({'success': True})
