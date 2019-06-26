import json
import traceback
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from manage_resources.models import *


def subcategory_landing_screen(request):
    category = Category.objects.filter(is_deleted=False)
    data = {'category_data': category}
    return render(request, "manage_resources/subcategory.html", data)


def load_subcategory_table(request):
    try:
        print("Request In | manage_resources | subcategory.py | load_subcategory_table", request.user)
        dataList = []

        # column = request.GET.get('order[0][column]')
        # searchTxt = request.GET.get('search[value]')
        # order = ""
        # if request.GET.get('order[0][dir]') == 'desc':
        #     order = "-"
        # list = ['bill_cycle__bill_cycle_code', 'bill_cycle__bill_cycle_name']
        # column_name = order + list[int(column)]
        # start = request.GET.get('start')
        # length = int(request.GET.get('length')) + int(request.GET.get('start'))

        subcategory_detail = SubCategory.objects.filter(is_deleted=False)

        total_record = subcategory_detail.count()
        # branddetail = brand_detail.order_by(column_name)[start:length]

        for mru in subcategory_detail:
            tempList = []

            tempList.append('Demo')
            tempList.append('Demo')
            tempList.append('Demo')
            tempList.append('Demo')
            tempList.append('Demo')
            tempList.append('Demo')
            tempList.append('Demo')
            dataList.append(tempList)

        data = {'iTotalRecords': total_record, 'iTotalDisplayRecords': total_record, 'aaData': dataList}
    except Exception as exc:
        print('exception ', str(traceback.print_exc()))
        print("Exception In | manage_resources | subcategory.py | load_subcategory_table", exc)
        data = {'iTotalRecords': 0, 'iTotalDisplayRecords': 0, 'aaData': []}
    return HttpResponse(json.dumps(data), content_type='application/json')


@csrf_exempt
def add_new_sub_category(request):
    try:
        print("Request In | manage_resources | subcategory.py | add_new_sub_category", request.user)
        # SubCategory(
        #     category_name=request.POST.get('sub_cat_name'),
        #     category_description=request.POST.get('sub_cat_description'),
        #     category_image=request.FILES['sub_cat_image'],
        #     category_id=request.POST.get('category_fk'),
        #
        # ).save()
        data = {'success': 'true'}
    except Exception as exc:
        print('exception ', str(traceback.print_exc()))
        print("Exception In | manage_resources | subcategory.py | add_new_sub_category", exc)
        data = {'error': 'Error Occurred'}
    return HttpResponse(json.dumps(data), content_type='application/json')
