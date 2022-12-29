from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from products.models import Products, Categories
from rest_framework.permissions import IsAuthenticated
from django.core.paginator import Paginator



class FetchAllProductsCategoryView(APIView):
    """Fetch category for user"""
    permission_classes = [(IsAuthenticated)]

    def get(self, request, category_id):
        user = request.user
        # user input page number, default as page 1
        page = request.GET.get("p", 1)
        # user input total size of the category, default as 10
        page_size = request.GET.get("psz", 10)
        name = request.GET.get('name', None)
        price_st = request.GET.get('price_st', None)
        price_end = request.GET.get('price_end', None)
        if name:
            # find the category object that is not deleted in the database
            category_qs = Categories.objects.filter(is_deleted=False, name__icontains=name)
            category = category_qs[0]
        category_qs = Products.objects.filter(is_deleted=False, category_id=category_id)
        if price_st:
            category_qs = category_qs.filter(price__gte=int(price_st))
        if price_end:
            category_qs = category_qs.filter(price__lte=int(price_end))
        # actual data of paginated form 
        paginator_object = Paginator(category_qs, page_size)
        # get total context of data, count, total_page_number
        object_list = paginator_object.page(page) 
        # import pdb; pdb.set_trace()
        page_info = {"total_items" : paginator_object.count, "total_pages" : paginator_object.num_pages, "cur_page" : page}
        # has_next check next avaliable
        if object_list.has_next():
            page_info["next"] = object_list.next_page_number()
        else:
            page_info["next"] = None
        # has_previous check previous avaliable
        if object_list.has_previous():
            page_info["previous"] = object_list.previous_page_number()
        else:
            page_info["previous"] = None

        resp = []
        for data in object_list:
            resp.append({"id" : data.id, "name" : data.name, "price" : data.price})
            
        return Response({"page_info" : page_info, "category" : category.name, "description" : category.description,
                         "data" : resp}, status = 200)
    
    
    