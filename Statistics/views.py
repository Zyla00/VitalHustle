from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class StatisticsView(LoginRequiredMixin, TemplateView):
    template_name = 'Statistics.html'
    login_url = '/login/'
    redirect_field_name = 'next'
