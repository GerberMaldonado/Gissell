from django.urls import path
from .views import SignUpView
from django.contrib.auth.decorators import login_required

app_name = 'registro'

urlpatterns = [
    path('signup/', login_required(SignUpView.as_view()), name="signup")
]