from django.urls import path
from . import views
from user.views import UserSignUpView

urlpatterns = [
    path('signup', UserSignUpView.as_view()),
    
]