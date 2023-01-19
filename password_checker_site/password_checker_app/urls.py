from django.urls import path
from password_checker_app.views import PasswordCheckerView

urlpatterns = [
    path('', PasswordCheckerView.as_view(), name='password_checker'),
]