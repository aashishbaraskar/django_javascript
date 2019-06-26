import json
import traceback
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from manage_resources.models import WastageType


# def wastageType_landing_screen(request):
#     wastageType_detail = WastageType.objects.filter(is_deleted=False)
#     print(f'Hello - {wastageType_detail}')
#     return render(request, "manage_resources/wastageType.html", {'wastageType_detail': wastageType_detail})

def wastageType_landing_screen(request):
    return render(request, "manage_resources/wastageType.html")


def load_wastageType_table(request):
    try:
        print("Request In | manage_resources | wastageType.py | load_wastageType_table", request.user)
        dataList = []
        # Todo server side pagination start
        column = request.GET.get('order[0][column]')
        searchtxt = request.GET.get('search[value]')
        order = ""
        if request.GET.get('order[0][dir]') == 'desc':
            order = "-"
        list = ['id', 'wastage_type_name']
        column_name = order + list[int(column)]
        start = int(request.GET.get('start'))
        length = int(request.GET.get('length')) + start
        # Todo server side pagination end
        wastageType_detail = WastageType.objects.filter((Q(id__icontains=searchtxt) | Q(wastage_type_name__icontains=searchtxt)), is_deleted=False)
        total_record = wastageType_detail.count()
        wastageTypedetail = wastageType_detail.order_by(column_name)[start:length]

        for wastage in wastageTypedetail:
            tempList = []
            action = '<div class="btn-group"><a onclick="edit_wastageType_data(' + str(
                wastage.id) + ')" data-toggle="tooltip" title="Edit" class="btn btn-xs btn-default">' \
                            '<i class="fa fa-pencil"></i></a><a onclick="delete_wastageType_detail(' + str(
                wastage.id) + ')" data-toggle="tooltip" title="Delete" class="btn btn-xs btn-danger">' \
                            '<i class="fa fa-times"></i></a></div>'
            tempList.append(wastage.id)
            tempList.append(wastage.wastage_type_name)
            tempList.append(wastage.description)
            if wastage.status_choice:
                tempList.append(
                    '<label class="switch switch-primary"><input type="checkbox" onclick="change_wastageType_status(' + str(
                        wastage.id) + ')" id="wastageType-status" checked ><span></span></label>')
            else:
                tempList.append(
                    '<label class="switch switch-primary"><input type="checkbox" onclick="change_wastageType_status(' + str(
                        wastage.id) + ')" id="wastageType-status"><span></span></label>')
            tempList.append(action)
            dataList.append(tempList)

        data = {'iTotalRecords': total_record, 'iTotalDisplayRecords': total_record, 'aaData': dataList}
    except Exception as exc:
        print('exception ', str(traceback.print_exc()))
        print("Exception In | manage_resources | wastageType.py | load_wastageType_table", exc)
        data = {'iTotalRecords': 0, 'iTotalDisplayRecords': 0, 'aaData': []}
    return HttpResponse(json.dumps(data), content_type='application/json')


@csrf_exempt
def add_new_wastageType(request):
    try:
        print("Request In | manage_resources | wastageType.py | add_new_wastageType", request.user)
        WastageType(
            wastage_type_name=request.POST.get('wastageType_name'),  
            description=request.POST.get('description'),
        ).save()
        data = {'success': 'true'}
    except Exception as exc:
        print('exception ', str(traceback.print_exc()))
        print("Exception In | manage_resources | wastageType.py | add_new_wastageType", exc)
        data = {'error': 'Error Occurred'}
    return HttpResponse(json.dumps(data), content_type='application/json')



def change_wastageType_status(request):
    try:
        print("Request In | manage_resources | wastageType.py | change_wastageType_status", request.user)
        wastageType_obj = WastageType.objects.get(id=request.GET.get('wastageType_id'))
        wastageType_status = request.GET.get('wastageType_status')
        if wastageType_status == 'true':
            wastageType_obj.status_choice = True
        else:
            wastageType_obj.status_choice = False

        wastageType_obj.save()
        data = {'success': 'true'}
    except Exception as exc:
        print('exception ', str(traceback.print_exc()))
        print("Exception In | manage_resources | wastageType.py | change_wastageType_status", exc)
        data = {'error': 'Error Occurred'}
    return HttpResponse(json.dumps(data), content_type='application/json')


def delete_wastageType_detail(request):
    try:
        print("Request In | manage_resources | wastageType.py | delete_wastageType_detail", request.user)
        wastageType_obj = WastageType.objects.get(id=request.GET.get('wastageType_id'))
        wastageType_obj.is_deleted = True
        wastageType_obj.save()
        data = {'success': 'true'}
    except Exception as exc:
        print('exception ', str(traceback.print_exc()))
        print("Exception In | manage_resources | wastageType.py | delete_wastageType_detail", exc)
        data = {'error': 'Error Occurred'}
    return HttpResponse(json.dumps(data), content_type='application/json')


def edit_wastageType_data(request):
    try:
        print("Request In | manage_resources | wastageType.py | edit_wastageType_data", request.user)
        wastageType_obj = WastageType.objects.get(id=request.GET.get('wastageType_id'))
        data = {'success': 'true', 'wastageType_name': wastageType_obj.wastage_type_name, 'description': wastageType_obj.description}
    except Exception as exc:
        print('exception ', str(traceback.print_exc()))
        print("Exception In | manage_resources | wastageType.py | edit_wastageType_data", exc)
        data = {'error': 'Error Occurred'}
    return HttpResponse(json.dumps(data), content_type='application/json')


@csrf_exempt
def update_wastageType_data(request):
    try:
        print("Request In | manage_resources | wastageType.py | edit_wastageType_data", request.user)
        wastageType_obj = WastageType.objects.get(id=request.POST.get('wastageType_id'))
        wastageType_obj.wastage_type_name = request.POST.get('wastageType_name')
        wastageType_obj.description = request.POST.get('description')
        wastageType_obj.save()
        data = {'success': 'true'}
    except Exception as exc:
        print('exception ', str(traceback.print_exc()))
        print("Exception In | manage_resources | wastageType.py | edit_wastageType_data", exc)
        data = {'error': 'Error Occurred'}
    return HttpResponse(json.dumps(data), content_type='application/json')