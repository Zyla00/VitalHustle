from django.urls import path
from .views import HomeView, DayCreateEditView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('day-create/', DayCreateEditView.as_view(), name='day-create-edit'),
]
