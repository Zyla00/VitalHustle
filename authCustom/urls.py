from django.urls import path
from .views import CustomLoginView, CustomLogoutView, RegisterView, CustomPasswordChangeView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('edit-password/', CustomPasswordChangeView.as_view(), name='edit-password//'),
]
