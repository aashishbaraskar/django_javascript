import json
import traceback
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from manage_resources.models import Unit

def unit_landing_screen(request):
    unit_detail = Unit.objects.filter(is_deleted=False)
    return render(request, "manage_resources/units.html",{'unit_detail': unit_detail})

def load_unit_table(request):
    try:
        print("Request In | manage_resources | units.py | load_unit_table", request.user)
        dataList = []
        # Todo server side pagination start
        column = request.GET.get('order[0][column]')
        searchtxt = request.GET.get('search[value]')
        order = ""
        if request.GET.get('order[0][dir]') == 'desc':
            order = "-"
        list = ['id', 'unit_name','base_unit']
        column_name = order + list[int(column)]
        start = int(request.GET.get('start'))
        length = int(request.GET.get('length')) + start
        # Todo server side pagination end

        unit_detail = Unit.objects.filter((Q(id__icontains=searchtxt) | Q(unit_name__icontains=searchtxt)),
                                            is_deleted=False)
        total_record = unit_detail.count()
        unit_detail = unit_detail.order_by(column_name)[start:length]

        for units in unit_detail:
            tempList = []
            action = '<div class="btn-group"><a onclick="edit_unit_data(' + str(
                units.id) + ')" data-toggle="tooltip" title="Edit" class="btn btn-xs btn-default">' \
                            '<i class="fa fa-pencil"></i></a><a onclick="delete_unit_detail(' + str(
                units.id) + ')" data-toggle="tooltip" title="Delete" class="btn btn-xs btn-danger">' \
                            '<i class="fa fa-times"></i></a></div>'
            tempList.append(units.id)
            tempList.append(units.unit_name)
            tempList.append(units.base_unit)
            tempList.append(
                '<label class="switch switch-primary"><input type="checkbox" onclick="change_unit_status(' + str(
                    units.id) + ')" id="unit-status" checked><span></span></label>')
            tempList.append(action)
            dataList.append(tempList)

        data = {'iTotalRecords': total_record, 'iTotalDisplayRecords': total_record, 'aaData': dataList}
    except Exception as exc:
        print('exception ', str(traceback.print_exc()))
        print("Exception In | manage_resources | units.py | load_unit_table", exc)
        data = {'iTotalRecords': 0, 'iTotalDisplayRecords': 0, 'aaData': []}
    return HttpResponse(json.dumps(data), content_type='application/json')



@csrf_exempt
def add_new_unit(request):
    try:
        print("Request In | manage_resources | units.py | add_new_unit", request.user)
        Unit(
            unit_name=request.POST.get('unit_name'),
            base_unit=request.POST.get('base_unit'),
        ).save()
        data = {'success': 'true'}
    except Exception as exc:
        print('exception ', str(traceback.print_exc()))
        print("Exception In | manage_resources | units.py | add_new_unit", exc)
        data = {'error': 'Error Occurred'}
    return HttpResponse(json.dumps(data), content_type='application/json')


def change_unit_status(request):
    try:
        print("Request In | manage_resources | units.py | change_unit_status", request.user)
        unit_obj = Unit.objects.get(id=request.GET.get('unit_id'))
        unit_status = request.GET.get('unit_status')
        if unit_status == 'true':
            unit_obj.status_choice = True
        else:
            unit_obj.status_choice = False

        unit_obj.save()
        data = {'success': 'true'}
    except Exception as exc:
        print('exception ', str(traceback.print_exc()))
        print("Exception In | manage_resources | units.py | change_unit_status", exc)
        data = {'error': 'Error Occurred'}
    return HttpResponse(json.dumps(data), content_type='application/json')


def delete_unit_detail(request):
    try:
        print("Request In | manage_resources | units.py | delete_unit_detail", request.user)
        unit_obj = Unit.objects.get(id=request.GET.get('unit_id'))
        unit_obj.is_deleted = True
        unit_obj.save()
        data = {'success': 'true'}
    except Exception as exc:
        print('exception ', str(traceback.print_exc()))
        print("Exception In | manage_resources | units.py | delete_unit_detail", exc)
        data = {'error': 'Error Occurred'}
    return HttpResponse(json.dumps(data), content_type='application/json')


def edit_unit_data(request):
    try:
        print("Request In | manage_resources | units.py | edit_unit_data", request.user)
        unit_obj = Unit.objects.get(id=request.GET.get('unit_id'))
        data = {'success': 'true', 'unit_name': unit_obj.unit_name, 'base_unit': unit_obj.base_unit}
    except Exception as exc:
        print('exception ', str(traceback.print_exc()))
        print("Exception In | manage_resources | units.py | edit_unit_data", exc)
        data = {'error': 'Error Occurred'}
    return HttpResponse(json.dumps(data), content_type='application/json')


@csrf_exempt
def update_unit_data(request):
    try:
        print("Request In | manage_resources | units.py | edit_unit_data", request.user)


        unit_obj = Unit.objects.get(id=request.POST.get('unit_id'))
        unit_obj.unit_name = request.POST.get('unit_name')
        unit_obj.base_unit = request.POST.get('base_unit')
        unit_obj.save()
        data = {'success': 'true'}
    except Exception as exc:
        print('exception ', str(traceback.print_exc()))
        print("Exception In | manage_resources | units.py | edit_unit_data", exc)
        data = {'error': 'Error Occurred'}
    return HttpResponse(json.dumps(data), content_type='application/json')






