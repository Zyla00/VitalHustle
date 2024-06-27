from django.urls import path
from .views import StatisticsView, mood_chart, mood_scale_data

urlpatterns = [
    path('statistics/', StatisticsView.as_view(), name='Statistics-view'),
    path('mood_chart/', mood_chart, name='mood_chart'),
    path('api/mood_scale_data/', mood_scale_data, name='mood_scale_data'),

]
