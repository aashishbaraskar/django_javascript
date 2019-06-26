import json
import traceback
import math, random
from django.conf import settings
from django.db import transaction
from django.shortcuts import render, redirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from account.models import Profile


class Index(TemplateView):
    template_name = "account/index.html"


def register_user(request):
    with open(settings.STATICFILES_DIRS[0] + '\state.json') as f:
        state_data = json.load(f)
    return render(request, 'account/register_user.html', {'state_data': state_data["RestResponse"]["result"]})


def get_city_data(request):
    state_code = request.GET.get('state')
    try:
        with open(settings.STATICFILES_DIRS[0] + "\city.json") as f:
            city_data = json.load(f)
        data = {'city_data': city_data[state_code]}
    except Exception as exc:
        print('Exception For Register User | get_city_data', exc)
        print('exception ', str(traceback.print_exc()))
        data = {}
    return HttpResponse(json.dumps(data), content_type='application/json')


def verify_primary_contact(request):
    # Declare a digits variable
    # which stores all digits
    digits = "0123456789"
    OTP = ""
    data = {}
    try:
        try:
            Profile.objects.get(username=request.GET.get('contact'))
            data = {'result': 'Exist', 'message': "Mobile No Already Exist."}
        except Profile.DoesNotExist:
            # length of password can be chaged
            # by changing value in range
            for i in range(5):
                OTP += digits[math.floor(random.random() * 10)]
            data = {'result': 'Success', 'message': "OTP Send to your given no", 'otp': OTP,
                    'contact': request.GET.get('contact')}
    except Exception as exc:
        print('Exception For Generating OTP | verify_primary_contact', exc)
        print('exception ', str(traceback.print_exc()))
        data = {'result': 'Failure', 'message': "Give Valid Data."}
    return HttpResponse(json.dumps(data), content_type='application/json')


@csrf_exempt
@transaction.atomic
def add_new_reg_user(request):
    sid = transaction.savepoint()  # Transaction open
    try:
        try:
            Profile.objects.get(username=request.POST.get('primary_contact'))
            data = {'success': 'exist', 'message': "Mobile No Already Exist."}
        except Profile.DoesNotExist:
            if Profile.objects.filter(email=request.POST.get('email')).exists():
                data = {'success': 'exist', 'message': "Email Id Already Exist."}
            else:
                user_data = Profile(
                    username=request.POST.get('primary_contact'),
                    primary_contact=request.POST.get('primary_contact'),
                    email=request.POST.get('email'),
                    first_name=request.POST.get('first_name'),
                    last_name=request.POST.get('last_name'),
                    pan_card=request.POST.get('pan_card'),
                    user_type=2
                )
                user_data.save()

                user_data.set_password(request.POST.get('password'))

                user_data.alternate_contact = request.POST.get('alternate_contact')
                user_data.address = request.POST.get('address')
                user_data.city = request.POST.get('city')
                user_data.town = request.POST.get('town')
                user_data.pincode = request.POST.get('pincode')
                user_data.landmark = request.POST.get('landmark')
                user_data.state = request.POST.get('state')

                user_data.beneficiary_name = request.POST.get('beneficiary_name')
                user_data.account_no = request.POST.get('account_no')
                user_data.ifsc_code = request.POST.get('ifsc_code')
                user_data.bank_name = request.POST.get('bank_name')

                user_data.pan_image = request.FILES['pancard_image']
                user_data.save()

                transaction.savepoint_commit(sid)
                data = {'success': 'true'}
    except Exception as exc:
        print('Exception For Register User | add_new_reg_user', exc)
        print('exception ', str(traceback.print_exc()))
        transaction.rollback(sid)
        data = {'error': 'true'}
    return HttpResponse(json.dumps(data), content_type='application/json')