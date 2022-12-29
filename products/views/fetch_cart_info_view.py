from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from products.models import UserCart, Products
from rest_framework.permissions import IsAuthenticated
from django.db import transaction
from django.core.paginator import Paginator


# create a functionality to set default address
# provide a nickname to address


class FetchCartDataView(APIView):
    """Add address for user"""
    permission_classes = [(IsAuthenticated)]

    def get(self, request):
        user = request.user
        category_qs = UserCart.objects.filter(user = user)
        resp = []
        total_cost = 0
        for data in category_qs:
            product_cost = float(data.quantity )* float(data.product.price)
            total_cost+=product_cost
            resp.append({"id" : data.id, "quantity" : data.quantity,"name" : data.product.name, "product_image" : data.product.image, "price" : data.product.price})
            
        return Response({"total_cost" : total_cost, "data" : resp}, status = 200)