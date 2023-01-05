from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from order.models import Order, OrderProducts
from products.models import UserCart, Products
from rest_framework.permissions import IsAuthenticated
from django.db import transaction
from order.serializer import PlaceOrderRequest


class PlaceOrderView(APIView):
    """Add order for user"""
    permission_classes = [(IsAuthenticated)]

    @transaction.atomic
    def post(self, request):
        user = request.user
        req_data = request.data
        request_data = PlaceOrderRequest(data = req_data)
        _ = request_data.is_valid(raise_exception = True)
        req_data = request_data.validated_data
        # create a order list for user
        qs = Order.objects.create(user = user, billing_address = req_data["billing_address"], shipping_address = req_data["shipping_address"])
        # filter only user's cart list
        cart_qs = UserCart.objects.filter(user = user)
        total_cost = 0
        if not cart_qs:
            return Response({"msg":"The cart is empty"})
        # calculate the total cost of the user cart list by each item, and create a order summary list
        for item in cart_qs:
            cost = float(item.product.price) * float(item.quantity)
            total_cost+=cost
            op_qs = OrderProducts.objects.create(order = qs, product = item.product, cost = item.product.price, quantity = item.quantity)
        # delete all item in the user cart
        UserCart.objects.filter(user = user).delete()
        return Response({"total_cost" : total_cost, "msg" : "Order placed"}, status = status.HTTP_200_OK)
    
    def get(self, request):
        user = request.user
        order_qs = Order.objects.filter(user=user)
        resp = []
        for order in order_qs:
            resp.append({"id" : order.id})
            op_qs = OrderProducts.objects.filter(order=order)
            op_resp = []
            for op in op_qs:
                product_qs = Products.objects.filter(id=op.product.id)
                op_resp.append({"id":product_qs[0].id, "name":product_qs[0].name, "quantity":op.quantity})
            resp.append({"id":order.id, "data":op_resp})
        return Response({"msg" : resp}, status = status.HTTP_200_OK)