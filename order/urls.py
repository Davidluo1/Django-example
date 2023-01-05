from django.urls import path
from order.views import PlaceOrderView

urlpatterns = [
    path('', PlaceOrderView.as_view()),
]