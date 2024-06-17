from django.urls import path
from .views import CaldView

urlpatterns = [
    path('cald/', CaldView.as_view(), name='cald-view'),
]
