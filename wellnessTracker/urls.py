from django.urls import path
from .views import (HomeView, DayCreateEditView, DayDeleteView, FetchPreviousDayView, ExportDaysExcelView,
                    ProcessDaysExportView, upload_file)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('day/create/', DayCreateEditView.as_view(), name='day-create-edit'),
    path('day/delete/<int:pk>', DayDeleteView.as_view(), name='day-delete'),
    path('day/previous/', FetchPreviousDayView.as_view(), name='fetch-next-day'),
    path('day/edit/<int:pk>/', DayCreateEditView.as_view(), name='day-edit'),
    path('days/prepare-export/', ProcessDaysExportView.as_view(), name='days-export'),
    path('upload/', upload_file, name='upload_file'),

    path('days/export/', ExportDaysExcelView.as_view(), name='prepare-days-export'),
]
