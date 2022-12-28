from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from products.models import Categories
from rest_framework.permissions import IsAuthenticated
from django.core.paginator import Paginator



class FetchCategoriesView(APIView):
    """Fetch category for user"""
    permission_classes = [(IsAuthenticated)]

    def get(self, request):
        user = request.user
        name = request.GET.get('name', None)
        category_list = Categories.objects.filter(name=name, is_deleted=False)
        page = request.GET.get('p', 1)
        page_size = request.GET.get('ps', 10)
        category_list = paginator_object.page(page)
        paginator_object = Paginator(category_list, page_size)
        page_info = [{"num of items" : paginator_object.count, "total pages" : paginator_object.num_pages,
                      "current page" : paginator_object.page}]
        if category_list.has_next():
            page_info['next'] = category_list.next_page_number()
        page_info['next'] = None
        if category_list.has_previous():
            page_info['previous'] = category_list.previous_page_number()
        page_info['previous'] = None
        resp = []
        for item in category_list:
            resp.append({"id":item.id, "name":item.name, "description":item.description})
        
        return Response({"page_info":page_info, "data": resp }, status = 200)
    
    
    