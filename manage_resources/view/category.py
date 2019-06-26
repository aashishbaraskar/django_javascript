import json
import traceback
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from manage_resources.models import Category

def category_landing_screen(request):
    category_detail = Category.objects.filter(is_deleted=False)
    print(category_detail)
    return render(request, "manage_resources/Category.html")

def load_category_table(request):
    try:
        print("Request In | manage_resources | category.py | load_category_table", request.user)
        dataList = []
        # Todo server side pagination start
        column = request.GET.get('order[0][column]')
        searchtxt = request.GET.get('search[value]')
        order = ""
        if request.GET.get('order[0][dir]') == 'desc':
            order = "-"
        list = ['id', 'category_name','description']
        column_name = order + list[int(column)]
        start = int(request.GET.get('start'))
        length = int(request.GET.get('length')) + start
        # Todo server side pagination end

        category_detail = Category.objects.filter((Q(id__icontains=searchtxt) | Q(category_name__icontains=searchtxt)),
                                            is_deleted=False)
        total_record = category_detail.count()
        categorydetail = category_detail.order_by(column_name)[start:length]

        for category in categorydetail:
            tempList = []
            action = '<div class="btn-group"><a onclick="edit_category_data(' + str(
                category.id) + ')" data-toggle="tooltip" title="Edit" class="btn btn-xs btn-default">' \
                            '<i class="fa fa-pencil"></i></a><a onclick="delete_category_detail(' + str(
                category.id) + ')" data-toggle="tooltip" title="Delete" class="btn btn-xs btn-danger">' \
                            '<i class="fa fa-times"></i></a></div>'
            tempList.append(category.id)
            tempList.append(category.category_name)
            tempList.append(category.description)
            tempList.append('<img src="'+category.category_image.url+'" alt="avatar" class="img-circle" height="50" width="50">')
            tempList.append(
                '<label class="switch switch-primary"><input type="checkbox" onclick="change_category_status(' + str(
                    category.id) + ')" id="category-status" checked><span></span></label>')
            tempList.append(action)
            dataList.append(tempList)

        data = {'iTotalRecords': total_record, 'iTotalDisplayRecords': total_record, 'aaData': dataList}
    except Exception as exc:
        print('exception ', str(traceback.print_exc()))
        print("Exception In | manage_resources | category.py | load_category_table", exc)
        data = {'iTotalRecords': 0, 'iTotalDisplayRecords': 0, 'aaData': []}
    return HttpResponse(json.dumps(data), content_type='application/json')


@csrf_exempt
def add_new_category(request):
    try:
        print("Request In | manage_resources | category.py | add_new_category", request.user)
        Category(
            category_name=request.POST.get('category_name'),
            description=request.POST.get('category_description'),
            category_image=request.FILES['category_image']
        ).save()
        data = {'success': 'true'}
    except Exception as exc:
        print('exception ', str(traceback.print_exc()))
        print("Exception In | manage_resources | category.py | add_new_category", exc)
        data = {'error': 'Error Occurred'}
    return HttpResponse(json.dumps(data), content_type='application/json')


def change_category_status(request):
    try:
        print("Request In | manage_resources | category.py | change_category_status", request.user)
        category_obj = Category.objects.get(id=request.GET.get('category_id'))
        category_status = request.GET.get('category_status')
        if category_status == 'true':
            category_obj.status_choice = True
        else:
            category_obj.status_choice = False

        category_obj.save()
        data = {'success': 'true'}
    except Exception as exc:
        print('exception ', str(traceback.print_exc()))
        print("Exception In | manage_resources | category.py | change_category_status", exc)
        data = {'error': 'Error Occurred'}
    return HttpResponse(json.dumps(data), content_type='application/json')


def delete_category_detail(request):
    try:
        print("Request In | manage_resources | category.py | delete_category_detail", request.user)
        category_obj = Category.objects.get(id=request.GET.get('category_id'))
        category_obj.is_deleted = True
        category_obj.save()
        data = {'success': 'true'}
    except Exception as exc:
        print('exception ', str(traceback.print_exc()))
        print("Exception In | manage_resources | category.py | delete_category_detail", exc)
        data = {'error': 'Error Occurred'}
    return HttpResponse(json.dumps(data), content_type='application/json')


def edit_category_data(request):
    try:
        print("Request In | manage_resources | category.py | edit_category_data", request.user)
        category_obj = Category.objects.get(id=request.GET.get('category_id'))
        data = {'success': 'true', 'category_name': category_obj.category_name, 'category_description': category_obj.description}
    except Exception as exc:
        print('exception ', str(traceback.print_exc()))
        print("Exception In | manage_resources | category.py | edit_category_data", exc)
        data = {'error': 'Error Occurred'}
    return HttpResponse(json.dumps(data), content_type='application/json')


@csrf_exempt
def update_category_data(request):
    try:
        print("Request In | manage_resources | category.py | edit_category_data", request.user)
        category_obj = Category.objects.get(id=request.POST.get('category_id'))
        category_obj.category_name = request.POST.get('category_name')
        category_obj.description = request.POST.get('category_description')

        try:
            category_obj.category_image = request.FILES['category_image']
        except Exception as exc:
            print("Exception in ", exc)
        category_obj.save()
        data = {'success': 'true'}
    except Exception as exc:
        print('exception ', str(traceback.print_exc()))
        print("Exception In | manage_resources | category.py | edit_category_data", exc)
        data = {'error': 'Error Occurred'}
    return HttpResponse(json.dumps(data), content_type='application/json')






