import json
import traceback

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from manage_resources.models import Brand


def brand_landing_screen(request):
    return render(request, "manage_resources/Brand.html")


def load_brand_table(request):
    try:
        print("Request In | manage_resources | brand.py | load_brand_table", request.user)
        dataList = [] 
        # Todo server side pagination start
        column = request.GET.get('order[0][column]')
        searchtxt = request.GET.get('search[value]')
        order = ""
        if request.GET.get('order[0][dir]') == 'desc':
            order = "-"
        list = ['id', 'brand_name']
        column_name = order + list[int(column)]
        start = int(request.GET.get('start'))
        length = int(request.GET.get('length')) + start
        # Todo server side pagination end

        brand_detail = Brand.objects.filter((Q(id__icontains=searchtxt) | Q(brand_name__icontains=searchtxt)),
                                            is_deleted=False)
        total_record = brand_detail.count()
        branddetail = brand_detail.order_by(column_name)[start:length]

        for brand in branddetail:
            tempList = []
            action = '<div class="btn-group"><a onclick="edit_brand_data(' + str(
                brand.id) + ')" data-toggle="tooltip" title="Edit" class="btn btn-xs btn-default">' \
                            '<i class="fa fa-pencil"></i></a><a onclick="delete_brand_detail(' + str(
                brand.id) + ')" data-toggle="tooltip" title="Delete" class="btn btn-xs btn-danger">' \
                            '<i class="fa fa-times"></i></a></div>'
            tempList.append(brand.id)
            tempList.append(brand.brand_name)
            tempList.append('<img src="'+brand.brand_image.url+'" alt="avatar" class="img-circle" height="50" width="50">')
            if brand.status_choice:
                tempList.append(
                    '<label class="switch switch-primary"><input type="checkbox" onclick="change_brand_status(' + str(
                        brand.id) + ')" id="brand-status" checked ><span></span></label>')
            else:
                tempList.append(
                    '<label class="switch switch-primary"><input type="checkbox" onclick="change_brand_status(' + str(
                        brand.id) + ')" id="brand-status"><span></span></label>')

            tempList.append(action)
            dataList.append(tempList)

        data = {'iTotalRecords': total_record, 'iTotalDisplayRecords': total_record, 'aaData': dataList}
    except Exception as exc:
        print('exception ', str(traceback.print_exc()))
        print("Exception In | manage_resources | brand.py | load_brand_table", exc)
        data = {'iTotalRecords': 0, 'iTotalDisplayRecords': 0, 'aaData': []}
    return HttpResponse(json.dumps(data), content_type='application/json')


@csrf_exempt
def add_new_brand(request):
    try:
        print("Request In | manage_resources | brand.py | add_new_brand", request.user)
        Brand(
            brand_name=request.POST.get('brand_name'),
            brand_image=request.FILES['brand_image']
        ).save()
        data = {'success': 'true'}
    except Exception as exc:
        print('exception ', str(traceback.print_exc()))
        print("Exception In | manage_resources | brand.py | add_new_brand", exc)
        data = {'error': 'Error Occurred'}
    return HttpResponse(json.dumps(data), content_type='application/json')


def change_brand_status(request):
    try:
        print("Request In | manage_resources | brand.py | change_brand_status", request.user)
        brand_obj = Brand.objects.get(id=request.GET.get('brand_id'))
        brand_status = request.GET.get('brand_status')
        if brand_status == 'true':
            brand_obj.status_choice = True
        else:
            brand_obj.status_choice = False

        brand_obj.save()
        data = {'success': 'true'}
    except Exception as exc:
        print('exception ', str(traceback.print_exc()))
        print("Exception In | manage_resources | brand.py | change_brand_status", exc)
        data = {'error': 'Error Occurred'}
    return HttpResponse(json.dumps(data), content_type='application/json')


def delete_brand_detail(request):
    try:
        print("Request In | manage_resources | brand.py | delete_brand_detail", request.user)
        brand_obj = Brand.objects.get(id=request.GET.get('brand_id'))
        brand_obj.is_deleted = True
        brand_obj.save()
        data = {'success': 'true'}
    except Exception as exc:
        print('exception ', str(traceback.print_exc()))
        print("Exception In | manage_resources | brand.py | delete_brand_detail", exc)
        data = {'error': 'Error Occurred'}
    return HttpResponse(json.dumps(data), content_type='application/json')


def edit_brand_data(request):
    try:
        print("Request In | manage_resources | brand.py | edit_brand_data", request.user)
        brand_obj = Brand.objects.get(id=request.GET.get('brand_id'))
        data = {'success': 'true', 'brand_name': brand_obj.brand_name}
    except Exception as exc:
        print('exception ', str(traceback.print_exc()))
        print("Exception In | manage_resources | brand.py | edit_brand_data", exc)  
        data = {'error': 'Error Occurred'}
    return HttpResponse(json.dumps(data), content_type='application/json')


@csrf_exempt
def update_brand_data(request):
    try:
        print("Request In | manage_resources | brand.py | edit_brand_data", request.user)
        brand_obj = Brand.objects.get(id=request.POST.get('brand_id'))
        brand_obj.brand_name = request.POST.get('brand_name')
        try:
            brand_obj.brand_image = request.FILES['brand_image']
        except Exception as exc:
            print("Exception in ", exc)
        brand_obj.save()
        data = {'success': 'true'}
    except Exception as exc:
        print('exception ', str(traceback.print_exc()))
        print("Exception In | manage_resources | brand.py | edit_brand_data", exc)
        data = {'error': 'Error Occurred'}
    return HttpResponse(json.dumps(data), content_type='application/json')