from django.urls import path
from user.views import UserSignUpView, UserDeactivateView, UserInfo, UserLoginView, User_OtpVerifyView, AddressView, AddressDefaultView
urlpatterns = [
    path('signup', UserSignUpView.as_view()),
    path('activate', User_OtpVerifyView.as_view()),
    path('login', UserLoginView.as_view()),
    path('deactivate', UserDeactivateView.as_view()),
    path('userinfo', UserInfo.as_view()),
    path('address', AddressView.as_view()),
    path('address/<int:address_id>/default', AddressDefaultView.as_view()),
]
