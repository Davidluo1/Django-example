from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from products.models import Categories
from rest_framework.permissions import IsAuthenticated
from django.core.paginator import Paginator



class FetchAllCategoriesView(APIView):
    """Fetch all categories for user"""
    permission_classes = [(IsAuthenticated)]

    def get(self, request):
        user = request.user
        # find the category object that is not deleted in the database
        category_qs = Categories.objects.filter(is_deleted = False)
        # user input page number, default as page 1
        page = request.GET.get("p", 1)
        # user input total size of the category, default as 10
        psz = request.GET.get("psz", 10)
        # get total context of data, count, total_page_number
        object_list = paginator_object.page(page) 
        # actual data of paginated form
        paginator_object = Paginator(category_qs, psz) 
        # import pdb; pdb.set_trace()
        page_info = {"count" : paginator_object.count, "total_pages" : paginator_object.num_pages, "cur_page" : page}
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
            resp.append({"id" : data.id, "name" : data.name, "description" : data.description})
            
        return Response({"page_info" : page_info, "data" : resp}, status = 200)
    
    
    