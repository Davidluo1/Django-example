from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from products.models import  Products, UserCart
from rest_framework.permissions import IsAuthenticated
from django.db import transaction
from utils.error_msg import ACCESS_DENIED_MGS, CART_ITEM_UPDATED, DELETE_ITEM_MSG


class UpdateProductToCartView(APIView):
    """Update product quantity for user"""
    permission_classes = [(IsAuthenticated)]

    @transaction.atomic
    def post(self, request, product_id):
        user = request.user
        print(user)
        if Products.objects.filter(id = product_id).exists():
            # if this data with this user_id exists update the count
            cart_qs = UserCart.objects.filter(user = user, product_id= product_id)
            if cart_qs.exists():
                quantity = cart_qs[0].quantity
                UserCart.objects.filter(user = user, product_id= product_id).update(quantity = quantity+1)
                cart_qs = cart_qs[0]
            else:
                cart_qs = UserCart.objects.create(user = user, product_id= product_id)
            return Response({"id" : cart_qs.id, "name" : cart_qs.product.name}, status = 200)
        else:
            return Response({"msg" : "Invalid product"}, status = 400)
        
    
    @transaction.atomic
    def put(self, request, product_id):
        user = request.user
        if Products.objects.filter(id = product_id).exists():
            cart_qs = UserCart.objects.filter(user = user, product_id= product_id)
            if cart_qs.exists():
                quantity = request.GET.get('q',None)
                cart_qs.update(quantity = quantity)
                return Response(CART_ITEM_UPDATED, status = 200)
            else:
                return Response(ACCESS_DENIED_MGS, status = 400)
        else:
            return Response({"msg" : "Invalid product"}, status = 400)
        
    @transaction.atomic
    def delete(self, request, product_id):
        user = request.user
        # check if product exist
        if Products.objects.filter(id = product_id).exists():
            cart_qs = UserCart.objects.filter(user = user, product_id= product_id)
            # check if product exist in cart
            if cart_qs.exists():
                cart_qs.delete()
                return Response(DELETE_ITEM_MSG, status = 200)
            else:
                return Response(ACCESS_DENIED_MGS, status = 400)
        else:
            return Response({"msg" : "Invalid product"}, status = 400)