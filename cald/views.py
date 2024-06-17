from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class CaldView(LoginRequiredMixin, TemplateView):
    template_name = 'calendar.html'
    login_url = '/login/'
    redirect_field_name = 'next'
