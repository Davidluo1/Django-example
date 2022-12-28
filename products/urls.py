from django.urls import path
from products.views import FetchAllCategoriesView, FetchCategoriesView


urlpatterns = [
    path('category', FetchAllCategoriesView.as_view()),
    path('category/product', FetchCategoriesView.as_view()),
]