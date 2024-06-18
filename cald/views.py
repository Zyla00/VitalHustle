from django.views.generic import ListView
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from wellnessTracker.models import Day

class CaldView(LoginRequiredMixin, ListView):
    template_name = 'calendar.html'
    login_url = '/login/'
    redirect_field_name = 'next'
    model = Day
    context_object_name = 'days'

    def get_queryset(self):
        return Day.objects.filter(user=self.request.user).order_by('-date')
