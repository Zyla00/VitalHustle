from django.urls import path
from .views import CaldView, load_data_view


urlpatterns = [
    path('cald/', CaldView.as_view(), name='cald-view'),
    path('load-data/', load_data_view, name='load_data'),
]
