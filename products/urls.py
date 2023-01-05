from django.urls import path
from products.views import (FetchAllCategoriesView, FetchAllProductsCategoryView, FetchCategoriesView,
                            UpdateProductToCartView, FetchCartDataView, AddProductReviewView, AddProductImage)

urlpatterns = [
    path('all_category', FetchAllCategoriesView.as_view()),
    path('category', FetchCategoriesView.as_view()),
    path('category/<int:category_id>/product', FetchAllProductsCategoryView.as_view()),
    path('product/<int:product_id>/cart', UpdateProductToCartView.as_view()),
    path('product/<int:product_id>/image', AddProductImage.as_view()),
    path('cart', FetchCartDataView.as_view()),
    path('review/<int:cart_id>', AddProductReviewView.as_view()),
]