from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from products.models import  Products, UserCart, ProductReview
from order.models import Order, OrderProducts
from rest_framework.permissions import IsAuthenticated
from django.db import transaction
from products.serializer import AddProductReviewRequest


class AddProductReviewView(APIView):
    """Add product review"""
    permission_classes = [(IsAuthenticated)]

    @transaction.atomic
    def post(self, request, product_id):
        user = request.user
        req_data = request.data
        request_data = AddProductReviewRequest(data = req_data)
        _ = request_data.is_valid(raise_exception = True)
        req_data = request_data.validated_data
        if Products.objects.filter(id = product_id).exists():
            # if this data with this user_id exists update the count
            order_qs = OrderProducts.objects.filter(product_id = product_id)
            if order_qs.exists():
                for orders in order_qs:
                    if orders.order.user == user:
                        ProductReview.objects.create(rating = req_data["rating"], comment = req_data["comment"], user = user, product_id = product_id)
                        return Response({"msg" : "Review added"}, status = 200)
                return Response({"msg" : "Product not bought"}, status = 400)
            else:
                return Response({"msg" : "Product not bought"}, status = 400)
            # return Response({"id" : cart_qs.id, "name" : cart_qs.product.name}, status = 200)
        else:
            return Response({"msg" : "Invalid product"}, status = 400)

        
    def get(self, request, product_id):
        qs = ProductReview.objects.filter(product_id= product_id)
        resp = []
        for reviews in qs:
            resp.append({"rating" : reviews.rating, "comment" : reviews.comment, "user" : reviews.user.first_name})

        return Response({"data" : resp}, status = status.HTTP_200_OK)


# product_id is valid  -- Done
# user has bought that product -- 
# Add commment and review