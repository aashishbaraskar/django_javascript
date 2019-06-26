import json
import traceback
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from manage_resources.models import Variant


def variant_landing_screen(request):
    return render(request, "manage_resources/variant.html")


def load_variant_table(request):
    try:
        print("Request In | manage_resources | variant.py | load_variant_table", request.user)
        dataList = []
        # Todo server side pagination start
        column = request.GET.get('order[0][column]')
        searchtxt = request.GET.get('search[value]')
        order = ""
        if request.GET.get('order[0][dir]') == 'desc':
            order = "-"
        list = ['id', 'variant_name']
        column_name = order + list[int(column)]
        start = int(request.GET.get('start'))
        length = int(request.GET.get('length')) + start
        # Todo server side pagination end

        variant_detail = Variant.objects.filter((Q(id__icontains=searchtxt) | Q(variant_name__icontains=searchtxt)), is_deleted=False) 
        total_record = variant_detail.count()
        variantdetail = variant_detail.order_by(column_name)[start:length]

        for variant in variantdetail:
            tempList = []
            action = '<div class="btn-group"><a onclick="edit_variant_data(' + str(
                variant.id) + ')" data-toggle="tooltip" title="Edit" class="btn btn-xs btn-default">' \
                            '<i class="fa fa-pencil"></i></a><a onclick="delete_variant_detail(' + str(
                variant.id) + ')" data-toggle="tooltip" title="Delete" class="btn btn-xs btn-danger">' \
                            '<i class="fa fa-times"></i></a></div>'
            tempList.append(variant.id)
            tempList.append(variant.variant_name)
            if variant.status_choice:
                tempList.append(
                    '<label class="switch switch-primary"><input type="checkbox" onclick="change_variant_status(' + str(
                        variant.id) + ')" id="variant-status" checked ><span></span></label>')
            else:
                tempList.append(
                    '<label class="switch switch-primary"><input type="checkbox" onclick="change_variant_status(' + str(
                        variant.id) + ')" id="variant-status"><span></span></label>')
            tempList.append(action)
            dataList.append(tempList)

        data = {'iTotalRecords': total_record, 'iTotalDisplayRecords': total_record, 'aaData': dataList}
    except Exception as exc:
        print('exception ', str(traceback.print_exc()))
        print("Exception In | manage_resources | variant.py | load_variant_table", exc)
        data = {'iTotalRecords': 0, 'iTotalDisplayRecords': 0, 'aaData': []}
    return HttpResponse(json.dumps(data), content_type='application/json')


@csrf_exempt
def add_new_variant(request):
    try:
        print("Request In | manage_resources | variant.py | add_new_variant", request.user)
        Variant(
            variant_name=request.POST.get('variant_name')
        ).save()
        data = {'success': 'true'}
    except Exception as exc:
        print('exception ', str(traceback.print_exc()))
        print("Exception In | manage_resources | variant.py | add_new_variant", exc)
        data = {'error': 'Error Occurred'}
    return HttpResponse(json.dumps(data), content_type='application/json')


def change_variant_status(request):
    try:
        print("Request In | manage_resources | variant.py | change_variant_status", request.user)
        variant_obj = Variant.objects.get(id=request.GET.get('variant_id'))
        variant_status = request.GET.get('variant_status')
        if variant_status == 'true':
            variant_obj.status_choice = True
        else:
            variant_obj.status_choice = False

        variant_obj.save()
        data = {'success': 'true'}
    except Exception as exc:
        print('exception ', str(traceback.print_exc()))
        print("Exception In | manage_resources | variant.py | change_variant_status", exc)
        data = {'error': 'Error Occurred'}
    return HttpResponse(json.dumps(data), content_type='application/json')

def delete_variant_detail(request):
    try:
        print("Request In | manage_resources | variant.py | delete_variant_detail", request.user)
        variant_obj = Variant.objects.get(id=request.GET.get('variant_id'))
        variant_obj.is_deleted = True
        variant_obj.save()
        data = {'success': 'true'}
    except Exception as exc:
        print('exception ', str(traceback.print_exc()))
        print("Exception In | manage_resources | variant.py | delete_variant_detail", exc)
        data = {'error': 'Error Occurred'}
    return HttpResponse(json.dumps(data), content_type='application/json')


def edit_variant_data(request): 
    try:
        print("Request In | manage_resources | variant.py | edit_variant_data", request.user)
        variant_obj = Variant.objects.get(id=request.GET.get('variant_id'))
        data = {'success': 'true', 'variant_name': variant_obj.variant_name}
    except Exception as exc:
        print('exception ', str(traceback.print_exc()))
        print("Exception In | manage_resources | variant.py | edit_variant_data", exc)
        data = {'error': 'Error Occurred'}
    return HttpResponse(json.dumps(data), content_type='application/json')

@csrf_exempt
def update_variant_data(request):
    try:
        print("Request In | manage_resources | variant.py | update_variant_data", request.user)
        id=request.POST.get('variant_id')
        name = request.POST.get('variant-name')
        print(f'hello - {id } -{name}')
        variant_obj = Variant.objects.get(id=request.POST.get('variant_id'))
        variant_obj.variant_name = request.POST.get('variant_name')
        variant_obj.save()
        data = {'success': 'true'}
    except Exception as exc:
        print('exception ', str(traceback.print_exc()))
        print("Exception In | manage_resources | variant.py | update_variant_data", exc)
        data = {'error': 'Error Occurred'}
    return HttpResponse(json.dumps(data), content_type='application/json')