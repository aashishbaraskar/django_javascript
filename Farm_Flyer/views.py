from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth import logout
from django.shortcuts import render, redirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

from account.models import Profile


class Landing(TemplateView):
    template_name = "account/login.html"


@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        username = request.POST['mobile-number']
        password = request.POST['login-password']
        try:
            Profile.objects.get(primary_contact=username)
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    return render(request, 'account/index.html')
                else:
                    data = {'error': True, 'message': "User is not Active"}
                    return render(request, 'account/login.html', data)
            else:
                data = {'error': True, 'message': "Invalid Password"}
                return render(request, 'account/login.html', data)
        except Profile.DoesNotExist:
            data = {'error': True, 'message': "Invalid Username"}
            return render(request, 'account/login.html', data)
    else:
        data = {'error': True, 'message': "Invalid Data"}
        return render(request, 'account/login.html', data)


@login_required(login_url='/')
def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('/')


@csrf_exempt
def reset_password(request):
    if request.method == 'POST':
        try:
            user_name = request.POST['reminder-mobile']
            Profile.objects.get(primary_contact=user_name)
            data1 = {'error': True, 'message': "Linked is Send to your Registered Mobile Number"}
        except Profile.DoesNotExist:
            data1 = {'error': True, 'message': "Registered number not matched"}
    else:
        data1 = {'error': True, 'message': "Invalid Number"}
    return render(request, 'account/login.html', data1)